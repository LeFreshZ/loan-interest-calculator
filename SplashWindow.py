import customtkinter as ctk
from PIL import Image

from MainWindow import MainWindow

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SplashWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.title("MainWindow")
        self.geometry("600x600")
        self.resizable(False, False)  # Отключаем изменение размера окна
        self.grid_columnconfigure((0, 1), weight=1)

        self.image = ctk.CTkImage(Image.open(
            "./Images/SplashScreen.png"), size=(175, 175))

        # Верхний заголовок
        ctk.CTkLabel(self, text="Белорусский национальный технический университет", font=("Arial", 14)).grid(
            row=0, column=0, columnspan=2, pady=(10, 5), sticky="n"
        )

        # Факультет и кафедра
        faculty_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        faculty_frame.grid(row=1, column=0, columnspan=2,
                           pady=(10, 50), sticky="ew")
        faculty_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(faculty_frame, text="Факультет информационных технологий и робототехники", font=(
            "Arial", 12)).pack()
        ctk.CTkLabel(faculty_frame, text="Кафедра программного обеспечения информационных систем и технологий", font=(
            "Arial", 12)).pack()

        # Название курсовой
        course_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        course_frame.grid(row=2, column=0, columnspan=2,
                          pady=(10, 20), sticky="ew")
        course_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(course_frame, text="Курсовой проект",
                     font=("Arial", 20)).pack()
        ctk.CTkLabel(course_frame, text="по дисциплине Языки программирования", font=(
            "Arial", 14)).pack()
        ctk.CTkLabel(course_frame, text="Расчет процентов по кредиту",
                     font=("Arial", 22)).pack()

        # Информация о студенте
        student_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        student_frame.grid(row=3, column=1, pady=(
            20, 0), padx=(20, 0), sticky="n")
        ctk.CTkLabel(student_frame, text="Выполнил студент группы 10701223", font=(
            "Arial", 12)).pack(anchor="w")
        ctk.CTkLabel(student_frame, text="Гупанов Андрей Русланович",
                     font=("Arial", 12)).pack(anchor="w")

        ctk.CTkLabel(self, image=self.image, text="").grid(row=3, column=0, rowspan=2,
                                                           pady=(20, 0), sticky="n")

        # Информация о преподавателе
        teacher_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"))
        teacher_frame.grid(row=4, column=1, pady=(20, 0), sticky="n")

        ctk.CTkLabel(
            teacher_frame, text="Преподаватель: к.ф.-м.н., доц.", font=("Arial", 12)).pack(anchor="w")
        ctk.CTkLabel(teacher_frame, text="Сидорик Валерий Владимирович", font=(
            "Arial", 12)).pack(anchor="w")

        # Нижний текст
        ctk.CTkLabel(self, text="Минск, 2024", font=("Arial", 12)).grid(
            row=5, column=0, columnspan=2, pady=(20, 10), sticky="n")

        # Кнопки
        button_next = ctk.CTkButton(
            self, text="Далее", command=self.on_next, width=200)
        button_next.grid(row=6, column=0, padx=15, pady=15, sticky="ew")

        button_exit = ctk.CTkButton(
            self, text="Выход", command=self.destroy, width=200)
        button_exit.grid(row=6, column=1, padx=15, pady=15, sticky="ew")

        self.after(60000, lambda: self.destroy())

    def on_next(self):
        self.destroy()
        MainWindow()


if __name__ == "__main__":
    app = SplashWindow()
    app.mainloop()