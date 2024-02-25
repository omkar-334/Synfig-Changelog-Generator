#Extract only merge commits or direct commits

import re
import os
from git import Repo
from github import Github


# Direct Commit - the previous commit becomes the parent of the new commit. Hence the new commit has only 1 parent.
# Merged Commit - the new commit has previous merged commits(2 or more) as parents

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
        commits = repo.get_commits()[:100]  # Select first 100 commits for faster results
        merges = [i for i in commits if 'merge' in i.commit.message.lower()]
        merge_list = [[i.sha, i.commit.author.name, i.commit.author.date, i.commit.message] for i in merges]

    else:
        repo = Repo(repo_path)
        gitlog = repo.git.log('--merges')
        pattern = r"commit [0-9a-f]+\nMerge: ([0-9a-f]+\s[0-9a-f]+)+\nAuthor: (.+)\nDate: (.+)\n\n\s+(.+)\n"
        info = re.findall(pattern, gitlog, re.MULTILINE)
        merge_list = [[merge, author, date, message] for merge, author, date, message in info]

    return merge_list

#To filter for direct commits, we need to check if the commit has only 1 parent.

def direct_extractor(repo_path : str, remote=True):
    """
    Args:
        repo_path (str): Path of the repository
        remote (bool): True if remote repository, False for local

    Returns:
        list[list[str]]: List of direct commits
    """
    if remote:
        repo = github.get_repo(repo_path)
        output = []
        commits = repo.get_commits()[:100]  # Select first 100 Commits for faster results
        direct_commits = [i for i in commits if len(i.parents) == 1]
        direct_list = [[i.sha, i.commit.author.name, i.commit.author.date, i.commit.message] for i in direct_commits]

    else:
        repo = Repo(repo_path)
        commits = list(repo.iter_commits())[:50]  # Select first 50 Commits for faster results
        direct_commits = [i for i in commits if len(i.parents) == 1]
        direct_list = [[i.hexsha, i.author.name, i.authored_datetime, i.message] for i in direct_commits]

    return direct_list


