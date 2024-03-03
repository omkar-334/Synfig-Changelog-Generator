# Automated release notes generator and packaging script fixes (175 or 350 hrs)

### Getting Started
1. First, either clone or download this repository onto your machine
```git clone https://github.com/omkar-334/Synfig-Changelog-Generator.git```

2. Then, install dependencies
```pip install -r requirements.txt```
Although there are only 2 libraries required - GitPython and PyGithub, it is better to install all requirements.

3. Get Github API token
Go to your GitHub account.
Account Settings -> Developer Settings -> Personal Access tokens -> Tokens (Classic)
Generate a new token.
Create a file named 'token.txt' in this directory and store your token in the file.

Tested Python version - 3.9.13
OS - Windows 11

### Running the code

##### task1
 Merged Commits extractor, Direct Commits extractor
 How it works
  - Merged Commit - the new commit has previous merged commits(2 or more) as parents
  - Direct Commit - the previous commit becomes the parent of the new commit. Hence the new commit has only 1 parent.
 So to check the type of commit, we need to find out the number of parents.

 Both functions have 2 parameters:
  - repo_path (str, path of the repository, either local path or github path)
  - remote (bool, True if remote repo, False if local repo)

###### Systemcall.py
   - It uses the ```subprocess``` module to interact with the command line and capture output of the command.
   - Git log command is used.
   - ```--oneline``` tag is used for a short one line message.
   - ```--merges``` tag is used to extract only merged commits.
   - ```--no-merges``` tag is used to extract only direct commits.
   - ```--grep="pull request"``` tag is used to extract Pull requests and their ids. (This tag will not work along with ```--no-merges```, as a PR is considered a merge.)

##### task2
Extracting Pull Request IDs from commits
2 variables have to be set:
  - repo_path (str, path of the repository, either local path or github path)
  - remote (bool, True if remote repo, False if local repo)

##### task3
 Extract PR information using GitHub API
 3 Variables have to be set:
  - Username (str, your personal username)
  - repo_path (str, path of the github repository)

##### Short Changelog Generator  
 Extracts the datetime, author, message and url of the commit using the PyGithub library.  
 Generates a markdown changelog file (along with icons).  