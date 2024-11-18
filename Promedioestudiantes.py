# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:45:04 2024

@author: josea
"""
estudiantes = []

def agregar_estudiante(nombre, calificacion):
    estudiantes.append({"nombre": nombre,
                        "Calificacion": calificacion})
def modificar_calificaciones(nombre, nueva_calificacion):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            estudiante["Calificacion"] = nueva_calificacion
            
def eliminar_estudiante(nombre):
    global estudiantes
    estudiantes = [e for e in estudiantes if e["nombre"] != nombre]
    
def mostrar_estudiantes():
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Calificacion: {estudiante['Calificacion']}")
        
def calcular_promedio():
    total_Calificaciones = sum(e["Calificacion"] for e in estudiantes)
    promedio = total_Calificaciones / len(estudiantes)
    print(f"calificaciones promedio = {promedio}")


agregar_estudiante("Putin", 10)
agregar_estudiante("Trump", 6)
agregar_estudiante("Peña", 3)
modificar_calificaciones("Peña", 7)
mostrar_estudiantes()
calcular_promedio()
eliminar_estudiante("Trump")
mostrar_estudiantes()
agregar_estudiante("Biden", 7)
calcular_promedio()
eliminar_estudiante("Peña")
mostrar_estudiantes()
agregar_estudiante("Amlo", 8)
calcular_promedio()
mostrar_estudiantes()
calcular_promedio()
