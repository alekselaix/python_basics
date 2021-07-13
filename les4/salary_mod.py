def calc(time, rate, bonus):
    """
    Рассчет заработной платы сотрудника
    по формуле: (выработка в часах*ставка в час) + премия
    :param time: выроботка в часах
    :param rate: ставка за 1 час
    :param bonus: премия
    :return:зарплата
    """
    try:
        time = float(time)
        rate = float(rate)
        bonus = float(bonus)

        return time * rate + bonus
    except TypeError:
        return
