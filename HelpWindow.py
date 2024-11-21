import customtkinter as ctk


class HelpWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Справка")
        self.geometry("600x500")
        self.resizable(False, False)

        # Основной фрейм
        main_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Заголовок
        ctk.CTkLabel(
            main_frame,
            text="Для корректной работы программы:",
            font=("Arial", 14),
            anchor="center"
        ).grid(row=0, column=0, pady=(0, 10), padx=(100, 0))

        # Инструкция ввода
        input_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        input_frame.grid(row=1, column=0, sticky="w", padx=50, pady=(10, 20))

        ctk.CTkLabel(input_frame, text="Введите:",
                     font=("Arial", 14)).pack(anchor="w")
        ctk.CTkLabel(input_frame, text="1. Сумму кредита.",
                     font=("Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(input_frame, text="2. Процентную ставку (годовая, в процентах).", font=(
            "Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(input_frame, text="3. Срок кредита (в месяцах).",
                     font=("Arial", 12)).pack(anchor="w", pady=2)

        # Инструкция вывода
        output_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        output_frame.grid(row=2, column=0, sticky="w", padx=50)

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

        # Кнопка "Назад"
        back_button = ctk.CTkButton(
            main_frame,
            text="Назад",
            width=150,
            height=35,
            command=self.destroy,
        )
        back_button.grid(row=3, column=0, pady=30, padx=(100, 0))
