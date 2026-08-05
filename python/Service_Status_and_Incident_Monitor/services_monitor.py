import json

# 🎯 2. Your Assignment in Python

#Write a Python program (`monitor_servicios.py`) that performs the 
# following tasks:

# JSON Reading
#Use Python's native `json` module (`import json`) to open and load
#  the `servicios.json` file (you can research the `json.load(file)` function).

# Processing with Dictionaries
# Iterate through the list of services.
# Filter those whose status is **NOT** "UP" (i.e., those that are "DOWN" 
# or "DEGRADED").
# Save the problematic services into a new list using dictionaries or 
# tuples (e.g., `{"name": "...", "status": "...", "latency": ...}`).

## General Metrics
#Calculate the availability percentage of your infrastructure:

# Reporting
#Export the result to a new JSON file named `alertas.json` containing
#  only the incident report and the overall availability percentage.


def guardar_file(services_with_problems):

    #El método json.dump() convierte la estructura de datos de 
    # Python (diccionarios, listas, etc.)
    #  a texto en formato JSON y la escribe en el file.


    with open("alertas.json", "w") as alertas:
        json.dump(services_with_problems, alertas, indent=4) 
                    #diccionario,     file a crear, indentacion estandar

def read_file():
    with open("services.json", "r") as f:
        datos = json.load(f)  # 'datos' se convierte automáticamente en una lista de diccionarios
    return datos

def principal():

    services_with_problems = []
    
    file = read_file()

    c_services = len(file)
    c = 0 

    for i in file:
        if i["estado"] != "UP":
            c += 1
            item = {
                "nombre" : i["servicio"],
                "estado" : i["estado"],
                "latencia" : i["latencia_ms"],
            }

            services_with_problems.append(item)

    percentage = (c / c_services) * 100 # corregido pedia el porcentaje no descuento.
    
    
    item2 = {
        "disponibilidad en porcentaje" : percentage,
        "cantidad de servicios" : c_services,
        "servicios con problemas" : len(services_with_problems),
        "incidentes" : services_with_problems,
    }
    
    guardar_file(item2)
            









if __name__ == "__main__":

    principal()


#If we need get an API:

#import requests

# 1. Hacemos la petición a la API (pedimos datos)
#response = requests.get("https://api.github.com/users/octocat")

# 2. Convertimos la respuesta JSON directamente a un diccionario de Python
#data = response.json()

# 3. Usamos los datos como ya sabés hacer
#print(f"Usuario: {data['login']}")
#print(f"Repos públicos: {data['public_repos']}")