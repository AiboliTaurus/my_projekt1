def mask_account_card(input_string: str) -> str:
    from masks import get_mask_account, get_mask_card_number  # Импортируем функции из masks.py
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

        # Проверяем наличие слова "счет" без учета регистра
        if 'счет' in name_part.lower():
            masked_number = get_mask_account(number)
        else:
            masked_number = get_mask_card_number(number)

        return f"{name_part} {masked_number}"

    except ValueError:
        raise ValueError("Ошибка при обработке номера")

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
    except ValueError:
        raise ValueError("Неверный формат даты. Ожидается формат 'ГГГГ-ММ-ДДТЧЧ:ММ:СС'")
