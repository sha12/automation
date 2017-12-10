from jira import JIRA
import webbrowser
import sys
connect_options = {'server': 'https://jira3.int.net.nokia.com'}
jira_obj = JIRA(connect_options, basic_auth=("CFW", "CFW"))
issues_in_proj = jira_obj.search_issues("project=SMTRS and component=MT_FW and status not in (Closed, Resolved)" ,maxResults=100, fields='comment,created,reporter')
for issue in issues_in_proj:
    if issue.raw['fields'].get("comment") and not issue.raw['fields'].get("comment").get("comments", ""):
        print issue.key, "link", "https://jira3.int.net.nokia.com/browse/"+issue.key,  "created on", " ".join(issue.raw["fields"].get("created").split("T"))
        if sys.argv[1:] == ["-b"]:
            webbrowser.open("https://jira3.int.net.nokia.com/browse/"+issue.key, new=2)


