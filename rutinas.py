# def choose_routine(mileage):
#     # Dividir kilometraje entre rutina y luego redondearlo para multiplicarlo por cada rutina
#     routine1500 = round(mileage / 1500) * 1500
#     routine4500 = round(mileage / 4500) * 4500
#     routine9000 = round(mileage / 9000) * 9000
#     routine15000 = round(mileage / 15000) * 15000
#     routine18000 = round(mileage / 18000) * 18000

#     # Restar kilometraje menos rutina, y redondear el resultado
#     subtraction1500 = abs(mileage - routine1500)
#     subtraction4500 = abs(mileage - routine4500)
#     subtraction9000 = abs(mileage - routine9000)
#     subtraction15000 = abs(mileage - routine15000)
#     subtraction18000 = abs(mileage - routine18000)

#     # Diccionarios con resultados de las retas y su rutina relacionada
#     subtractions = {
#         subtraction1500: "Rutina de 1 (más cercana en {} km)".format(routine1500),
#         subtraction4500: "Rutina de 2 (más cercana en {} km)".format(routine4500),
#         subtraction9000: "Rutina de 3 (más cercana en {} km)".format(routine9000),
#         subtraction15000: "Rutina de 4 (más cercana en {} km)".format(routine15000),
#         subtraction18000: "Rutina de 5 (más cercana en {} km)".format(routine18000)
#     }

#     # Obtener resultado donde kilometraje y el multiplo sea menor
#     min_subtraction = min(subtractions.keys())
#     # Retornar mensaje dentro de la opción seleccionada
#     return subtractions[min_subtraction]

# def choose_routine(mileage):
#     # Definir las rutinas y sus valores más cercanos
#     routine1500 = round(mileage / 1500) * 1500
#     routine4500 = round(mileage / 4500) * 4500
#     routine9000 = round(mileage / 9000) * 9000
#     routine15000 = round(mileage / 15000) * 15000
#     routine18000 = round(mileage / 18000) * 18000

#     # Diccionario para almacenar la rutina y la diferencia
#     routines = {
#         1: (routine1500, mileage - routine1500),
#         2: (routine4500, mileage - routine4500),
#         3: (routine9000, mileage - routine9000),
#         4: (routine15000, mileage - routine15000),
#         5: (routine18000, mileage - routine18000)
#     }
# Realizando segunda prueba
#     # Iterar sobre cada rutina y su diferencia
#     for routine, (closest_routine, difference) in routines.items():
#         # Verificar si está dentro de 150 km antes de la rutina
#         if 0 < abs(difference) <= 150 and difference < 0:
#             return routine, f"Estás a {abs(difference)} km cerca de la Rutina {routine} de {closest_routine} km."
        
#         # Verificar si está hasta 150 km por encima de la rutina
#         elif 0 < abs(difference) <= 150 and difference > 0:
#             return routine, f"Estás a {difference} km por encima de la Rutina {routine} de {closest_routine} km."

#     # Si no está ni cerca ni por encima de 150 km de ninguna rutina
#     return "No hay rutinas cercanas dentro de ±150 km."

# def create_routine(c, a, lub, v, l, custom_values=None):   

#     routine = {
#         'Filtro combustible': c,
#         'Guayas del acelerador, embrague y freno': f"{a} y {lub}",
#         'Filtro aire': l,
#         'Bujia': v,
#         'Calibracion valvulas': None,
#         'Aceite motor': c,
#         'Carburador': None,
#         'Kit arrastre': f"{a} y {lub}",
#         'Freno delantero (pastas/Bandas)': f"{v}, {a} y {lub}",
#         'Freno trasero (pastas/Bandas)': f"{v}, {a} y {lub}",
#         'Liquido de frenos': v,
#         'Disco embrague': None,
#         'Bateria': v,
#         'Soporte lateral': v,
#         'Suspension delantera': None,
#         'Suspension trasera': None,
#         'Sistema electrico general (incluye luces)': v,
#         'Tornillos y tuercas': a
#     }
    
#     if custom_values:
#         routine.update(custom_values)
    
#     return routine

# def create_alert(routine):
#     l = 'Limpiar'
#     v = 'Verificar'
#     lub = 'Lubricar'
#     c = 'Cambiar'
#     cal = 'Calibrar'
#     a = 'Ajustar'
    
