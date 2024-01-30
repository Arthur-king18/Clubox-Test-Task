from backend.src.project.logs import configure_logging

configure_logging()

import nest_asyncio

nest_asyncio.apply()

from tortoise import Tortoise, connections

from functools import partial
from fastapi import FastAPI
from backend.src.project.scheduler import scheduler
from backend.src.project.telegram import signals as telegram_signals
from backend.src.project.db.config import config
from backend.src.project.db.migrations import run_migration
from backend.src.project.settings import settings

app = FastAPI(
    on_startup=[
        run_migration,
        partial(Tortoise.init, config=config),
        Tortoise.generate_schemas,
        scheduler.start,
        telegram_signals.on_startup,
    ],
    on_shutdown=[
        telegram_signals.on_shutdown,
        scheduler.shutdown,
        connections.close_all,
    ],
    debug=settings.DEBUG,
)

from . import middlewares
from . import routes
