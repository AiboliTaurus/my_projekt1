import pytest
from scr.widget import mask_account_card, get_date


def test_mask_account_card_card():
    # Карта с текстом
    assert mask_account_card, get_date("Карта 1234567890123456") == "Карта 1234 56** **** 3456"

    # Только номер карты
    assert mask_account_card, get_date("1234567890123456") == "1234 56** **** 3456"


def test_mask_account_card_account():
    # Счет с текстом
    assert mask_account_card, get_date("Счет 1234567890123456") == "Счет **3456"

    # Разные варианты написания "счет"
    assert mask_account_card, get_date("СЧЕТ 1234567890123456") == "СЧЕТ **3456"
    assert mask_account_card, get_date("счет 1234567890123456") == "счет **3456"


def test_mask_account_card_invalid():
    # Неверный формат номера
    with pytest.raises(ValueError):
        mask_account_card, get_date("Неверный формат 1234")