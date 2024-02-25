import requests

username = 'omkar-334'
token = open('token.txt','r').read()

owner = 'synfig'
repo = 'synfig'

url = f'https://api.github.com/repos/{owner}/{repo}/pulls'

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    pull_requests = response.json()

    for pr in pull_requests:
        print(f"Pull Request #{pr['number']}: {pr['title']}")
        print(f"Created by: {pr['user']['login']}")
        print(f"Description: {pr['body']}")
        print(f"URL: {pr['html_url']}")
        print()
else:
    print(f"Failed to fetch pull requests. Status code: {response.status_code}")
