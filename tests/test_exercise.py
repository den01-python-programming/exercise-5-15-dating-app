import pytest
from src.simple_date import SimpleDate

def test_exercise():
    date = SimpleDate(13, 2, 2015)

    assert str(date) == "13.2.2015"

    assert str(date.after_number_of_days(7)) == "20.2.2015"

    now = SimpleDate(13, 2, 2015)
    after_one_week = now
    after_one_week.after_number_of_days(7)

    assert str(now) == str(after_one_week)
