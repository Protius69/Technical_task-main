# -*- coding: utf-8 -*-
from typing import Union, Any

import vertica_python
import pandas as pd
from datetime import datetime
from connection_test import conn_vertica_info, range_day, today, week_number, teams_911

team = str(teams_911['911_CC'])
team = team.replace('[','').replace(']','')
print(team)

utcnow = datetime.utcnow()



vertica_query = f"""
with status_time as (select
      j.id as amount
      , ci.oldstring as status
      , au.lower_user_name as Login
      ,'SD911-'||j.issuenum as Ticket
      , case 
          when lag(cg.created) over (partition by j.id order by cg.created) is null
              then j.created
          else lag(cg.created) over (partition by j.id order by cg.created)
      end as start_date 
      , cg.created as end_date
    from prodjiradb.jiraissue j
    join prodjiradb.changegroup cg
        on cg.issueid = j.id
    join prodjiradb.customfieldvalue cfv 
        on cfv.issue = j.id and cfv.customfield = 17032
    join prodjiradb.changeitem ci
        on ci.groupid = cg.id and ci.field = 'status'
    join prodjiradb.app_user au
        on au.user_key = cg.author 
    where j.project = 16601 
        and j.created > '{range_day}'
        and j.created < '{today.strftime("%Y-%m-%d")}'
        and resolution is not null)
select
  Login
  , sum(diff) as sum, count(distinct amount) as count
from
  (select 
     Login
     , amount
     , case 
       when date_part('hour', start_date) >= 17 and date(start_date) != date(end_date)
               or date_part('hour', start_date) < 5 and date_part('hour', end_date) >= 5
               then end_date::time - '04:59:00'
       else end_date - start_date
     end as diff
  from status_time
  where status in ('В работе') and Login in ({team})) t
group by Login
Order by 2
"""

print(vertica_query)

with vertica_python.connect(**conn_vertica_info) as vertica_conn:
    vertica_curs = vertica_conn.cursor()
    vertica_curs.execute(vertica_query)
    rows = vertica_curs.fetchall()

df_by_time = pd.DataFrame(rows)
df_by_time.columns = ['login', 'sum', 'count']
df_by_time['sum']= utcnow + df_by_time['sum'] - utcnow
df_by_time['sum'] = round((df_by_time['sum'].dt.total_seconds()/60), 4)
df_by_time.loc['Total',:] = df_by_time.sum(axis=0)
df_by_time.at['Total','login'] = 'Total'
df_by_time['avg_time'] = round((((((df_by_time['sum']*60)/df_by_time['count']) // 60))+(((df_by_time['sum']*60)/df_by_time['count'])%60/100)),2)
df_by_time['week'] = week_number
df_by_time['upload_date'] = today.strftime("%Y-%m-%d")

print(df_by_time)
df_by_time.to_csv('~/Desktop/time.csv')