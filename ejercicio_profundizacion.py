__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gmail.com"

import json
import requests
import tinymongo as tm
import tinydb

# Bug: https://github.com/schapman1974/tinymongo/issues/58
class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage

db_name = 'users'

def clear():
    conn = TinyMongoClient()
    db = conn[db_name]

    db.user.remove({})

    conn.close()


def fill():

    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    data = response.json()

    conn = TinyMongoClient()
    db = conn[db_name]

    db.user.insert_many(data)

    conn.close()


def title_completed_count(userId): 

    conn = TinyMongoClient()
    db = conn[db_name]

    cantidad = db.user.find({"userId": userId, "completed":True}).count()

    print(f'{cantidad} Usuarios con userId {userId} completaron su titulo')

    conn.close()


if __name__ == "__main__":
  #clear()

  #fill()

  # Buscar title completed por userdId
  userId = 1
  title_completed_count(userId)