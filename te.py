class TeProducto:
    
    precios = {"300gr": 3000, "500gr":5000 }
    datosTe = {
        "té negro": {
            "tiempo_preparacion": 3,
            "recomendacion": "Se recomienda consumir al desayuno."
        },
        "té verde": {
            "tiempo_preparacion": 5,
            "recomendacion": "Se recomienda consumir al medio día."
        },
        "agua de hierbas": {
            "tiempo_preparacion": 6,
            "recomendacion": "Se recomienda consumir al atardecer."
        }
    }
    
    @staticmethod
    def tiempo_prep(sabor):
        if  sabor == 1:
            nombre= "té negro"
            tiempo= TeProducto.datosTe.get("té negro").get("tiempo_preparacion")
            recomendacion= TeProducto.datosTe.get("té negro").get("recomendacion")
        elif sabor == 2:
            nombre= "té verde"
            tiempo= TeProducto.datosTe.get("té verde").get("tiempo_preparacion")
            recomendacion= TeProducto.datosTe.get("té verde").get("recomendacion")
        elif sabor == 3:
            nombre = "agua de hierbas"
            tiempo= TeProducto.datosTe.get("agua de hierbas").get("tiempo_preparacion")
            recomendacion= TeProducto.datosTe.get("agua de hierbas").get("recomendacion")    
        return tiempo,recomendacion,nombre
    
    @staticmethod
    def obtener_precio(valor):
        if valor == 300:
            formato="300gr"
            p_var=TeProducto.precios.get("300gr")
        elif valor == 500:
            formato="500gr"
            p_var=TeProducto.precios.get("500gr")
        return p_var,formato
    
        


       