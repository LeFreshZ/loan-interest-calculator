import customtkinter as ctk


class HelpWindow(ctk.CTkToplevel):
    """
    Окно справки, которое объясняет пользователю, как использовать программу.
    Содержит инструкции для ввода и вывода данных, а также действия, которые можно выполнить.
    """

    def __init__(self, master):
        """
        Инициализация окна справки.
        В этом окне отображаются инструкции по использованию программы.
        """
        super().__init__(master)
        self.title("Справка")  # Заголовок окна
        self.geometry("600x500")  # Размеры окна
        self.attributes('-topmost', True)
        self.resizable(False, False)  # Окно нельзя изменять по размеру

        # Основной фрейм, содержащий все элементы интерфейса окна
        main_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Заголовок окна, который сообщает о назначении окна
        ctk.CTkLabel(main_frame, text="Для корректной работы программы:", font=(
            "Arial", 14), anchor="center").grid(row=0, column=0, pady=(0, 10), padx=(100, 0))

        # Фрейм для инструкций по вводу данных
        input_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        input_frame.grid(row=1, column=0, sticky="w", padx=50, pady=(10, 20))

        # Инструкции по вводу данных: сумма кредита, процентная ставка и срок кредита
        ctk.CTkLabel(input_frame, text="Введите:",
                     font=("Arial", 14)).pack(anchor="w")
        ctk.CTkLabel(input_frame, text="1. Сумму кредита.",
                     font=("Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(input_frame, text="2. Процентную ставку (годовая, в процентах).", font=(
            "Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(input_frame, text="3. Срок кредита (в месяцах).",
                     font=("Arial", 12)).pack(anchor="w", pady=2)

        # Фрейм для инструкций по выводу данных
        output_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        output_frame.grid(row=2, column=0, sticky="w", padx=50)

        # Инструкции по выводу данных после нажатия кнопки "Рассчитать"
        ctk.CTkLabel(output_frame, text="Нажмите Рассчитать, чтобы получить:", font=(
            "Arial", 14)).pack(anchor="w", pady=(0, 5))
        ctk.CTkLabel(output_frame, text="1. Ежемесячный платёж — сумма для выплаты каждый месяц.", font=(
            "Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(output_frame, text="2. Общую сумму выплат — сумма всех выплат по кредиту.", font=(
            "Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(output_frame, text="3. Переплату — излишек, уплаченный по процентам.", font=(
            "Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(output_frame, text="Для сброса данных нажмите Очистить.", font=(
            "Arial", 12)).pack(anchor="w", pady=(30, 0))

        # Кнопка "Назад", которая закрывает окно справки
        ctk.CTkButton(main_frame, text="Назад", width=150, height=35,
                      command=self.destroy).grid(row=3, column=0, pady=30, padx=(100, 0))

        self.mainloop()
