#modelos
from django.contrib.auth.models import User
from backend.storage.models import Collection, Item, Item_type, Tag, Theme, Category

#queries

#cantidad registros
def registros_totales():
	#consultas
	qs1 = Collection.objects.count()
	qs2 = Item.objects.count()
	qs3 = Item_type.objects.count()
	qs4 = Tag.objects.count()
	qs5 = Category.objects.count()
	qs6 = Theme.objects.count()
	qs7 = User.objects.count()
	
	#guardar en diccionario
	diccionario={"total_colecciones":qs1,
				 "total_items":qs2,
				 "total_tipos_items":qs3,
				 "total_tags":qs4,
				 "total_categorias":qs5,
				 "total_temas":qs6,
				 "total_usuarios":qs7,
				}

	return diccionario

#lista objetos
def lista_elementos():
	#consultas
	qs1 = Collection.objects.values('id','nombre')
	qs2 = Item.objects.values('id','nombre')
	qs3 = Item_type.objects.values('id','nombre')
	qs4 = Tag.objects.values('id','nombre')
	qs5 = Category.objects.values('id','nombre')
	qs6 = Theme.objects.values('id','nombre')
	
	#guardar en diccionario
	diccionario={"lista_colecciones":qs1,
				 "lista_items":qs2,
				 "lista_tipos_items":qs3,
				 "lista_tags":qs4,
				 "lista_categorias":qs5,
				 "lista_temas":qs6,
				}

	return diccionario


#lista string
def lista_elementosv2():
	#consultas
	qs1 = Collection.objects.values_list('id','nombre')
	qs2 = Item.objects.values_list('id','nombre')
	qs3 = Item_type.objects.values_list('id','nombre')
	qs4 = Tag.objects.values_list('id','nombre')
	qs5 = Category.objects.values_list('id','nombre')
	qs6 = Theme.objects.values_list('id','nombre')
	
	#guardar en diccionario
	diccionario={"lista_colecciones":qs1,
				 "lista_items":qs2,
				 "lista_tipos_items":qs3,
				 "lista_tags":qs4,
				 "lista_categorias":qs5,
				 "lista_temas":qs6,
				}

	return diccionario


#añadido recientemente
def recent_uploads():
#consultas
	qs1 = Item.objects.all().order_by('-publicado')[:8]
	qs2 = Collection.objects.all().order_by('-publicado')[:4]
	
	#guardar en diccionario
	diccionario={"ultimos":qs1,
				 "ultimos_c":qs2,

				}
	return diccionario
