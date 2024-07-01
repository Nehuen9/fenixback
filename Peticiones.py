import requests

consulta  = requests.get("https://jasonplaceholder.typicode.com/users")

print(consulta.status_code)

#validar cont