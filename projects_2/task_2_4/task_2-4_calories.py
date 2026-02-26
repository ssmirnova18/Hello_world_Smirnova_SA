# Запрос данных
proteins = float(input("Введите массу белков (г): "))
fats = float(input("Введите массу жиров (г): "))
carbohydrates = float(input("Введите массу углеводов (г): "))

# Расчет калорийности
calories = (proteins * 4) + (fats * 9) + (carbohydrates * 4)

# Вывод результата
print(f"Общая калорийность продукта: {calories} ккал")
