class LoanOrigin:
    """
    Класс для представления данных о кредите.

    Содержит информацию о сумме кредита, процентной ставке и сроке кредита в месяцах.
    Используется для передачи данных в расчетные методы (например, в LoanCalculator).
    """

    def __init__(self, credit_sum: str, interest_rate: str, periods: str):
        """
        Конструктор для инициализации данных о кредите.

        Параметры:
            credit_sum (str): Сумма кредита в виде строки, которая будет преобразована в тип float.
            interest_rate (str): Годовая процентная ставка в процентах в виде строки, которая будет преобразована в тип float.
            periods (str): Срок кредита в месяцах в виде строки, которая будет преобразована в тип int.
        """
        self.__credit_sum = float(
            credit_sum)  # Преобразуем строку в число с плавающей точкой для суммы кредита
        # Преобразуем строку в процентную ставку в долях (например, 5% -> 0.05)
        self.__interest_rate = float(interest_rate) / 100
        # Преобразуем строку в целое число для срока кредита в месяцах
        self.__periods = int(periods)

    def get_sum(self) -> float:
        """
        Получение суммы кредита.

        Возвращает:
            float: Сумма кредита.
        """
        return self.__credit_sum

    def get_interest_rate(self) -> float:
        """
        Получение процентной ставки.

        Возвращает:
            float: Процентная ставка в долях.
        """
        return self.__interest_rate

    def get_periods(self) -> int:
        """
        Получение срока кредита.

        Возвращает:
            int: Срок кредита в месяцах.
        """
        return self.__periods
