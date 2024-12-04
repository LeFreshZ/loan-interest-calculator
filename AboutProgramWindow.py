import customtkinter as ctk
from PIL import Image


class AboutProgramWindow(ctk.CTkToplevel):
    """
    Окно, которое предоставляет информацию о программе. 
    Содержит описание программы, её функции, а также формулы, используемые для расчетов.
    """

    def __init__(self, master):
        """
        Инициализация окна "О программе".
        В окне отображается информация о назначении программы, её возможностях и формулах расчета.
        """
        super().__init__(master)
        self.title("О программе")  # Заголовок окна
        self.geometry("750x550")  # Размеры окна
        self.attributes('-topmost', True)
        self.resizable(False, False)  # Окно нельзя изменять по размеру

        # Загружаем изображение, которое будет отображаться в окне
        self.image = ctk.CTkImage(Image.open(
            "./Images/AboutProgram.png"), size=(175, 175))

        # Основной фрейм, который содержит все элементы интерфейса окна
        main_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Заголовок окна, который объясняет назначение программы
        ctk.CTkLabel(main_frame, text="Данная программа предназначена для расчёта аннуитетных платежей по кредиту.", font=(
            "Arial", 14)).grid(row=0, column=0, columnspan=2, pady=(0, 20), padx=45)

        # Изображение, которое будет отображаться в окне
        ctk.CTkLabel(main_frame, image=self.image, text="").grid(
            row=1, column=0, pady=20, padx=80)

        # Фрейм, который содержит описание программы и её функционала
        description_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        description_frame.grid(row=1, column=1, sticky="e")

        # Описание, объясняющее функции программы и используемые формулы
        ctk.CTkLabel(description_frame, text="Программа позволяет:",
                     font=("Arial", 12)).pack(anchor="w", pady=(0, 5))
        ctk.CTkLabel(description_frame, text="1. Рассчитать сумму ежемесячного платежа.", font=(
            "Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(description_frame, text="Коэффициент аннуитета:",
                     font=("Arial", 12)).pack(anchor="w")
        ctk.CTkLabel(description_frame, text="A = P * (1 + P)^N / ((1 + P)^N - 1), где",
                     font=("Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(description_frame, text="A — коэффициент аннуитета; P — процентная ставка (в долях);", font=(
            "Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(description_frame, text="N — число периодов.",
                     font=("Arial", 12)).pack(anchor="w", pady=2)

        ctk.CTkLabel(description_frame, text="2. Определить общую сумму выплат.", font=(
            "Arial", 12)).pack(anchor="w", pady=(10, 2))
        ctk.CTkLabel(description_frame, text="S = N * A * K, где",
                     font=("Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(description_frame, text="K — сумма кредита.",
                     font=("Arial", 12)).pack(anchor="w", pady=2)

        ctk.CTkLabel(description_frame, text="3. Узнать переплату по кредиту.", font=(
            "Arial", 12)).pack(anchor="w", pady=(10, 2))
        ctk.CTkLabel(description_frame, text="Sp = (N * A - 1) * K",
                     font=("Arial", 12)).pack(anchor="w", pady=2)

        # Кнопка "Назад", которая закрывает окно "О программе"
        ctk.CTkButton(main_frame, text="Назад", width=150, height=35, command=self.destroy).grid(
            row=2, column=0, columnspan=2, pady=(20, 0))

        self.mainloop()
