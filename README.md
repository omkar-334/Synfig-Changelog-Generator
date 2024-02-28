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


### Description
We use Conventional commits (https://www.conventionalcommits.org/en/v1.0.0/) for git commits, so we can automatically split messages into groups (bug fixes, features, etc.)
 - Add script which extract git messages starting from start_commit_id to commit_id (this can be achieved by using formatted git log output)
 - Group these messages by type and output them in HTML/markdown format
 - Add this script to CI pipeline (so it will show to user how it changes final changelog) (optional)

### AppImage bundler
We are currently using AppImage to prepare bundle for Linux, but we are using AppImage 1.0 which is outdated and needs to be updated
 - Write a script for packaging AppImage (there are ready-made scripts for packaging AppImage, but you need to check if they work correctly)

### Debian package and Flatpak packag
 - Write a script for automated Debian and Flatpak packages (Optional)

### Where to begin
Try extracting a list of messages from the git log output using the following requirements
 - Extract only merge commits or direct commits
 - Extract Pull Request id from this commits
 - Extract Pull Request description using Github API (this is necessary because PR may contain images and extended information)

### Expected outcome
175 hour - Changelog file can be generated automatically
350 hour - AppImage bundle, Debian and Flatpak packages can be generated automatically

Difficulty: Easy/Medium
Skills required/preferred: Python/C+
Possible mentor(s): Ayush Chamoli, Rodolfo Ribeiro Gome
Expected size of project: 175 or 350 hour
