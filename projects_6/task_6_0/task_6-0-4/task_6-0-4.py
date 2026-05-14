import pandas as pd

df = pd.read_csv('wild_boars.csv')

file = open('mode_values.txt', 'w')

file.write(f"gender: {df['gender'].mode()[0]}\n")
file.write(f"age_years: {df['age_years'].mode()[0]}\n")
file.write(f"weight_kg: {df['weight_kg'].mode()[0]}\n")
file.write(f"length_cm: {df['length_cm'].mode()[0]}\n")
file.write(f"shoulder_height_cm: {df['shoulder_height_cm'].mode()[0]}\n")
file.write(f"tusk_length_cm: {df['tusk_length_cm'].mode()[0]}\n")
file.write(f"litter_size: {df['litter_size'].mode()[0]}\n")
file.write(f"health_score: {df['health_score'].mode()[0]}\n")
file.write(f"territory_ha: {df['territory_ha'].mode()[0]}\n")

file.close()

print("Файл создан")
