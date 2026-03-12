#!/bin/bash

echo -e "Файл\tA\tT\tG\tC"

for file in *.fasta; do
    [ -e "$file" ] || continue
    [ -s "$file" ] || continue

    sequence=$(grep -v '^>' "$file" | tr 'a-z' 'A-Z')

    a_count=$(echo "$sequence" | grep -o "A" | wc -l)
    t_count=$(echo "$sequence" | grep -o "T" | wc -l)
    g_count=$(echo "$sequence" | grep -o "G" | wc -l)
    c_count=$(echo "$sequence" | grep -o "C" | wc -l)

    echo -e "${file}\t${a_count}\t${t_count}\t${g_count}\t${c_count}"
done
