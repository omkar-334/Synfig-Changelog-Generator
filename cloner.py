import os
from git import Repo
from task1 import merge_extractor

repo_url = 'https://github.com/synfig/synfig.git'
repo_local = "Synfig_Repo"

repo_path = os.getcwd() + "\\" + repo_local
Repo.clone_from(repo_url, repo_local)

result = merge_extractor(repo_path, remote = False)

