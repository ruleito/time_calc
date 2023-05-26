import tkinter as tk
from datetime import datetime, timedelta

class TimeCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор времени")

        self.label1 = tk.Label(self.master, text="Введите время в формате чч-мм")
        self.label1.pack()

        self.entry1 = tk.Entry(self.master)
        self.entry1.pack()

        self.label2 = tk.Label(self.master, text="Введите количество часов и минут для добавления (в формате 0-13)")
        self.label2.pack()

        self.entry2 = tk.Entry(self.master)
        self.entry2.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

        self.calculate_button = tk.Button(self.master, text="Вычислить", command=self.calculate)
        self.calculate_button.pack()

    def calculate(self):
        time_str = self.entry1.get()
        delta_str = self.entry2.get()

        try:
            time = datetime.strptime(time_str, '%H-%M').time()
            if "-" in delta_str:
                delta_hours, delta_minutes = map(int, delta_str.split('-'))
                if delta_hours > 23 or delta_minutes > 59:
                    raise ValueError
                delta = timedelta(hours=delta_hours, minutes=delta_minutes)
            else:
                delta_minutes = int(delta_str)
                if delta_minutes > 59:
                    raise ValueError
                delta = timedelta(minutes=delta_minutes)

            new_time = (datetime.combine(datetime.min, time) + delta).time()

            self.result_label.config(text=f"Результат: {new_time.strftime('%H-%M')}")
        except ValueError:
            self.result_label.config(text="Ошибка: неверный формат времени")

root = tk.Tk()
app = TimeCalculator(root)
root.mainloop()
