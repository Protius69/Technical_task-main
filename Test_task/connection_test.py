# -*- coding: utf-8 -*-
from jira.client import JIRA
from datetime import datetime, timedelta

# ------------- count weekday, weeknumber, rangeday MONDAY TO MONDAY ------------------ #

today = (datetime.today() + timedelta(hours=3))

# today = datetime.strptime("2022-07-11", "%Y-%m-%d") #3 10 17 24

print(today, " datetime now")
weekday = 8 if today.isoweekday() == 1 else today.isoweekday()

range_day = (today - timedelta(days=weekday - 1)).strftime("%Y-%m-%d")

print(range_day, "range_day дата понедельника")

week_number = (today - timedelta(days=1)).strftime("%y_%W")

print(week_number, " its number week")

if weekday != 8:
    today += timedelta(days=1)
    print(f"сегодня НЕ понедельник, поэтому выносим правую границу запроса в будущее = {today}")

# ------------- count weekday, weeknumber, rangeday FOR FRIDAY TO FRIDAY ------------------ #
# посчитаем нужный нам range_day (отсчитываемый от пятницы к пятнице)
# СБ = -1д, ПТ = -7д (с учетом того, что крона работает в 00:05 самом начале дня)
# двигаем на три часа, так как на проде UTC
today_shift = (datetime.today() + timedelta(hours=3))

weekday_shift = today_shift.isoweekday()
weekday_shift = weekday_shift + (-5 if weekday_shift > 5 else +2)
range_day_shift = (today_shift - timedelta(days=weekday_shift)).strftime("%Y-%m-%d")

print(range_day_shift, " дата стартовой пятницы")
# нужно получить формат номера недели такой "YY_mm"
week_number_shift = (today_shift + timedelta(days=2)).isocalendar()[1]
week_number_shift = f'{(today_shift + timedelta(days=2)).isocalendar()[0]}_{("0" + str(week_number_shift)) if week_number_shift < 10 else week_number_shift}'
week_number_shift = week_number_shift[-5:]

# сделаем так, чтобы во все дни недели (КРОМЕ ПЯТНИЦЫ) данные брались на текущий момент по сегодняшний день изменени тоже.
if weekday != 7:
    today_shift += timedelta(days=1)
    print(f"сегодня НЕ пятница, поэтому выносим правую границу запроса в будущее = {today_shift}")


#Логин и пароль жира обязательно в кавычках
secrets = {"jira_token":"Твой Jira токен"}

# -------------------------------------------------------------------

default_headers = JIRA.DEFAULT_OPTIONS["headers"].copy()
default_headers["UserAgent"] = "python_cronjobs_911cc"

jira_headers = {**default_headers}
jira_headers["Authorization"] = f"Bearer {secrets['jira_token']}"
jira_options = {
	"headers": jira_headers
}
jira = JIRA(server="https://jira.o3.ru/", options=jira_options)


# ------------------------------------------------------------------------------ #
