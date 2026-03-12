
#!/bin/bash

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "Ошибка: скрипт должен быть запущен от суперпользователя (root)."
        exit 1
    fi
}

check_root

echo "Скрипт запущен с правами root."
