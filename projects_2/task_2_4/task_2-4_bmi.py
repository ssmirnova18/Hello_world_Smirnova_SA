# Ввод данных
weight = float(input("Введите ваш вес (кг): "))
height_cm = float(input("Введите ваш рост (см): "))

# Перевод роста в метры
height_m = height_cm / 100

# Расчет ИМТ
bmi = weight / (height_m ** 2)

# Вывод отчета с использованием \t
print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height_cm} см")
print(f"Вес:\t{weight} кг")
print(f"Индекс массы тела:\t{bmi:.2f}")
