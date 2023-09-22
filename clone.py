import requests
import os

organization = 'your_organization'
access_token = 'your_access_token'

# Lấy danh sách repositories trong organization
url = f'https://api.github.com/orgs/{organization}/repos'
headers = {'Authorization': f'token {access_token}'}
response = requests.get(url, headers=headers)
repos = response.json()

# Clone ALl repository
for repo in repos:
    repo_name = repo['name']
    repo_url = repo['ssh_url']
    os.system(f'git clone {repo_url}')
