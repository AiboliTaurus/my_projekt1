def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты по шаблону XXXX XX** **** XXXX
    """
    if len(card_number) != 16:
        raise ValueError("Неверный формат номера карты")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета по шаблону **XXXX
    """
    if len(account_number) < 6:
        raise ValueError("Неверный формат номера счета")

    return f"**{account_number[-4:]}"


def mask_account_card(input_string: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа
    """
    # Ищем разделитель между названием и номером
    for i, char in enumerate(input_string):
        if char.isdigit():
            break

    # Извлекаем название и номер
    name_part = input_string[:i].strip()
    number_part = input_string[i:].strip()

    # Определяем тип и применяем соответствующую маску
    if 'Счет' in name_part:
        masked_number = get_mask_account(number_part)
    else:
        masked_number = get_mask_card_number(number_part)

    return f"{name_part} {masked_number}"


from datetime import datetime


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой из формата ISO в формат ДД.ММ.ГГГГ

    Args:
        date_string (str): Строка с датой в формате "2024-03-11T02:26:18.671407"

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ"
    """
    try:
        # Парсим исходную дату
        original_date = datetime.fromisoformat(date_string.replace('Z', ''))
        # Форматируем в нужный формат
        formatted_date: str = original_date.strftime('%d.%m.%Y')
        return formatted_date
