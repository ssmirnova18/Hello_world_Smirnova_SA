#!/bin/bash


echo "Введите массу (кг):"
read WEIGHT

echo "Введите рост (метры):"
read HEIGHT


BMI=$(echo "$WEIGHT / ($HEIGHT * $HEIGHT)" | bc)


echo "Ваш индекс массы тела (BMI): $BMI"
