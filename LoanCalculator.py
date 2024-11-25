from LoanOrigin import LoanOrigin
from LoanResult import LoanResult


class LoanCalculator:

    @classmethod
    def calculate(cls, loan: LoanOrigin) -> LoanResult:
        if loan.get_sum() <= 0 or loan.get_interest_rate() <= 0 or loan.get_periods() <= 0:
            raise Exception("Все значения должны быть больше нуля.")

        monthly_rate = loan.get_interest_rate() / 12

        annuity_coeff = (monthly_rate * (1 + monthly_rate)
                         ** loan.get_periods()) / ((1 + monthly_rate) ** loan.get_periods() - 1)
        monthly_payment = annuity_coeff * loan.get_sum()
        total_payment = loan.get_periods() * monthly_payment
        overpayment = total_payment - loan.get_sum()

        return LoanResult(monthly_payment, total_payment, overpayment)
