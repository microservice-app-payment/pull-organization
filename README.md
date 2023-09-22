# pull-organization
1. Using CMD
```
for repo in $(curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/<your_organization>/repos | jq -r '.[] | .ssh_url'); do git clone $repo; done
```
2. Run Python app
```
python clone.app
```
