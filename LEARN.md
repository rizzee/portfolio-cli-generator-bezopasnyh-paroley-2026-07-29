# LEARN.md: CLI-генератор паролей

## 1. Что сделали
- CLI-утилита на Python для генерации паролей
- Поддержка 3 режимов: буквы/цифры/оба
- Парсинг аргументов через `argparse` 
- Тесты на длину и состав пароля (`unittest`)

## 2. Что разобрать
- Генерация случайных данных: `random.choices()`
- Формирование алфавита: `string.ascii_letters`, `string.digits`
- Структура unittest: `TestCase`, `assertEqual()`
- Аргументы CLI: `add_argument()`, `parse_args()`

## 3. Ссылки
- [random](https://docs.python.org/3/library/random.html)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [string](https://docs.python.org/3/library/string.html)
- [unittest](https://docs.python.org/3/library/unittest.html)

## 4. Вопросы
1. Как ограничить выбор символов только буквами?
2. Почему `random.choices()` лучше `random.sample()` для этой задачи?
3. Как проверить, что пароль содержит цифры в тестах?
4. Какие аргументы обязательны по умолчанию в argparse?
5. Как получить все латинские буквы одной строкой?
6. Какой метод unittest проверяет точное соответствие?
7. Зачем нужен параметр `k` в `random.choices()`?
