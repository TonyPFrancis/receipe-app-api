"""
Wait for database to be available for app the connect
"""
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    Django command to wait for DB to be available
    """

    default_wait_time = 5

    def handle(self, *args, **options):
        """Entrypoint for wait_for_db command"""
        self.stdout.write("Waiting for database")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OperationalError, OperationalError):
                self.stdout.write(
                    self.style.ERROR(
                        f"Database unavailable, waiting for "
                        f"{self.default_wait_time} seconds"
                    )
                )
                time.sleep(self.default_wait_time)
        self.stdout.write(self.style.SUCCESS("Database available"))
