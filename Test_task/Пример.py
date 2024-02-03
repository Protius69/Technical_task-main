# -*- coding: utf-8 -*-

import pandas as pd

from connection_test import jira, range_day, today
from support_func import get_all_issues

# -----------------------------------------------------#

#Фильтр жира (обязательно начинается с f и в кавычках)
#range_day дата последнего понедельника, today - сегодняшняя дата+1 день если сегодня не понедельник
jql = f"project = SD911 AND assignee was in membersOf(911_CC_Team) AND createdDate >= {range_day} AND createdDate < {today.strftime('%Y-%m-%d')}"

#Выбираем необходимые для выгрузки поля заявки, для моего примера нужно всего 2 это имя заявки в формате SD911-****** и поле CRT
fields = ['key', 'customfield_12700']


issues = get_all_issues(jira, jql, fields) #Функция вызова жира

#Создаем сводную таблицу выбираем необходимые поля
df_sd_tickets = {'count_sd': [], 'crt': []}

#Делаем запрос в жиру и заполняем сводную таблицу

for issue in issues:
    df_sd_tickets['count_sd'].append(issue.key)
    #Поскольку не у всех заявок может быть заполнено поле CRT запускаем проверку на заполненость поля
    if (issue.fields.customfield_12700) is None:
        df_sd_tickets['crt'].append('Empty')
    else:
        df_sd_tickets['crt'].append(issue.fields.customfield_12700.requestType.name)

#Преобразуем сводную таблицу в датафрейм
df_sd_tickets = pd.DataFrame(df_sd_tickets)

#Суммируем данные из сводной таблицы в итоговую
df_crt = df_sd_tickets.groupby(by=['crt'])[['count_sd']].count().reset_index()
#Добавляем столбец с датой загрузки
df_crt['upload_date'] = today.strftime("%Y-%m-%d")
#Преобразуем столбец в формат даты
df_crt['upload_date'] = pd.to_datetime(df_crt['upload_date']).dt.date

print(df_crt) #выводим итоговую таблицу
df_crt.to_csv('~/Desktop/crt_gropped.csv') #Сохраняем таблицу на рабочий стол в формате csv


