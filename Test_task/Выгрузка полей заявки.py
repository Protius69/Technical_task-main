from connection_test import jira

jql = f"project = 'SD911' AND key = SD911-3356243"

issues = jira.search_issues(jql, maxResults=1)
print(issues.total)
for issue in issues:
    print(issue.key)

    for field_name in issue.raw['fields']:
        print ("Field:", field_name, "Value:", issue.raw['fields'][field_name])

