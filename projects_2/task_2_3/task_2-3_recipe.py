# Запрос данных у пользователя
medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации (°C): ")

# Создание и запись файла
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{medium_name}\n")
    file.write(f"- Концентрация агара: {agar_concentration}%\n")
    file.write(f"- Температура стерилизации: {sterilization_temperature}°C\n")
    
# Сообщение об успешном создании файла
print("Файл 'recipe.txt' успешно сформирован!")    
