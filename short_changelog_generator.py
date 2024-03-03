import re
import markdown
from github import Github

repo_path = 'synfig/synfig'
token = open('token.txt','r').read()
github = Github(token)
repo = github.get_repo(repo_path)


commits = repo.get_commits()[:50]
output = [[i.commit.author.name, i.commit.author.date, i.commit.message, i.html_url] for i in commits]

icondict = {'feat':'✨', 'fix': '🐛', 'docs':'📚', 'style': '💎', 'refactor': '♻️', 'perf':'🚀', 'test'  :'✅', 'build': '📦', 'ci':'👷', 'chore': '🔧'}

pattern = '|'.join(re.escape(keyword) for keyword in icondict.keys())
regex = re.compile(pattern, flags=re.IGNORECASE)


with open("SHORT_CHANGELOG.md", "w", encoding="utf-8") as file:
    for commit in output:
        author = "[" + commit[0]+"](https://github.com/" + commit[0] +")  "
        date = "#### " +commit[1].strftime('%d-%m-%Y %H:%M')
        temp = re.split(":", commit[2])
        type = regex.search(temp[0])[0]
        icon = icondict.get(type)
        message = re.split(r"\n", temp[1])[0]

        line1 = markdown.markdown(date + "    -    " + author)
        line2 = markdown.markdown(icon + "   " + temp[0] + "   :   " + "[" + str(message) + "](" + commit[3] + ")  ")

        file.write(line1)
        file.write(line2)
        file.write('<br>')

