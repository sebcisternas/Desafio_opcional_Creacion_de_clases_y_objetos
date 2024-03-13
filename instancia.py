from te import TeProducto

producto1=TeProducto()
producto2=TeProducto()

var_prod1=type(producto1)
var_prod2=type(producto2)

if var_prod1==var_prod2 :
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")