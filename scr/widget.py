def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты по шаблону XXXX XX** **** XXXX
    """
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета по шаблону **XXXX
    """
    account_str = str(account_number)
    if len(account_str) < 6:
        raise ValueError("Номер счета должен содержать минимум 6 цифр")

    return f"**{account_str[-4:]}"


def mask_account_card(input_string: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа
    """
    # Находим позицию начала номера
    for i, char in enumerate(input_string):
        if char.isdigit():
            break

    # Извлекаем название и номер
    name_part = input_string[:i].strip()
    number_part = input_string[i:].strip()

    try:
    # Преобразуем номер в число
        number = int(number_part)

    # Определяем тип и применяем соответствующую маску
        if 'Счет' in name_part:
            masked_number = get_mask_account(number)
        else:
            masked_number = get_mask_card_number(number)

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
            original_date = datetime.fromisoformat(date_string)
    # Форматируем в нужный формат
            formatted_date = original_date.strftime('%d.%m.%Y')
            return formatted_date