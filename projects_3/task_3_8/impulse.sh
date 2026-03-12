#!/bin/bash


if [ $# -lt 2 ]; then
    echo "Ошибка: недостаточно входных данных."
    echo "Использование: ./impulse.sh <имя_гена> <уровень_экспрессии>"
    exit 1
fi


GENE=$1
EXPRESSION=$2


echo "Экспрессия гена $GENE составляет $EXPRESSION единиц"
