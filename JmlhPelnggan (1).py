class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers

restaurant = Restaurant("RM Sederhana", "Masakan Padang")

print(f"Jumlah awal: {restaurant.number_served}")

restaurant.number_served = 10
print(f"Setelah diubah manual: {restaurant.number_served}")

restaurant.set_number_served(25)
print(f"Setelah set_number_served: {restaurant.number_served}")

restaurant.increment_number_served(15)
print(f"Setelah increment (total harian): {restaurant.number_served}")