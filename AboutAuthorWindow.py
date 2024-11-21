import customtkinter as ctk
from PIL import Image


class AboutAuthorWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("О авторе")
        self.geometry("300x450")
        self.resizable(False, False)

        self.image = ctk.CTkImage(Image.open(
            "./Images/AboutAuthor.png"), size=(175, 175))

        # Основной фрейм с выравниванием по центру
        main_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.pack(fill="both", expand=True, pady=10)

        # Заголовок
        ctk.CTkLabel(main_frame, text="Автор",
                     font=("Arial", 16)).pack(pady=10)

        # Изображение
        ctk.CTkLabel(main_frame, image=self.image, text="").pack(pady=(10, 20))

        # Информация об авторе
        ctk.CTkLabel(main_frame, text="Студент группы 10701223",
                     font=("Arial", 14)).pack(pady=5)
        ctk.CTkLabel(main_frame, text="Гупанов Андрей Русланович",
                     font=("Arial", 14)).pack(pady=5)
        ctk.CTkLabel(main_frame, text="thescaver@gmail.com",
                     font=("Arial", 14)).pack(pady=5)

        # Кнопка "Назад"
        back_button = ctk.CTkButton(
            main_frame, text="Назад", width=150, height=35, command=self.destroy)
        back_button.pack(pady=15)
