#sistema
import random
import string

#modelos
from backend.storage.models import Collection, Item, Item_type, Tag, Theme, Category

#funciones para generar datos aleatorios


#descripcion string aleatorio
def random_string(length=60):
 
    myList = ['Breve descripcion generada de forma aletatoria opcion:1','Breve descripcion generada de forma aletatoria opcion:2', 
              'Breve descripcion generada de forma aletatoria opcion:3','Breve descripcion generada de forma aletatoria opcion:4',
              'Breve descripcion generada de forma aletatoria opcion:5','Breve descripcion generada de forma aletatoria opcion:6']
    return u''.join(random.choice(myList))

def random_metadato(length=60):
 
    myList = ['metadato 1','metadato 2', 
              'metadato 3','metadato 4',
              'metadato 5','metadato 6']
    return u''.join(random.choice(myList))

def alphabet():

	#lista de letras
	listaletras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	#guardar en diccionario
	diccionario={"lista":listaletras
				}

	return diccionario
