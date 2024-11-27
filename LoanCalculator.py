from LoanOrigin import LoanOrigin
from LoanResult import LoanResult


class LoanCalculator:
    """
    Класс для расчета аннуитетных платежей по кредиту.
    Содержит метод, который принимает объект типа LoanOrigin с данными о кредите
    и возвращает объект LoanResult с результатами расчета.
    """

    @classmethod
    def calculate(cls, loan: LoanOrigin) -> LoanResult:
        """
        Метод для расчета аннуитетных платежей по кредиту.

        Параметры:
            loan (LoanOrigin): Объект класса LoanOrigin, содержащий информацию о кредите (сумма, ставка, срок).

        Возвращает:
            LoanResult: Объект класса LoanResult, который содержит результаты расчета:
            - ежемесячный платёж
            - общую сумму выплат
            - переплату.

        Исключения:
            Exception: Если одно из значений (сумма, процентная ставка или срок кредита) меньше или равно нулю.
        """
        # Проверка, что все значения больше нуля
        if loan.get_sum() <= 0 or loan.get_interest_rate() <= 0 or loan.get_periods() <= 0:
            raise Exception("Все значения должны быть больше нуля.")

        # Рассчитываем ежемесячную процентную ставку
        monthly_rate = loan.get_interest_rate() / 12

        # Рассчитываем коэффициент аннуитета
        annuity_coeff = (monthly_rate * (1 + monthly_rate)
                         ** loan.get_periods()) / ((1 + monthly_rate) ** loan.get_periods() - 1)

        # Рассчитываем ежемесячный платёж
        monthly_payment = annuity_coeff * loan.get_sum()

        # Рассчитываем общую сумму выплат по кредиту
        total_payment = loan.get_periods() * monthly_payment

        # Рассчитываем переплату (общая сумма выплат минус сумма кредита)
        overpayment = total_payment - loan.get_sum()

        # Возвращаем объект LoanResult с результатами
        return LoanResult(monthly_payment, total_payment, overpayment)
