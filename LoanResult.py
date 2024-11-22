class LoanResult:
    def __init__(self, monthly_payment: float, total_payment: float, overpayment: float):
        self.__monthly_payment = monthly_payment
        self.__total_payment = total_payment
        self.__overpayment = overpayment
        
    def get_monthly_payment(self) -> float:
        return self.__monthly_payment
    
    def get_total_payment(self) -> float:
        return self.__total_payment
    
    def get_overpayment(self) -> float:
        return self.__overpayment