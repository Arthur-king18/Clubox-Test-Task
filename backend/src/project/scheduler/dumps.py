from apscheduler.triggers.cron import CronTrigger

from backend.src.project.db.dumps import create_pg_dump
from backend.src.project.scheduler import scheduler


@scheduler.scheduled_job(CronTrigger(hour=0, minute=0))
def create_dump_schedule():
    create_pg_dump()
