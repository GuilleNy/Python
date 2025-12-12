**Iterar sobre múltiples listas**



compra = \['Agua', 'Aceite', 'Arroz']

detalles = \['mineral natural', 'de oliva virgen', 'basmati']



***for***<i> producto, detalle **in** zip(compra, detalles):</i>

<i>	print(producto, detalle)</i>



\#Salida

Agua mineral natural

Aceite de oliva virgen

Arroz basmati





**Pertenencia de una objeto a una lista**



lista = \['banana', 'orange', 'mango', 'lemon']



&nbsp;	*if 'banana' in lista:*

		*print('Si, banana está en la lista!')*

	*else:*

		*print('No, banana no está en la lista!')*



<b>Ordenar una lista</b>

*El método sort() ordena la lista y modifica su contenido*

*lista = \['banana', 'orange', 'mango', 'lemon']*

*lista.sort()*

*print (lista)*



*#Salida*

*\['banana', 'lemon', 'mango', 'orange']*



*La función sorted retorna una nueva la lista ordenada pero no modificará la lista original.*

*lista = \['banana', 'orange', 'mango', 'lemon']*

*lista\_ordenada=sorted(lista)*

