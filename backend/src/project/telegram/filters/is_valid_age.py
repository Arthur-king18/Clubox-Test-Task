from typing import Any


async def is_valid_age(age: Any) -> bool:
    if isinstance(age, int) and 0 < age <= 121:
        return True

    else:
        return False
