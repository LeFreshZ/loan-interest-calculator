import customtkinter as ctk
import tkinter.messagebox as mb

from AboutAuthorWindow import AboutAuthorWindow
from AboutProgramWindow import AboutProgramWindow
from FileOperator import FileOperator
from HelpWindow import HelpWindow
from LoanCalculator import LoanCalculator
from LoanOrigin import LoanOrigin
from LoanResult import LoanResult


class MainWindow(ctk.CTk):
    """
    Главное окно приложения, которое предоставляет интерфейс для расчета кредита.
    Включает поля ввода данных, результаты расчетов и панель с дополнительной информацией.
    """

    def __init__(self):
        """
        Инициализация главного окна. Настроены все элементы управления, такие как:
        поля ввода для суммы кредита, процентной ставки и срока кредита,
        кнопки для расчета и очистки, а также фреймы для вывода результатов.
        """
        super().__init__()

        # Настройки окна
        self.title("MainScreen")  # Заголовок окна
        self.geometry("650x500")  # Размеры окна
        self.resizable(False, False)  # Отключаем изменение размера окна

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)

        # Основной фрейм для ввода и вывода
        main_frame = ctk.CTkFrame(self, fg_color=self.cget(
            "bg"), border_width=2, border_color="white")
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)

        # Фрейм для ввода данных
        input_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        input_frame.grid(row=0, column=0, pady=20, padx=20, sticky="nsew")

        # Фрейм для ввода суммы кредита
        row1_frame = ctk.CTkFrame(input_frame, fg_color=self.cget("bg"))
        row1_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row1_frame, text="Сумма кредита:",
                     width=160).pack(side="left", padx=5)
        self.credSum_TB = ctk.CTkEntry(row1_frame)
        self.credSum_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Фрейм для ввода процентной ставки
        row2_frame = ctk.CTkFrame(input_frame, fg_color=self.cget("bg"))
        row2_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row2_frame, text="Процентная ставка:",
                     width=160).pack(side="left", padx=5)
        self.procent_TB = ctk.CTkEntry(row2_frame)
        self.procent_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Фрейм для ввода срока кредита
        row3_frame = ctk.CTkFrame(input_frame, fg_color=self.cget("bg"))
        row3_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row3_frame, text="Срок кредита (в месяцах):",
                     width=160).pack(side="left", padx=5)
        self.time_TB = ctk.CTkEntry(row3_frame, width=100)
        self.time_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Кнопка расчета
        ctk.CTkButton(
            main_frame, text="Рассчитать", command=self.calculate, width=150).grid(row=1, column=0, pady=20, sticky="n")
        self.bind("<Return>", self.calculate)

        # Фрейм для отображения результатов расчета
        output_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        output_frame.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")

        # Фрейм для отображения ежемесячного платежа
        row4_frame = ctk.CTkFrame(output_frame, fg_color=self.cget("bg"))
        row4_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row4_frame, text="Ежемесячный платёж:",
                     width=160).pack(side="left", padx=5)
        self.resMonth_TB = ctk.CTkEntry(row4_frame, state="disabled")
        self.resMonth_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Фрейм для отображения общей суммы выплат
        row5_frame = ctk.CTkFrame(output_frame, fg_color=self.cget("bg"))
        row5_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row5_frame, text="Общая сумма выплат:",
                     width=160).pack(side="left", padx=5)
        self.resSum_TB = ctk.CTkEntry(row5_frame, state="disabled")
        self.resSum_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Фрейм для отображения переплаты
        row6_frame = ctk.CTkFrame(output_frame, fg_color=self.cget("bg"))
        row6_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row6_frame, text="Переплата:",
                     width=160).pack(side="left", padx=5)
        self.overPrice_TB = ctk.CTkEntry(row6_frame, state="disabled")
        self.overPrice_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Кнопка очистки полей
        ctk.CTkButton(
            main_frame, text="Очистить", command=self.clear_fields, width=150).grid(row=3, column=0, pady=20, sticky="n")

        # Боковая панель с кнопками
        side_panel = ctk.CTkFrame(self, fg_color=self.cget(
            "bg"), border_width=2, border_color="white")
        side_panel.grid(row=0, column=1, padx=20, pady=20, sticky="ns")
        side_panel.grid_rowconfigure(0, weight=1)
        # Этот фрейм содержит кнопки для перехода к дополнительной информации
        ctk.CTkButton(
            side_panel, text="Об авторе", width=120, command=self.about_author).pack(pady=(25, 5), padx=15)

        ctk.CTkButton(
            side_panel, text="О программе", width=120, command=self.about_program).pack(pady=5, padx=15)

        ctk.CTkButton(
            side_panel, text="Помощь", width=120, command=self.help_info).pack(pady=5, padx=15)

        # Кнопка "Выход"
        ctk.CTkButton(
            side_panel, text="Выход", width=120, command=self.destroy).pack(side="bottom", pady=(0, 20))

        ctk.CTkButton(
            side_panel, text="Сохранить", command=self.save, width=120).pack(side="bottom", pady=(0, 10))

        self.mainloop()
        
    def save(self) -> None:
        """
        Сохраняет результат в файл
        """
        try:
            origin = LoanOrigin(self.credSum_TB.get(), self.procent_TB.get(), self.time_TB.get())
            result = LoanResult(float(self.resMonth_TB.get()), float(self.resSum_TB.get()), float(self.overPrice_TB.get()))
        
            FileOperator.save_to_file(origin, result)
        except Exception as e:
            mb.showerror("Ошибка", "Ошибка записи в файл")
            

    def calculate(self, e=None) -> None:
        """
        Выполняет расчет кредита на основе введенных данных.
        Результаты (ежемесячный платеж, общая сумма выплат, переплата) выводятся в соответствующие поля.
        """
        try:
            res = LoanCalculator.calculate(
                LoanOrigin(self.credSum_TB.get(), self.procent_TB.get(), self.time_TB.get()))
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
            return

        self.resMonth_TB.configure(state="normal")
        self.resMonth_TB.delete(0, "end")
        self.resMonth_TB.insert(0, f"{res.get_monthly_payment():.2f}")
        self.resMonth_TB.configure(state="disabled")

        self.resSum_TB.configure(state="normal")
        self.resSum_TB.delete(0, "end")
        self.resSum_TB.insert(0, f"{res.get_total_payment():.2f}")
        self.resSum_TB.configure(state="disabled")

        self.overPrice_TB.configure(state="normal")
        self.overPrice_TB.delete(0, "end")
        self.overPrice_TB.insert(0, f"{res.get_overpayment():.2f}")
        self.overPrice_TB.configure(state="disabled")

    def about_author(self) -> None:
        """
        Открывает окно с информацией об авторе программы.
        """
        AboutAuthorWindow(self)

    def about_program(self) -> None:
        """
        Открывает окно с информацией о программе.
        """
        AboutProgramWindow(self)

    def help_info(self) -> None:
        """
        Открывает окно с информацией о том, как использовать программу.
        """
        HelpWindow(self)

    def clear_fields(self) -> None:
        """
        Очищает все поля ввода и результатов, возвращая их в исходное состояние.
        """
        for field_name in ["CredSum_TB", "Procent_TB", "Time_TB", "ResMonth_TB", "ResSum_TB", "OverPrice_TB"]:
            field = getattr(self, field_name)
            field.configure(state="normal")
            field.delete(0, "end")
            if field_name in ["ResMonth_TB", "ResSum_TB", "OverPrice_TB"]:
                field.configure(state="disabled")
