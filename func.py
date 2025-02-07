count = 0
notes = []

with open("notes.txt", "r", encoding="utf-8") as start:
    strings = start.read().strip()  # Читаем файл и убираем лишние пробелы/переводы строк
    old_strings = strings.split("---\n") if strings else []  # Разделяем заметки по "---"

    for old_string in old_strings:
        lines = old_string.strip().split("\n")  # Разбиваем заметку на строки
        if len(lines) > 1 and lines[0].isdigit():  # Проверяем, есть ли ID в первой строке
            notes.append(old_string)  # Добавляем заметку в список
            count = int(lines[0])  # Устанавливаем счетчик на последний ID

def add_note(title, note):
    global count
    count += 1  
    with open("notes.txt", "a+", encoding="utf-8") as f:
        f.write(f"---\n{count}\n{title}\n{note}\n---\n")
    notes.append(f"---\n{count}\n{title}\n{note}\n---\n")
    print(f"Заметка номер {count} добавлена. Всего вы имеете {len(notes)} заметок")


# Запрашиваю у юзера название и текст

def del_note(id_to_delete):
    global count, notes
    
    id_to_delete = int(id_to_delete)
    
    # Создаем новый список заметок без удалённой
    new_notes = []
    for note in notes:
        lines = note.strip().split("\n")
        if len(lines) > 1 and lines[0].isdigit():
            if int(lines[0]) == id_to_delete:
                print(f"Удаляем заметку {id_to_delete}")
                continue  # Пропускаем удалённую заметку
        new_notes.append(lines)  # Добавляем остальные заметки как список строк
    
    # Перенумеровываем ID заново
    for index, note_lines in enumerate(new_notes):
        note_lines[0] = str(index + 1)  # Первый элемент (ID) заменяем на новый
    
    # Перезаписываем файл
    with open("notes.txt", "w", encoding="utf-8") as f:
        for note_lines in new_notes:
            f.write("---\n" + "\n".join(note_lines) + "\n---\n")
    
    # Обновляем список notes
    notes = ["---\n" + "\n".join(note) + "\n---\n" for note in new_notes]

    # Обновляем счетчик ID
    count = len(new_notes)

    print(f"Заметка {id_to_delete} удалена. Теперь у вас {count} заметок.")


while True:
    action = input("Для добавления заметки введите 'add', для удаления заметки введите 'delete', для выхода введите 'exit': ")
    if action == "add":
        add_note(
                     title = input("Введите название заметки: "),  # str() можно не писать, input и так возвращает строку
                     note = input("Введите текст заметки: ")
         )
    elif action == "delete":
        del_note(
            id_to_delete = input("Введите номер заметки: ")
        )
    elif action == "exit":
        break
    else:
        print("Ошибка: Неправильное действие. Введите 'add', 'delete' или 'exit'.")