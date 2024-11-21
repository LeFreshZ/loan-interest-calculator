import customtkinter as ctk
from PIL import Image


class AboutProgramWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("О программе")
        self.geometry("600x325")
        self.resizable(False, False)

        self.image = ctk.CTkImage(Image.open(
            "./Images/AboutProgram.png"), size=(150, 150))

        # Основной фрейм
        main_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Заголовок
        ctk.CTkLabel(
            main_frame,
            text="Данная программа предназначена для расчёта аннуитетных платежей по кредиту.",
            font=("Arial", 14),
            wraplength=560,
            anchor="center"
        ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Изображение
        ctk.CTkLabel(main_frame, image=self.image, text="").grid(
            row=1, column=0, pady=(0, 20), padx=20)

        # Описание
        description_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        description_frame.grid(row=1, column=1, sticky="n", padx=20)

        ctk.CTkLabel(description_frame, text="Программа позволяет:",
                     font=("Arial", 14)).pack(anchor="w", pady=(0, 5))
        ctk.CTkLabel(description_frame, text="1. Рассчитать сумму ежемесячного платежа.", font=(
            "Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(description_frame, text="2. Определить общую сумму выплат.", font=(
            "Arial", 12)).pack(anchor="w", pady=2)
        ctk.CTkLabel(description_frame, text="3. Узнать переплату по кредиту.", font=(
            "Arial", 12)).pack(anchor="w", pady=2)

        # Кнопка "Назад"
        back_button = ctk.CTkButton(
            main_frame,
            text="Назад",
            width=150,
            height=35,
            command=self.destroy
        )
        back_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))
