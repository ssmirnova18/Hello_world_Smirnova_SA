reagent_name = input("Введите название нового реактива: ")
reagent_quantity = int(input("Введите количество (целое число): "))
report = (f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт.")

print(report)

f = open("C:/Users/Azerty/Documents/smirnova_sa/projects_2/task_2_2/inventory.txt", "w", encoding="utf-8")
print(report, file=f)
f.close()
