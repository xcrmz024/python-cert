# 1. Script que lee JSON:
import json

users = []

# 4. Manejo de errores de archivo:
try:
    with open("src/mod2_fundamentos_lenguaje/data/users.json", "r") as file:
        users = json.load(file)
# error de archivo (FileNotFoundError exception):
except FileNotFoundError:
    print("No se encontró el archivo users.json")

# error de formato (json.JSONDecodeError):
except json.JSONDecodeError:
    print("El archivo no contiene un JSON válido")


print(users)
print(type(users))  # list
print(type(users[0]))  # dict

# recorrido lista users - acceso por dict (user):
adults = []

for user in users:
    # 2. Filtrar datos:
    if user["age"] >= 18:
        adults.append(user)

        # 3. Agregar datos:
        user["is_adult"] = True

print(adults)
