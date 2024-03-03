import subprocess
import os
from pathlib import Path
path = r'c:\Users\omkar\Desktop\Synfig\Synfig_Repo'

#To extract Pull Requests and their ids, add ' --grep="pull request"' at the end of the command.
#THis will search for the words 'pull request' in the commit messages.
def sys_merge_extractor(repo_path : str):
    out = subprocess.run('git log --oneline --merges', shell=True, cwd=path,stdout = subprocess.PIPE)
    out = out.stdout.decode('utf-8')
    return out

def sys_direct_extractor(repo_path : str):
    out = subprocess.run('git log --oneline --no-merges', shell=True, cwd=path,stdout = subprocess.PIPE)
    out = out.stdout.decode('utf-8')
    return out

print(sys_merge_extractor(path))