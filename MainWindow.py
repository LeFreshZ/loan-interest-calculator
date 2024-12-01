import customtkinter as ctk
import tkinter.messagebox as mb

from AboutAuthorWindow import AboutAuthorWindow
from AboutProgramWindow import AboutProgramWindow
from HelpWindow import HelpWindow
from LoanCalculator import LoanCalculator
from LoanOrigin import LoanOrigin


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
        self.CredSum_TB = ctk.CTkEntry(row1_frame)
        self.CredSum_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Фрейм для ввода процентной ставки
        row2_frame = ctk.CTkFrame(input_frame, fg_color=self.cget("bg"))
        row2_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row2_frame, text="Процентная ставка:",
                     width=160).pack(side="left", padx=5)
        self.Procent_TB = ctk.CTkEntry(row2_frame)
        self.Procent_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Фрейм для ввода срока кредита
        row3_frame = ctk.CTkFrame(input_frame, fg_color=self.cget("bg"))
        row3_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row3_frame, text="Срок кредита (в месяцах):",
                     width=160).pack(side="left", padx=5)
        self.Time_TB = ctk.CTkEntry(row3_frame, width=100)
        self.Time_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Кнопка расчета
        self.Calc_BTN = ctk.CTkButton(
            main_frame, text="Рассчитать", command=self.calculate, width=150)
        self.Calc_BTN.grid(row=1, column=0, pady=20, sticky="n")
        self.bind("<Return>", self.calculate)

        # Фрейм для отображения результатов расчета
        output_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        output_frame.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")

        # Фрейм для отображения ежемесячного платежа
        row4_frame = ctk.CTkFrame(output_frame, fg_color=self.cget("bg"))
        row4_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row4_frame, text="Ежемесячный платёж:",
                     width=160).pack(side="left", padx=5)
        self.ResMonth_TB = ctk.CTkEntry(row4_frame, state="disabled")
        self.ResMonth_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Фрейм для отображения общей суммы выплат
        row5_frame = ctk.CTkFrame(output_frame, fg_color=self.cget("bg"))
        row5_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row5_frame, text="Общая сумма выплат:",
                     width=160).pack(side="left", padx=5)
        self.ResSum_TB = ctk.CTkEntry(row5_frame, state="disabled")
        self.ResSum_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Фрейм для отображения переплаты
        row6_frame = ctk.CTkFrame(output_frame, fg_color=self.cget("bg"))
        row6_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(row6_frame, text="Переплата:",
                     width=160).pack(side="left", padx=5)
        self.OverPrice_TB = ctk.CTkEntry(row6_frame, state="disabled")
        self.OverPrice_TB.pack(side="left", fill="x", expand=True, padx=10)

        # Кнопка очистки полей
        self.Clear_BTN = ctk.CTkButton(
            main_frame, text="Очистить", command=self.clear_fields, width=150)
        self.Clear_BTN.grid(row=3, column=0, pady=20, sticky="n")

        # Боковая панель с кнопками
        side_panel = ctk.CTkFrame(self, fg_color=self.cget(
            "bg"), border_width=2, border_color="white")
        side_panel.grid(row=0, column=1, padx=20, pady=20, sticky="ns")
        side_panel.grid_rowconfigure(0, weight=1)
        # Этот фрейм содержит кнопки для перехода к дополнительной информации
        self.AboutAuthor_BTN = ctk.CTkButton(
            side_panel, text="Об авторе", width=120, command=self.about_author)
        self.AboutAuthor_BTN.pack(pady=(25, 5), padx=15)

        self.AboutProgram_BTN = ctk.CTkButton(
            side_panel, text="О программе", width=120, command=self.about_program)
        self.AboutProgram_BTN.pack(pady=5, padx=15)

        self.Help_BTN = ctk.CTkButton(
            side_panel, text="Помощь", width=120, command=self.help_info)
        self.Help_BTN.pack(pady=5, padx=15)

        # Кнопка "Выход"
        self.Exit_BTN = ctk.CTkButton(
            side_panel, text="Выход", width=120, command=self.destroy)
        self.Exit_BTN.pack(side="bottom", pady=20)

    def calculate(self, e=None) -> None:
        """
        Выполняет расчет кредита на основе введенных данных.
        Результаты (ежемесячный платеж, общая сумма выплат, переплата) выводятся в соответствующие поля.
        """
        try:
            res = LoanCalculator.calculate(
                LoanOrigin(self.CredSum_TB.get(), self.Procent_TB.get(), self.Time_TB.get()))
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
            return

        self.ResMonth_TB.configure(state="normal")
        self.ResMonth_TB.delete(0, "end")
        self.ResMonth_TB.insert(0, f"{res.get_monthly_payment():.2f}")
        self.ResMonth_TB.configure(state="disabled")

        self.ResSum_TB.configure(state="normal")
        self.ResSum_TB.delete(0, "end")
        self.ResSum_TB.insert(0, f"{res.get_total_payment():.2f}")
        self.ResSum_TB.configure(state="disabled")

        self.OverPrice_TB.configure(state="normal")
        self.OverPrice_TB.delete(0, "end")
        self.OverPrice_TB.insert(0, f"{res.get_overpayment():.2f}")
        self.OverPrice_TB.configure(state="disabled")

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
