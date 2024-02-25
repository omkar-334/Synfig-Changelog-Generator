import re
import os
from git import Repo
from github import Github


token = open('token.txt','r').read()
github = Github(token)

remote_path = 'synfig/synfig'

folder = "Synfig_Repo"
local_path = os.getcwd() + "\\" + folder

def merge_extractor(repo_path : str, remote=True):
    """
    Args:
        repo_path (str): Path of the repository
        remote (bool): True if remote repository, False for local

    Returns:
        list[list[str]]: List of merges
    """
    if remote:
        repo = github.get_repo(repo_path)
        output = []
        commits = repo.get_commits()
        merges = [i for i in commits[:500] if 'merge' in i.commit.message.lower()]
        merge_list = [[i.sha, i.commit.author.name, i.commit.author.date, i.commit.message] for i in merges]

    else:
        repo = Repo(repo_path)
        gitlog = repo.git.log('--merges')
        pattern = r"commit [0-9a-f]+\nMerge: ([0-9a-f]+\s[0-9a-f]+)+\nAuthor: (.+)\nDate: (.+)\n\n\s+(.+)\n"
        info = re.findall(pattern, gitlog, re.MULTILINE)
        merge_list = [[merge, author, date, message] for merge, author, date, message in info]

    return merge_list

output = merge_extractor(local_path, remote=False)
print(output)

