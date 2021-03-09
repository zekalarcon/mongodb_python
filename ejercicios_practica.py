#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gmail.com"
__version__ = "1.1"

import json

import tinymongo as tm
import tinydb

# Bug: https://github.com/schapman1974/tinymongo/issues/58
class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage

db_name = 'secundaria'


def clear():
    conn = TinyMongoClient()
    db = conn[db_name]

    # Eliminar todos los documentos que existan en la coleccion estudiante
    db.alumno.remove({})

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('Completemos esta tablita!')
    # Llenar la coleccion "estudiante" con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto completado por mongo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia insert_one o insert_many.

    conn = TinyMongoClient()
    db = conn[db_name]

    estudiantes = [{"name":'MIKE', "age": 14, "grade":3, "tutor":'MARTIN'},
                   {"name":'RAMON', "age":16, "grade":5, "tutor":'SUSANA'},
                   {"name":'GABRIELA', "age":17, "grade":6, "tutor":'MARCELA'},
                   {"name":'JUAN', "age":19, "grade":6, "tutor":'MARCELA'},
                   {"name":'LAURA', "age":15, "grade":4, "tutor":'DIEGO'}]
    
    db.alumno.insert_many(estudiantes)

    conn.close()

def show():
    print('Comprovemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia find para imprimir en pantalla
    # todos los documentos de la DB
    # Queda a su criterio serializar o no el JSON "dumps"
    #  para imprimirlo en un formato más "agradable"

    
    conn = TinyMongoClient()
    db = conn[db_name]
    
    cursor = db.alumno.find()
    data = list(cursor)
    json_string = json.dumps(data, indent=4)
    print(json_string)
   
    conn.close()

def find_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia find para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes debe imprimir
    # en pantalla unicamente los siguiente campos por cada uno:
    # id / name / age

    conn = TinyMongoClient()
    db = conn[db_name]

    alumno = db.alumno.find_one({"grade": grade})
    print(f'ID: {alumno["_id"]}, NAME: {alumno["name"]}, AGE: {alumno["age"]}')

def insert(student):
    print('Nuevos ingresos!')
    # Utilizar la sentencia insert_one para ingresar nuevos estudiantes
    # a la secundaria

    # El parámetro student deberá ser un JSON el cual se inserta en la db

    conn = TinyMongoClient()
    db = conn[db_name]

    db.alumno.insert_one(student)

    conn.close()

def count(grade):
    print('Contar estudiantes')
    # Utilizar la sentencia find + count para contar
    # cuantos estudiantes pertenecen el grado "grade"

    conn = TinyMongoClient()
    db = conn[db_name]

    cantidad = db.alumno.find({"grade": grade}).count()

    print(f'Estudiantes grade {grade}: {cantidad}')


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Borrar la db
    clear()

    fill()
    show()

    grade = 6
    find_by_grade(grade)

    student = {"name":'NELSON', "age":11, "grade":1, "tutor":'EDNA'}
    insert(student)

    grade = 6
    count(grade)
