files = ["seq1", "seq2", "seq3", "seq4"]
sample_date = int(input("Введите точную дату через нижний пробел")) 

for name in files:
    new_name = name + "_" + sample_date + ".fasta"
    print(new_name)
