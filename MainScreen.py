import customtkinter as ctk
import tkinter.messagebox as mb

from LoanCalculator import LoanCalculator


class MainScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.title("MainScreen")
        self.geometry("600x500")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)

        # Основной фрейм для ввода и вывода
        main_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"), border_width=2, border_color="white")
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)

        # Поля ввода
        input_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        input_frame.grid(row=0, column=0, pady=20, padx=20, sticky="nsew")
        input_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(input_frame, text="Сумма кредита:", width=140).grid(row=0, column=0, sticky="w", pady=5)
        self.CredSum_TB = ctk.CTkEntry(input_frame)
        self.CredSum_TB.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Процентная ставка:", width=140).grid(row=1, column=0, sticky="w", pady=5)
        self.Procent_TB = ctk.CTkEntry(input_frame)
        self.Procent_TB.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Срок кредита:", width=140).grid(row=2, column=0, sticky="w", pady=5)
        self.Time_TB = ctk.CTkEntry(input_frame)
        self.Time_TB.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Кнопка "Рассчитать"
        self.Calc_BTN = ctk.CTkButton(main_frame, text="Рассчитать", command=self.calculate, width=150)
        self.Calc_BTN.grid(row=1, column=0, pady=20, sticky="n")

        # Поля вывода
        output_frame = ctk.CTkFrame(main_frame, fg_color=self.cget("bg"))
        output_frame.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")
        output_frame.grid_columnconfigure(1, weight=1)
        
        self.Clear_BTN = ctk.CTkButton(main_frame, text="Очистить", command=self.clear_fields, width=150)
        self.Clear_BTN.grid(row=3, column=0, pady=20, sticky="n")

        ctk.CTkLabel(output_frame, text="Ежемесячный платёж:", width=140).grid(row=0, column=0, sticky="w", pady=5)
        self.ResMonth_TB = ctk.CTkEntry(output_frame, state="disabled")
        self.ResMonth_TB.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(output_frame, text="Общая сумма выплат:", width=140).grid(row=1, column=0, sticky="w", pady=5)
        self.ResSum_TB = ctk.CTkEntry(output_frame, state="disabled")
        self.ResSum_TB.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(output_frame, text="Переплата:", width=140).grid(row=2, column=0, sticky="w", pady=5)
        self.OverPrice_TB = ctk.CTkEntry(output_frame, state="disabled")
        self.OverPrice_TB.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Боковая панель с кнопками
        side_panel = ctk.CTkFrame(self, fg_color=self.cget("bg"), border_width=2, border_color="white") 
        side_panel.grid(row=0, column=1, padx=20, pady=20, sticky="ns")
        side_panel.grid_rowconfigure(0, weight=1)

        self.AboutAuthor_BTN = ctk.CTkButton(side_panel, text="Об авторе", width=120, command=self.about_author)
        self.AboutAuthor_BTN.pack(pady=(25,5), padx=15)

        self.AboutProgram_BTN = ctk.CTkButton(side_panel, text="О программе", width=120, command=self.about_program)
        self.AboutProgram_BTN.pack(pady=5, padx=15)

        self.Help_BTN = ctk.CTkButton(side_panel, text="Помощь", width=120, command=self.help_info)
        self.Help_BTN.pack(pady=5, padx=15)

        # Кнопка "Выход"
        self.Exit_BTN = ctk.CTkButton(side_panel, text="Выход", width=120, command=self.exit_program)
        self.Exit_BTN.pack(side="bottom", pady=20)

    def calculate(self):
        try:
            res = LoanCalculator.calculate(self.CredSum_TB.get(), self.Procent_TB.get(), self.Time_TB.get())
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
            return
        
        self.ResMonth_TB.configure(state="normal")
        self.ResMonth_TB.delete(0, "end")
        self.ResMonth_TB.insert(0, f"{res[0]:.2f}")
        self.ResMonth_TB.configure(state="disabled")

        self.ResSum_TB.configure(state="normal")
        self.ResSum_TB.delete(0, "end")
        self.ResSum_TB.insert(0, f"{res[1]:.2f}")
        self.ResSum_TB.configure(state="disabled")

        self.OverPrice_TB.configure(state="normal")
        self.OverPrice_TB.delete(0, "end")
        self.OverPrice_TB.insert(0, f"{res[2]:.2f}")
        self.OverPrice_TB.configure(state="disabled")

    def about_author(self):
        print("Об авторе")

    def about_program(self):
        print("О программе")

    def help_info(self):
        print("Помощь")

    def exit_program(self):
        self.destroy()

    def clear_fields(self):
        for field_name in ["CredSum_TB", "Procent_TB", "Time_TB", "ResMonth_TB", "ResSum_TB", "OverPrice_TB"]:
            field = getattr(self, field_name)
            field.configure(state="normal")
            field.delete(0, "end")
            if field_name in ["ResMonth_TB", "ResSum_TB", "OverPrice_TB"]:
                field.configure(state="disabled")