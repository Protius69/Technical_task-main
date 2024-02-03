from datetime import datetime

def get_duration(start, end):
    end = end if end != 'None' else datetime.today().strftime('%Y-%m-%d')
    if start:
        return (datetime.strptime(end, '%Y-%m-%d') - datetime.strptime(start, '%Y-%m-%d')).days
    return 'None'

# Ограничение выгрузки тикетов
def get_all_issues(jira_client, query, fields):
    issues = []
    i = 0
    chunk_size = 300
    while True:
        chunk = jira_client.search_issues(query, fields=fields,
                                          startAt=i, maxResults=chunk_size)
        i += chunk_size
        issues += chunk.iterable
        if i >= chunk.total:
            break
        print(i, "выгружено тикетов с Jira")
    return issues
