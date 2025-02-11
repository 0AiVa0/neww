import tkinter as tk
# Функция для вывода всех свойств Label
def show_label_properties():
    root = tk.Tk()
    label = tk.Label(root, text="Пример текста", font=("Arial", 12), bg="white", fg="black")

    print("🔹 СВОЙСТВА Label:")
    for key in label.configure():
        print(f"{key}: {label[key]}")

    root.mainloop()


# Функция для вывода списка событий Label
def show_label_events():
    def show_event(event):
        print(f"Событие: {event}")

    root = tk.Tk()
    label = tk.Label(root, text="Наведите и кликните!", font=("Arial", 14), bg="white")
    label.pack(pady=10)

    # Привязываем основные события
    label.bind("<Button-1>", show_event)  # ЛКМ
    label.bind("<Double-Button-1>", show_event)  # Двойной клик ЛКМ
    label.bind("<Enter>", show_event)  # Наведение курсора
    label.bind("<Leave>", show_event)  # Уход курсора
    label.bind("<Motion>", show_event)  # Движение мыши
    label.bind("<KeyPress>", show_event)  # Нажатие клавиши

    print("🔹 СОБЫТИЯ Label:")
    print("<Button-1> - Клик левой кнопкой")
    print("<Button-2> - Клик средней кнопкой")
    print("<Button-3> - Клик правой кнопкой")
    print("<Double-Button-1> - Двойной клик")
    print("<Enter> - Наведение курсора")
    print("<Leave> - Уход курсора")
    print("<Motion> - Движение мыши")
    print("<KeyPress> - Нажатие клавиши")

    root.mainloop()


# Функция для вывода методов Label
def show_label_methods():
    root = tk.Tk()
    label = tk.Label(root, text="Пример текста")
    print("🔹 МЕТОДЫ Label:")
    print(dir(label))  # Вывод всех доступных методов
    root.mainloop()


# Запускаем функции
show_label_properties()
show_label_events()
show_label_methods()
