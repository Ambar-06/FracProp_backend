import datetime as dt
import random as _r
import string


def generate_random_id_number(
    optional_number: int = None,
    length: int = _r.randint(10, 15),  # nosec
    use_alphanumeric: bool = True,
    use_small_letters: bool = False,
) -> str:
    """
    Generates a random ID number using random length, 2 random strings of random length, one random combination of 2 random strings sliced using random length and timestamp numeric value of random length.
    """
    if optional_number is None:
        optional_number = _r.randint(10, 99)  # nosec
    elif optional_number < 10 or optional_number > 99:
        optional_number = _r.randint(10, 99)  # nosec

    if use_alphanumeric:
        if use_small_letters:
            alpha_str = string.ascii_letters
        else:
            alpha_str = string.ascii_uppercase
        random_string_1 = "".join(_r.choices(alpha_str, k=_r.randint(4, 5)))  # nosec
        random_string_2 = "".join(_r.choices(alpha_str, k=_r.randint(4, 5)))  # nosec
        random_string_combined = random_string_1 + random_string_2
        random_string_3 = "".join(
            _r.choices(random_string_combined, k=_r.randint(4, 6))  # nosec
        )

    current_time = dt.datetime.now()
    milliseconds = current_time.microsecond // 1000
    microseconds = current_time.microsecond % 1000
    combined_number = (
        int(optional_number) * 1000000 + milliseconds * 1000 + microseconds
    )

    numeric_part = str(combined_number)[: _r.randint(4, 7)]  # nosec

    if not use_alphanumeric:
        return str(combined_number)[:length]

    return (random_string_1 + random_string_3 + numeric_part + random_string_2)[:length]
