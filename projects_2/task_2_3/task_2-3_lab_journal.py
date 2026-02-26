# Сбор данных
researcher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату (дд.мм.гггг): ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

# Ширина рамки
width = 60

# Формирование рамки
top_border = "+" + "-" * (width - 2) + "+"
empty_line = "|" + " " * (width - 2) + "|"

# Формирование текста внутри рамки
title = f"| {'Электронный лабораторный журнал':^{width - 2}} |"
line1 = f"| ФИО исследователя : {researcher_name:<33}|"
line2 = f"| Дата              : {experiment_date:<33}|"
line3 = f"| Эксперимент       : {experiment_name:<33}|"

# Блок вывода (разбиваем длинный текст вручную)
conclusion_title = f"| {'Вывод:':<58}|"
conclusion_text = f"| {conclusion:<58}|"

# Запись в файл
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(top_border + "\n")
    file.write(title + "\n")
    file.write(top_border + "\n")
    file.write(line1 + "\n")
    file.write(line2 + "\n")
    file.write(line3 + "\n")
    file.write(top_border + "\n")
    file.write(conclusion_title + "\n")
    file.write(conclusion_text + "\n")
    file.write(top_border + "\n")

print("Файл 'journal.txt' успешно сформирован!")
