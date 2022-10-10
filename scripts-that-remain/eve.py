import requests

x = requests.get('https://api.github.com/users/mayankt18')

print(x)

print(x.content)
