class LoanResult:
    """
    Класс для представления результатов расчета по кредиту.

    Содержит информацию о ежемесячном платеже, общей сумме выплат и переплате по кредиту.
    """

    def __init__(self, monthly_payment: float, total_payment: float, overpayment: float):
        """
        Конструктор для инициализации результатов расчета.

        Параметры:
            monthly_payment (float): Ежемесячный платеж по кредиту.
            total_payment (float): Общая сумма выплат по кредиту.
            overpayment (float): Переплата (сумма, уплаченная сверх основной суммы кредита).
        """
        self.__monthly_payment = monthly_payment  # Ежемесячный платеж
        self.__total_payment = total_payment  # Общая сумма выплат
        self.__overpayment = overpayment  # Переплата по кредиту

    def get_monthly_payment(self) -> float:
        """
        Получение ежемесячного платежа.

        Возвращает:
            float: Ежемесячный платеж.
        """
        return self.__monthly_payment

    def get_total_payment(self) -> float:
        """
        Получение общей суммы выплат.

        Возвращает:
            float: Общая сумма выплат.
        """
        return self.__total_payment

    def get_overpayment(self) -> float:
        """
        Получение переплаты по кредиту.

        Возвращает:
            float: Переплата.
        """
        return self.__overpayment
