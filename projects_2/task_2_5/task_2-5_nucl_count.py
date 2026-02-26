print("=== Анализ последовательности ДНК ===\n")
dna = input("Введите последовательность ДНК: ").upper()
print(f"\nПоследовательность в верхнем регистре: {dna}\n")

# Подсчет нуклеотидов через str.count()
count_a = dna.count("A")
count_t = dna.count("T")
count_g = dna.count("G")
count_c = dna.count("C")

total_len = len(dna)

print("Подсчёт нуклеотидов:")
print(f"A: {count_a}")
print(f"T: {count_t}")
print(f"G: {count_g}")
print(f"C: {count_c}\n")

print(f"Общая длина: {total_len} нуклеотидов\n")

# Проценты 
if total_len == 0:
    a_percent = t_percent = g_percent = c_percent = 0
else:
    a_percent = (count_a / total_len) * 100
    t_percent = (count_t / total_len) * 100
    g_percent = (count_g / total_len) * 100
    c_percent = (count_c / total_len) * 100

print("Процентное содержание:")
print(f"A: {a_percent:.2f}%")
print(f"T: {t_percent:.2f}%")
print(f"G: {g_percent:.2f}%")
print(f"C: {c_percent:.2f}%")
