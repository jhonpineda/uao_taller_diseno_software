import string
import random


class VehiculoInfo:

    def __init__(self, brand, electric, catalogo_precio):
        self.brand = brand
        self.electric = electric
        self.catalogo_precio = catalogo_precio

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogo_precio

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehiculo:

    def __init__(self, id, placa_matricula, info):
        self.id = id
        self.placa_matricula = placa_matricula
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.placa_matricula}")
        self.info.print()


class VehiculoRegistro:

    def __init__(self):
        self.Vehiculo_info = {}
        self.add_Vehiculo_info("Tesla Model 3", True, 60000)
        self.add_Vehiculo_info("Volkswagen ID3", True, 35000)
        self.add_Vehiculo_info("BMW 5", False, 45000)
        self.add_Vehiculo_info("Tesla Model Y", True, 75000)

    def add_Vehiculo_info(self, brand, electric, catalogo_precio):
        self.Vehiculo_info[brand] = VehiculoInfo(brand, electric, catalogo_precio)

    def generate_Vehiculo_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_Vehiculo_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_Vehiculo(self, brand):
        id = self.generate_Vehiculo_id(12)
        placa_matricula = self.generate_Vehiculo_license(id)
        return Vehiculo(id, placa_matricula, self.Vehiculo_info[brand])


class Aplicacion:

    def register_Vehiculo(self, brand: string):
        # create a registry instance
        registry = VehiculoRegistro()

        Vehiculo = registry.create_Vehiculo(brand)

        # print out the Vehiculo information
        Vehiculo.print()


app = Aplicacion()
app.register_Vehiculo("Volkswagen ID3")