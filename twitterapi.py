import requests

req={
     'email':'yash'
}
r = requests.get('https://twitter.com/account/begin_password_reset', params=req)
print(r.url)
print(r.status_code)
print(r.json())
