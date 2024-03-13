from te import TeProducto

producto = TeProducto()
sabor = int(input("Ingrese el sabor de té (té negro = 1, té verde = 2, infusión de hierbas = 3): "))
cantidad= int(input("Ingresa la cantidad de material con valores enteros (300gr=300 y 500gr=500) : "))

tiempo_preparacion,recomendacion,nombre = producto.tiempo_prep(sabor)
precio,formato = producto.obtener_precio(cantidad)

print(f"Sabor del tipo de té  = {nombre}")
print(f"Formato : {formato}")
print(f"Precio : ${precio}")
print(f"Tiempo de preparación: {tiempo_preparacion} minutos")
print(f"Recomendación {recomendacion}")
        

        