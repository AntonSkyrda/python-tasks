class Device:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def __str__(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}"

    @classmethod
    def self_name(cls) -> str:
        return f"My name is {cls.__name__}"


class CalculateMixin:
    @staticmethod
    def calculate(x: int, y: int) -> int:
        return x + y


class Phone(CalculateMixin, Device):
    contacts = {}

    def __init__(self, brand: str, model: str, phone_type: str) -> None:
        super().__init__(brand, model)
        self.phone_type = phone_type

    def __str__(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}, Type: {self.phone_type}"

    def ring(self, ring_to) -> None:
        try:
            print(f"Ringing to {self.contacts[ring_to]} from phone {self.model}")
        except KeyError:
            print(f"Contact {ring_to} does not exist!")


class Laptop(CalculateMixin, Device):
    def __init__(self, brand: str, model: str, storage_type: str = "HDD") -> None:
        super().__init__(brand, model)
        self.storage_type = storage_type

    def __str__(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}, Storage Type: {self.storage_type}"

    def play(self) -> None:
        print(f"Playing on {self.brand} {self.model}")

    def work(self) -> None:
        print(f"Working on {self.brand} {self.model}")


device1 = Device("Ford", "Model1")
# print(device1.brand)
# print(device1.model)
# print(device1)
#
device2 = Phone("Samsung", "Model2", "button")
# print(device2)
#
device3 = Laptop("Lenovo", "Legion")
# print(device3)
#
# device3.work()
# device2.contacts["DEN"] = 12432432432
# device2.ring("DEN1")
#
# string = "qwer"
# print(device1.self_name())
# print(device2.self_name())
# print(device3.self_name())
phone1 = Phone("Samsung", "qweer", "qerewr")
phone2 = Phone("IPhone", "dfsfds", "fsdfsdfsd")
# print(phone1.self_name(), "----", phone1)
# print(phone2.self_name(), "----", phone2)
print(device2.calculate(1, 4))
print(device3.calculate(5, 6))
