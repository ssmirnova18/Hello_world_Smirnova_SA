#!/bin/bash


for (( i=1; i<=10; i++ ))
do
    touch "test$i.txt"
    echo "Создан файл test$i.txt"
done


i=10
while [ $i -ge 1 ]
do
    rm "test$i.txt"
    echo "Удален файл test$i.txt"
    ((i--))
done
