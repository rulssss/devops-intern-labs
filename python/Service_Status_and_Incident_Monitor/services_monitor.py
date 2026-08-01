import json


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