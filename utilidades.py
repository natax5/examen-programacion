import csv
import random

def agregarempleados(empleados):

nombres=input("ingrese el nombre del trabajador: ")
apellido=input("ingrese el apellido: ")
sueldo=round (random.uniform(300000,2500000)10)
empleados={'nombres':nombres,'apellido':apellido,'sueldo':sueldo}
empleados.append(empleados)
print(f"empleado{empleados} su sueldo es: {sueldo}")


def guardar_empleados_csv(empleados, filename='empleados.csv'):
    if empleados:
        keys = empleados[0].keys()
        with open(filename,'w', newline=) as output_file:
        dict_writer=csv.DictWriter(output,fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(empleados)
        print(f"empleados guardados en el archivo {filename}")
    else:
        print("no hay productos para guardar" )

