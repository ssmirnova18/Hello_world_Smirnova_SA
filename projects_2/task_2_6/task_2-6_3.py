donor = input("Введите группу крови донора (1, 2, 3, 4): ").strip()
recipient = input("Введите группу крови пациента (1, 2, 3, 4): ").strip()

if donor == "I" or donor == recipient:
    print("Переливание возможно.")
else:
    print("Переливание невозможно.")
