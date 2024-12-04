from tkinter import filedialog
from LoanOrigin import LoanOrigin
from LoanResult import LoanResult


class FileOperator:
    """
    Класс для операций с файлами. Предоставляет функционал для сохранения данных о кредите
    (исходных данных и результатов расчёта) в текстовый файл.
    """

    @classmethod
    def save_to_file(cls, loan_origin: LoanOrigin, loan_result: LoanResult) -> None:
        """
        Сохраняет данные о кредите в текстовый файл.

        Параметры:
            loan_origin: Экземпляр LoanOrigin, содержащий исходные данные кредита (сумма, процентная ставка и срок).
            loan_result: Экземпляр LoanResult, содержащий результаты расчёта кредита (ежемесячный платёж, общая сумма выплат, переплата).
        """
        # Открытие диалогового окна для выбора имени и пути сохранения файла.
        filename = filedialog.asksaveasfilename(
            filetypes=[("Text  files", "*.txt")]
        )
        
        # Сохранение данных в указанный файл
        with open(filename, "w", encoding="utf-8") as file:
            # Запись исходных данных
            file.write("Исходные данные:" + "\n")
            file.write("Сумма кредита: " + str(loan_origin.get_sum()) + "\n")
            file.write("Процентная ставка: " + str(loan_origin.get_interest_rate() * 100) + "%" + "\n")
            file.write("Срок кредита (в месяцах): " + str(loan_origin.get_periods()) + "\n\n")
            
            # Запись результатов расчёта
            file.write("Результат:" + "\n")
            file.write("Ежемесячный платёж: " + str(loan_result.get_monthly_payment()) + "\n")
            file.write("Общая сумма выплат: " + str(loan_result.get_total_payment()) + "\n")
            file.write("Переплата по кредиту: " + str(loan_result.get_overpayment()))
