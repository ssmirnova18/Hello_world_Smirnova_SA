# 1. Получаем объем от пользователя
volume = float(input("Введите необходимый объем раствора (мл): "))

# 2. Расчеты
salt_mass = volume * 0.009
salt_mass = round(salt_mass, 2)
water_volume = volume

# 3. Открываем файл и записываем отчет
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 30 + "\n")
    file.write(f"Общий объем: {volume:.2f} мл\n")
    file.write(f"Масса соли: {salt_mass:.2f} г\n")
    file.write(f"Объем воды: {water_volume:.2f} мл\n")

print("Файл 'recipe.txt' успешно сформирован!")
