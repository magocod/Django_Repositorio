#commandos django
from django.core.management import BaseCommand

import os


#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):

	 
	help = "Eliminar directorios vacios"

	def handle(self, *args, **options):

		print("instrucciones")
		print("Escribir ruta en este caso media, si modifico la configuracion escriba la carpeta correcta")
		print("la limpieza de carpeta tomo como base el root del directorio del codigo fuente")
		ruta = input()

		buscar_carpetas(ruta) 


def buscar_carpetas(string): 
	global carpeta_elegida 
	carpeta_elegida = string
	comprobar_existencia(carpeta_elegida) 

	global paths 
	paths = [] 
	global dirs 
	dirs = [] 

	for dirpath, dirname, filename in os.walk(carpeta_elegida):
		paths.append(dirpath) 
		dirs.append(dirname) 

	print("nA continuacion, se borraran las carpetas vacias.nPresione ENTER para continuar")
	borrar_carpetas() 

def borrar_carpetas(): 
	counter = 0 
	paths.reverse() 

	print("nEliminando las carpetas vacias del directorio elegido.nPor favor, aguarde un momento.n")
	for path in paths: 
		try: 
			os.rmdir("%s" % (path)) 
			counter += 1 
		except: None 

	print("Carpetas vacias eliminadas") 
	print("Se han eliminado %d carpetas sobre un total de %dn" % (counter, len(dirs) - 1))

	print("Presione ENTER para terminar") 

	exit() 
	bool = False 

def comprobar_existencia(carpeta_elegida): 
	if os.path.isdir(carpeta_elegida) != True: 
		print("nNo se puede encontrar la direccion o ruta especificada.")
		print("Por favor intentelo de nuevo.")
		exit()  
	else: 
		print("Generando base de datos. Por favor espere.")

