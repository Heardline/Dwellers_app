
from typing import Tuple
from neighbour.models import models

async def add_user(tg_id: int, full_name: str) -> Tuple[models.User, bool]:
    return await models.User.get_or_create(
        tg_id=tg_id, full_name=full_name
    )