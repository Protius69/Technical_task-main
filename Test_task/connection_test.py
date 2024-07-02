# -*- coding: utf-8 -*-
from typing import Union, Any

from jira.client import JIRA
import requests
from datetime import datetime, timedelta
from proto.staff_public_api_pb2 import DESCRIPTOR as desc_staff_public_api
from grpc_requests import StubClient


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


#Токен жира обязательно в кавычках
secrets = {"jira_token":"Твой Jira токен",
		   "vertica_user": "доменный логин(без @ozon.ru)",
		   "vertica_password": "доменный пароль",
           "s2s-client-secret": "обратись к Сане"
           }

#Подключение к Jira

default_headers = JIRA.DEFAULT_OPTIONS["headers"].copy()
default_headers["UserAgent"] = "python_cronjobs_911cc"
jira_headers = {**default_headers}
jira_headers["Authorization"] = f"Bearer {secrets['jira_token']}"
jira_options = {
	"headers": jira_headers
}
jira = JIRA(server="https://jira.o3.ru/", options=jira_options)

#Подключение к Вертике

conn_vertica_info = {
    'host': 'vertica-sandbox.s.o3.ru',
    'port': 5433, 'database': 'OLAP',
    'user': secrets['vertica_user'],
    'password':  secrets['vertica_password'],
    'read_timeout': 10,
    'unicode_error': 'strict',
    'ssl': False,
    'use_prepared_statements': False,
    # 'connection_timeout': 10
}

#Подключение к Staff для получения списка сотрудников
def get_auth_token(target_service):
	SERVICE_NAME = "s2s|cronjobs"
	AUTH_HOST = "https://sso.o3.ru/auth/realms/service2service/protocol/openid-connect/token"


	dataStr = 'grant_type=client_credentials&client_id=' + SERVICE_NAME + '&client_secret=' + secrets['s2s-client-secret'] + '&scope=' + target_service
	response = requests.post(AUTH_HOST, data=dataStr, headers={'Content-Type': 'application/x-www-form-urlencoded'})
	if response.status_code == 200:
		jsonAuthResponse = response.json()
		return str(jsonAuthResponse['token_type'] + ' ' + jsonAuthResponse['access_token'])
	return "Error Keycloak: " + str(response.status_code) + " | " + str(response.text)

def new_staff_public_api_client():
	service_descriptor = desc_staff_public_api.services_by_name['StaffPublicAPI']

	client = StubClient.get_by_endpoint(f"staff-public-api.kdp.svc.prod.k8s.o3.ru:82", service_descriptors=[service_descriptor, ])

	staff_public_api_client = client.service("ozon.kdp.api.staff_public_api.api.staff_public_api.v1.StaffPublicAPI")

	staff_api_token = get_auth_token("s2s|staff-public-api")

	metadata = (('x-o3-app-name', 'cronjobs'), ('x-o3-s2s', staff_api_token))

	return staff_public_api_client, metadata

staff_public_client, metadata = new_staff_public_api_client()

guid_dict = {
	"911_CC" : "23324236-a31a-11ea-90f9-9418826ee072"
}

teams_911 = {}
for team, guid in guid_dict.items():
	teams_911[team] = []
	# URL = f"http://staff-public-api.prod.a.o3.ru:80/employees/org?guids={guid}"
	payload = {
		"guids": [guid],
	}

	response = staff_public_client.GetEmployeesByOrgGuids(payload, metadata=metadata)
	employees = response['orgEmployees'][0]['employees']

	# response = requests.get(URL, headers=headers_staff)
	# if response.status_code != 200:
		# print(response, f"problems with {URL}")
	# res = response['orgEmployees'][0]['employees']
	# print(json.dumps(res, sort_keys=True, indent=4))
	# print(len(res), "сотрудников ", team)

	for item in employees:
		teams_911[team].append(item['person']['login'])
		# print(item['person']['login'])
print("911_CC: ", teams_911['911_CC'])

# ------------------------------------------------------------------------------ #
