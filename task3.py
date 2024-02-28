#Extract Pull Request description using Github API (this is necessary because PR may contain images and extended information)

import requests

username = 'omkar-334'
repo_path = 'synfig/synfig'

url = f'https://api.github.com/repos/{repo_path}/pulls'
token = open('token.txt','r').read()

response = requests.get(url, auth=(username, token))

if (sc:=response.status_code) == 200:
    pull_requests = response.json()

    for pr in pull_requests:
        print(f"Pull Request #{pr['number']}: {pr['title']}")
        print(f"Created by: {pr['user']['login']}")
        print(f"Description: {pr['body']}")
        print(f"URL: {pr['html_url']}")
        print()
else:
    print(f"Failed. Status code: {sc}")
