from enum import Enum

class MyEnum(Enum):
    SMALL = 1000000000
    MEDIUM = 2000000000
    LARGE = 3000000000

class MyClass:
    FLOAT_CONST = 3.14  # Константа (float)

    def __init__(self, char_value, string_list, enum_value):
        self.char_value = char_value  # Переменная char (один символ)
        self.string_list = string_list  # Массив строк (список)
        self.enum_value = enum_value  # Переменная с Enum (long)

    def perform_operations(self):
        print(f"🔹 Исходные данные:")
        print(f"Переменная char: {self.char_value}")
        print(f"Константа float: {self.FLOAT_CONST}")
        print(f"Массив строк: {self.string_list}")
        print(f"Enum значение (long): {self.enum_value.name} = {self.enum_value.value}")

        # ✅ Допустимые операции
        print("\n🔹 Выполнение операций:")
        float_sum = self.FLOAT_CONST + 2.5  # Операция с float
        print(f"Сложение float: {self.FLOAT_CONST} + 2.5 = {float_sum}")

        new_string_list = self.string_list + ["новая строка"]  # Добавление в массив
        print(f"Массив после добавления: {new_string_list}")

        enum_mult = self.enum_value.value * 2  # Умножение Enum long
        print(f"Умножение Enum long: {self.enum_value.value} * 2 = {enum_mult}")
