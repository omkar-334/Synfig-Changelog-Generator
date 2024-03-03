#Extract Pull Request id from this commits
import re
import os

from github import Github
from git import Repo

repo_path = None
remote = False

pr_list1 = []
pr_list2 = []

if not remote:
# For a local repository
    repo_path = os.getcwd() + "\\" + "Synfig_Repo"
    repo = Repo(repo_path)
    commits = list(repo.iter_commits())[:1000] # Select first 1000 Commits for faster results
    for i in commits:
        match = re.search(r'(?:#|Pull request #)(\d+)', i.message)
        if match:
            pr_id = match.group(1)
            pr_list1.append([i.hexsha, pr_id])
    print(pr_list1)

else:
    # For a remote repository
    # repo_path = 'synfig/synfig'
    token = open('token.txt','r').read()
    github = Github(token)
    grepo = github.get_repo(repo_path)

    commits = grepo.get_commits()[:10]   # Select first 10 Commits for faster results
    for i in commits:
        temp = [[pr.number, pr.title] for pr in i.get_pulls()]
        if temp not in pr_list2:
            pr_list2.append(temp)
    print(pr_list2)
