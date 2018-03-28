#ejecutadas en shell de django y test

#fabricas de modelos

#parametros cantidad de modelos a ingresar
class seederv2():

	def help():
		print("cantidad a agregar")
		print("seed_1=(temas, tipos de items)")
		print("seed_2=(tags, items, colecciones, categorias)")

	#metodos

	#enviar parametros t=temas, ti=tipos
	def seed_1(t,ti):
		#factories
		from backend.fabricator.factories import Themefactory, Item_typefactory

		Themefactory.create_batch(size=t)
		Item_typefactory.create_batch(size=ti)

		print("agregados los modelos")

	#enviar parametros t=tags, i=items, cl=colecciones, ct=categorias
	def seed_2(t,i,cl,ct):
		#factories
		from backend.fabricator.factories import Collectionfactory, Categoryfactory, Tagfactory, Itemfactory

		#agregar tags
		tag = Tagfactory.create_batch(size=t)

		#agregar categorias
		list_categories = Categoryfactory.create_batch(size=ct)

		#agregar colecciones
		list_collection = Collectionfactory.create_batch(size=cl, categorias=list_categories)

		#agregar items
		Itemfactory.create_batch(i, tags=tag, colecciones=list_collection)

		
		
		print("agregados los modelos")

		
#llamar desde el shell (from backend.fabricator.seeders import seederv2)