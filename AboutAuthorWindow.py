import customtkinter as ctk
from PIL import Image


class AboutAuthorWindow(ctk.CTkToplevel):
    """
    Окно, которое отображает информацию о авторе программы. 
    Содержит изображение автора, его имя, контактные данные и дополнительные сведения.
    """

    def __init__(self, master):
        """
        Инициализация окна "О авторе".
        В окне будет отображена информация о разработчике программы.
        """
        super().__init__(master)
        self.title("О авторе")  # Заголовок окна
        self.geometry("300x450")  # Размеры окна
        self.resizable(False, False)  # Окно нельзя изменять по размеру

        # Загружаем изображение автора, которое будет отображаться в окне
        self.image = ctk.CTkImage(Image.open(
            "./Images/AboutAuthor.png"), size=(175, 175))

        # Основной фрейм, который содержит все элементы интерфейса окна
        main_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.pack(fill="both", expand=True, pady=10)

        # Заголовок окна, который говорит, что информация относится к автору
        ctk.CTkLabel(main_frame, text="Автор",
                     font=("Arial", 16)).pack(pady=10)

        # Изображение автора, которое будет отображаться в окне
        ctk.CTkLabel(main_frame, image=self.image, text="").pack(pady=(10, 20))

        # Информация о авторе, его контактные данные
        ctk.CTkLabel(main_frame, text="Студент группы 10701223",
                     font=("Arial", 14)).pack(pady=5)
        ctk.CTkLabel(main_frame, text="Гупанов Андрей Русланович",
                     font=("Arial", 14)).pack(pady=5)
        ctk.CTkLabel(main_frame, text="thescaver@gmail.com",
                     font=("Arial", 14)).pack(pady=5)

        # Кнопка "Назад", которая закрывает окно и возвращает пользователя в предыдущее окно
        back_button = ctk.CTkButton(
            main_frame, text="Назад", width=150, height=35, command=self.destroy)
        back_button.pack(pady=15)
