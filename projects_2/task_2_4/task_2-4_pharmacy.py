# Ввод данных
total_capsules = int(input("Введите общее количество произведенных капсул: "))
capsules_per_pack = int(input("Введите количество капсул в одной упаковке: "))

# Расчеты
full_packs = total_capsules // capsules_per_pack
remaining_capsules = total_capsules % capsules_per_pack

# Вывод отчета
print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок: {full_packs}")
print(f"Остаток капсул: {remaining_capsules}")
