class LoanCalculator:
    
    @classmethod
    def calculate(cls, credit_sum: str, interest_rate: str, periods: str) -> tuple:
        try:
            credit_sum = float(credit_sum)
            interest_rate = float(interest_rate) / 100
            periods = int(periods)

            if credit_sum <= 0 or interest_rate <= 0 or periods <= 0:
                raise Exception("Все значения должны быть больше нуля.")

            monthly_rate = interest_rate / 12
            
            if monthly_rate <= 0 or periods <= 0:
                raise Exception("Процентная ставка и число периодов должны быть больше нуля.")

            annuity_coeff = (monthly_rate * (1 + monthly_rate) ** periods) / ((1 + monthly_rate) ** periods - 1)
            monthly_payment = annuity_coeff * credit_sum
            total_payment = periods * monthly_payment
            overpayment = total_payment - credit_sum 
        
            return (monthly_payment, total_payment, overpayment)
        except Exception as e:
            raise Exception(f"Произошла ошибка: {e}")
        