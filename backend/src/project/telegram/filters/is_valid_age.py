from typing import Any


async def is_valid_age(age: Any) -> bool:
    try:
        age = int(age)
        if isinstance(age, int) and 0 < age <= 121:
            return True
    except:
        pass
    else:
        return False