#     match routine:
#         case 1:
#             routine = create_routine(c, a, lub, v, l)
#         case 2:
#             custom_values = {'Carburador': l}
#             routine = create_routine(c, a, lub, v, l, custom_values)
#         case 3:
#             custom_values = {'Bujia': c, 'Carburador': l, 'Liquido de frenos': c}
#             routine = create_routine(c, a, lub, v, l, custom_values)
#         case 4:
#             custom_values = {'Kit arrastre': c}
#             routine = create_routine(c, a, lub, v, l, custom_values)
#         case 5:
#             custom_values = {
#                 'Bujia': c,
#                 'Calibracion valvulas': a,
#                 'Carburador': l,
#                 'Kit arrastre': f"{a} y {l}",
#                 'Disco embrague': c,
#                 'Bateria': f"{v} y {c}",
#                 'Suspension delantera': f"{c} (aceite)"
#             }
#             routine = create_routine(c, a, lub, v, l, custom_values)
    
#     # Crear una lista para almacenar las alertas
#     alert_list = []
    
#     for item, action in routine.items():
#         if action:
#             alert_list.append(f"*{item}* ➡️ {action}")
    
#     # Unir las alertas en una sola línea separadas por punto y coma
#     result = ". ".join(alert_list)
    
#     return result

# # Ejemplo de uso
# mileage = 1650
# routine, chosen_routine = choose_routine(mileage)
# print(chosen_routine)

# process = create_alert(routine)

# print(process)

from datetime import datetime

# # Función para enviar mensaje de error por Whatsaap
# def send_text_1param(mobile, param1, param2, param3, param4, template):
#     import requests
#     import json

#     # def save_ws(info):
#     #     # Abrir log
#     #     with open("{log}", "a") as archivo:
#     #         archivo.write(f"{info}.\n")

#     client_phone = str(mobile)
#     client_phone = int(float(client_phone))
#     url = "https://qg3dp2.api.infobip.com/whatsapp/1/message/template"
#     payload = json.dumps(
#         {
#             "messages": [
#                 {
#                     "from": "593963166655",
#                     "to": client_phone,
#                     "messageId": template,
#                     "content": {
#                         "templateName": template,
#                         "templateData": {
#                             "body": {
#                                 "placeholders": [
#                                     "*" + str(param1) + "*",
#                                     "*" + str(param2) + "*",
#                                     "*" + str(param3) + "*",
#                                     str(param4),
#                                 ]
#                             },
#                         },
#                         "language": "es",
#                     },
#                     "callbackData": '{"parametro1":"' + str(param1) + '"}',
#                 }
#             ]
#         }
#     )
    
#     headers = {
#         "Authorization": "Basic c2F0cmFjazE6SW5mb2JpcCQkNDU2",
#         "Content-Type": "application/json",
#     }
    
#     response = requests.request("POST", url, headers=headers, data=payload)
#     print("Response text: {}".format(response.text))
#     print("Response status code: {}".format(response.status_code))

# Obtener la fecha de hoy
today_date = datetime.now()
# Formatear fecha en formato año-mes-día y string
today = today_date.strftime("%Y-%m-%d")

# send_text_1param('573226090775', today, routine, 'PRUEBASHC', process, 'rpa_pesv_notify_previous_routine')

# Función para enviar mensaje exitoso por Whatsaap
def send_text_3param(mobile, date_template, param1, param2, template):
    import requests
    import json

    def save_ws(info):
        # Abrir log
        with open("{log}", "a") as archivo:
            archivo.write(f"{info}.\n")

    client_phone = str(mobile)
    client_phone = int(float(client_phone))
    url = "https://qg3dp2.api.infobip.com/whatsapp/1/message/template"
    payload = json.dumps(
        {
            "messages": [
                {
                    "from": "593963166655",
                    "to": client_phone,
                    "messageId": template,
                    "content": {
                        "templateName": template,
                        "templateData": {
                            "body": {
                                "placeholders": [
                                    "*" + str(date_template) + "*",
                                    "*" + str(param1) + "*",
                                    "*" + str(param2) + "*",
                                ]
                            },
                        },
                        "language": "es",
                    },
                    "callbackData": '{"parametro1":"' + str(param1) + '"}',
                }
            ]
        }
    )
    headers = {
        "Authorization": "Basic c2F0cmFjazE6SW5mb2JpcCQkNDU2",
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    save_ws("Response text: {}".format(response.text))
    save_ws("Response status code: {}".format(response.status_code))

send_text_3param('573226090775', today, "'No se moviliza'", 'PRUEBASHC', 'rpa_pesv_notify_succesful_other_pesv')
