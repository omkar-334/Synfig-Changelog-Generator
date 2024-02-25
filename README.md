# Automated release notes generator and packaging script fixes (175 or 350 hrs)

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

175 hour
 - Changelog file can be generated automatically

350 hour
 - AppImage bundle can be generated automatically
 - Debian and Flatpak packages can be generated automatically (optional)

Difficulty: Easy/Mediu
Skills required/preferred: Python/C+
Possible mentor(s): Ayush Chamoli, Rodolfo Ribeiro Gome
Expected size of project: 175 or 350 hour