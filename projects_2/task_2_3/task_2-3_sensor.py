# Запрос данных
operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")

# Запись в файл в формате таблицы: ОПЕРАТОР [TAB] ЗНАЧЕНИЕ
with open("sensor_log.txt", "a", encoding="utf-8") as file:
    file.write(f"{operator_name}\t{pressure_value}\n")

# Сообщение об успешном сохранении
print("Данные успешно сохранены в sensor_log.txt")
