import pandas as pd

df = pd.read_csv('wild_boars.csv')

file = open('percentile_values.txt', 'w')

q1 = df['weight_kg'].quantile(0.25)
q2 = df['weight_kg'].quantile(0.50)
q3 = df['weight_kg'].quantile(0.75)
p90 = df['weight_kg'].quantile(0.90)
p95 = df['weight_kg'].quantile(0.95)
iqr = q3 - q1

file.write("weight_kg:\n")
file.write(f"Percentile 25: {q1:.1f}\n")
file.write(f"Median 50: {q2:.1f}\n")
file.write(f"Percentile 75: {q3:.1f}\n")
file.write(f"Percentile 90: {p90:.1f}\n")
file.write(f"Percentile 95: {p95:.1f}\n")
file.write(f"Min: {df['weight_kg'].min():.1f}\n")
file.write(f"Max: {df['weight_kg'].max():.1f}\n")
file.write(f"IQR: {iqr:.1f}\n\n")

q1 = df['length_cm'].quantile(0.25)
q2 = df['length_cm'].quantile(0.50)
q3 = df['length_cm'].quantile(0.75)
p90 = df['length_cm'].quantile(0.90)
p95 = df['length_cm'].quantile(0.95)
iqr = q3 - q1

file.write("length_cm:\n")
file.write(f"Percentile 25: {q1:.1f}\n")
file.write(f"Median 50: {q2:.1f}\n")
file.write(f"Percentile 75: {q3:.1f}\n")
file.write(f"Percentile 90: {p90:.1f}\n")
file.write(f"Percentile 95: {p95:.1f}\n")
file.write(f"Min: {df['length_cm'].min():.1f}\n")
file.write(f"Max: {df['length_cm'].max():.1f}\n")
file.write(f"IQR: {iqr:.1f}\n\n")

q1 = df['shoulder_height_cm'].quantile(0.25)
q2 = df['shoulder_height_cm'].quantile(0.50)
q3 = df['shoulder_height_cm'].quantile(0.75)
p90 = df['shoulder_height_cm'].quantile(0.90)
p95 = df['shoulder_height_cm'].quantile(0.95)
iqr = q3 - q1

file.write("shoulder_height_cm:\n")
file.write(f"Percentile 25: {q1:.1f}\n")
file.write(f"Median 50: {q2:.1f}\n")
file.write(f"Percentile 75: {q3:.1f}\n")
file.write(f"Percentile 90: {p90:.1f}\n")
file.write(f"Percentile 95: {p95:.1f}\n")
file.write(f"Min: {df['shoulder_height_cm'].min():.1f}\n")
file.write(f"Max: {df['shoulder_height_cm'].max():.1f}\n")
file.write(f"IQR: {iqr:.1f}\n\n")

q1 = df['tusk_length_cm'].quantile(0.25)
q2 = df['tusk_length_cm'].quantile(0.50)
q3 = df['tusk_length_cm'].quantile(0.75)
p90 = df['tusk_length_cm'].quantile(0.90)
p95 = df['tusk_length_cm'].quantile(0.95)
iqr = q3 - q1

file.write("tusk_length_cm:\n")
file.write(f"Percentile 25: {q1:.1f}\n")
file.write(f"Median 50: {q2:.1f}\n")
file.write(f"Percentile 75: {q3:.1f}\n")
file.write(f"Percentile 90: {p90:.1f}\n")
file.write(f"Percentile 95: {p95:.1f}\n")
file.write(f"Min: {df['tusk_length_cm'].min():.1f}\n")
file.write(f"Max: {df['tusk_length_cm'].max():.1f}\n")
file.write(f"IQR: {iqr:.1f}\n\n")

q1 = df['age_years'].quantile(0.25)
q2 = df['age_years'].quantile(0.50)
q3 = df['age_years'].quantile(0.75)
p90 = df['age_years'].quantile(0.90)
p95 = df['age_years'].quantile(0.95)
iqr = q3 - q1

file.write("age_years:\n")
file.write(f"Percentile 25: {q1:.1f}\n")
file.write(f"Median 50: {q2:.1f}\n")
file.write(f"Percentile 75: {q3:.1f}\n")
file.write(f"Percentile 90: {p90:.1f}\n")
file.write(f"Percentile 95: {p95:.1f}\n")
file.write(f"Min: {df['age_years'].min():.1f}\n")
file.write(f"Max: {df['age_years'].max():.1f}\n")
file.write(f"IQR: {iqr:.1f}\n\n")

q1 = df['litter_size'].quantile(0.25)
q2 = df['litter_size'].quantile(0.50)
q3 = df['litter_size'].quantile(0.75)
p90 = df['litter_size'].quantile(0.90)
p95 = df['litter_size'].quantile(0.95)
iqr = q3 - q1

file.write("litter_size:\n")
file.write(f"Percentile 25: {q1:.1f}\n")
file.write(f"Median 50: {q2:.1f}\n")
file.write(f"Percentile 75: {q3:.1f}\n")
file.write(f"Percentile 90: {p90:.1f}\n")
file.write(f"Percentile 95: {p95:.1f}\n")
file.write(f"Min: {df['litter_size'].min():.1f}\n")
file.write(f"Max: {df['litter_size'].max():.1f}\n")
file.write(f"IQR: {iqr:.1f}\n\n")

q1 = df['health_score'].quantile(0.25)
q2 = df['health_score'].quantile(0.50)
q3 = df['health_score'].quantile(0.75)
p90 = df['health_score'].quantile(0.90)
p95 = df['health_score'].quantile(0.95)
iqr = q3 - q1

file.write("health_score:\n")
file.write(f"Percentile 25: {q1:.1f}\n")
file.write(f"Median 50: {q2:.1f}\n")
file.write(f"Percentile 75: {q3:.1f}\n")
file.write(f"Percentile 90: {p90:.1f}\n")
file.write(f"Percentile 95: {p95:.1f}\n")
file.write(f"Min: {df['health_score'].min():.1f}\n")
file.write(f"Max: {df['health_score'].max():.1f}\n")
file.write(f"IQR: {iqr:.1f}\n\n")

q1 = df['territory_ha'].quantile(0.25)
q2 = df['territory_ha'].quantile(0.50)
q3 = df['territory_ha'].quantile(0.75)
p90 = df['territory_ha'].quantile(0.90)
p95 = df['territory_ha'].quantile(0.95)
iqr = q3 - q1

file.write("territory_ha:\n")
file.write(f"Percentile 25: {q1:.1f}\n")
file.write(f"Median 50: {q2:.1f}\n")
file.write(f"Percentile 75: {q3:.1f}\n")
file.write(f"Percentile 90: {p90:.1f}\n")
file.write(f"Percentile 95: {p95:.1f}\n")
file.write(f"Min: {df['territory_ha'].min():.1f}\n")
file.write(f"Max: {df['territory_ha'].max():.1f}\n")
file.write(f"IQR: {iqr:.1f}\n\n")

file.close()

print("Файл создан")
