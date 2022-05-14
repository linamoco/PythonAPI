import requests
payload = {"login":"secret_login", "password":"secret_password"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data = payload)

cookie_value = response1.cookies.get("auth_cookies")
cookies = {}
if cookie_value is not None:
    cookies.update({"auth_cookie": cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response2.text)