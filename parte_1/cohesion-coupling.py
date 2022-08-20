import string
import random

class RegistroVehiculo:

    def generar_vehiculo_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generar_licencia_vehiculo(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Aplicacion:

    def registrar_vehiculo(self, brand: string):
        # create a registry instance
        registro = RegistroVehiculo()

        # generate a vehicle id of length 12
        vehiculo_id = registro.generar_vehiculo_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        placa_matricula = registro.generar_licencia_vehiculo(vehiculo_id)

        # compute the catalogue price
        catalogo_precio = 0
        if brand == "Tesla Model 3":
            catalogo_precio = 60000
        elif brand == "Volkswagen ID3":
            catalogo_precio = 35000
        elif brand == "BMW 5":
            catalogo_precio = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogo_precio

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehiculo_id}")
        print(f"License plate: {placa_matricula}")
        print(f"Payable tax: {payable_tax}")

app = Aplicacion()
app.registrar_vehiculo("Volkswagen ID3")