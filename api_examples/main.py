'''
from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")
'''
'''
import requests
responce = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(responce.status_code)
print(responce.text)
'''
'''
import requests

headers = {"some_header":"123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
# тут заголовки, которые мы отправили
print(response.text)
# а тут которые получили
print(response.headers)
'''

#куки
import requests
payload = {"login":"secret_login", "password":"secret_pass"}
responce = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data = payload)
print(responce.text)
print(responce.status_code)
print(dict(responce.cookies))

print(responce.headers)

'''
{
   "Date":"Sat, 14 May 2022 15:30:29 GMT",
   "Content-Type":"text/html; charset=utf-8",
   "Content-Length":"0",
   "Connection":"keep-alive",
   "Keep-Alive":"timeout=10",
   "Server":"Apache",
   "Set-Cookie":
                "auth_cookie=274692; - название
                expires=Tue, - значение
                14-Jun-2022 15:30:29 GMT; - дата, до которой эти куки акутальны
                Max-Age=2678400; - домен, к которому она относится
                path=/; domain=playground.learnqa.ru; - часть URL без домена, для которой эти куки нужно передавать
                HttpOnly", - флаг, чтобы куки была защищена от XSS и CSRF атак
   "Cache-Control":"max-age=0",
   "Expires":"Sat, 14 May 2022 15:30:29 GMT"
}
'''