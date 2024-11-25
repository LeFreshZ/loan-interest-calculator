class LoanOrigin:
    def __init__(self, credit_sum: str, interest_rate: str, periods: str):
        self.__credit_sum = float(credit_sum)
        self.__interest_rate = float(interest_rate) / 100
        self.__periods = int(periods)

    def get_sum(self) -> float:
        return self.__credit_sum

    def get_interest_rate(self) -> float:
        return self.__interest_rate

    def get_periods(self) -> int:
        return self.__periods
