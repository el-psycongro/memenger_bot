from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import pytz
import config

jobstores = {
    'default': SQLAlchemyJobStore(url=config.POSTGRES_URL.replace('+asyncpg', '')),
}

executors = {
    'default': AsyncIOExecutor(),
}

job_defaults = {"coalesce": False, "max_instances": 3, "misfire_grace_time": 3600}

scheduler = AsyncIOScheduler(
    jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=pytz.utc
)
