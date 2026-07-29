# Password Generator CLI

Простая консольная утилита для генерации безопасных случайных паролей. Вы можете задать нужную длину пароля и выбрать набор символов: только буквы, только цифры или смешанный режим.

## Запуск

Для генерации пароля используйте команду:
```bash
python password_generator.py --length 12 --mode mixed
```

Доступные режимы (`--mode`):
* `letters` — только буквы
* `numbers` — только цифры
* `mixed` — буквы и цифры

## Пример

```bash
$ python password_generator.py --length 16 --mode mixed
aB3kL9pQzR2mN5xT

$ python password_generator.py --length 8 --mode numbers
58291047
```

## Тесты

Для запуска автоматических тестов используйте:
```bash
python -m unittest discover -s. -p "test_password_generator.py" -v
```
