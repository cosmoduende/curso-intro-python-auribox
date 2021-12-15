
class Restaurant:
    
    def agregar_restaurant(self, nombre):  # self es un atributo que pasa automáticamente
        print("Agregando...")
        self.nombre = nombre # Atributo
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")

# Instanciar la clase // objeto = Clase

restaurant = Restaurant()
print(restaurant)

restaurant.agregar_restaurant("Pizzería México")
restaurant.mostrar_informacion()

# segunda instancia de Clase

restaurant2 = Restaurant()
print(restaurant2)

restaurant2.agregar_restaurant("Hamburguesa Python")
restaurant2.mostrar_informacion()

# Otra manera de mostrar la información

print(f"Nombre del restaurant: {restaurant.nombre}")
print(f"Nombre del restaurant: {restaurant2.nombre}")