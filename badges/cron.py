from datetime import datetime, timedelta
from django_cron import CronJobBase, Schedule
from django.contrib.auth.models import User

from utils import create_badge
from conf import BADGES_DICT


class AnniversaryJob(CronJobBase):
    """
    Runs every 24 hours to check the subscription date of all users.
    Give the Pionneer badge if the user joined 1 year ago.
    """
    RUN_EVERY_MINS = 3600  # every 24 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "badges.anniversary_job"

    def do(self):
        for user in User.objects.all():
            if (datetime.now() - user.date_joined) > timedelta(years=1):
                create_badge(BADGES_DICT["Pionneer"], user)
