import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

response1 = requests.get(url)
print(response1.text)
arg1 = {"method":"GET"}
response_get = requests.head(url, params=arg1)
response_get = requests.get(url, params=arg1)
print(response_get.text)
responses = ["POST", "GET", "PUT", "DELETE"]
for type_of_param in responses:

    response_get = requests.get(url, params= {"method":type_of_param})
    print(type_of_param, "get",  response_get.text)

    response_post = requests.post(url, data={"method":type_of_param})
    print(type_of_param, "post", response_post.text)

    response_put = requests.put(url, data={"method":type_of_param})
    print(type_of_param, "put", response_put.text)

    response_delete = requests.delete(url, data={"method":type_of_param})
    print(type_of_param, "delete", response_delete.text)

    print()