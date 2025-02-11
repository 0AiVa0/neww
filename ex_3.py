import tkinter as tk
from tkinter import messagebox

def on_button_click():
    text = entry.get()  # Получаем текст из поля ввода
    messagebox.showinfo("Сообщение", f"Вы ввели: {text}")  # Выводим сообщение

# Создаем основное окно
root = tk.Tk()
root.title("Отладка Tkinter")

# Поле ввода
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# Кнопка
button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack(pady=5)

# Запуск главного цикла Tkinter
root.mainloop()
