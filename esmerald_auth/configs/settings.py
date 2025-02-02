import os
from edgy import Database, Registry
from esmerald import EsmeraldAPISettings
from esmerald_simple_jwt.config import SimpleJWT
from functools import cached_property
from typing import Optional, Tuple

from esmerald_auth.apps.accounts.backends import BackendAuthentication, RefreshAuthentication

DATABASE_URL = os.environ.get("DATABASE_URI", "sqlite:///db.sqlite")


class AppSettings(EsmeraldAPISettings):
    """
    The settings object for the application.
    """

    @cached_property
    def db_connection(self) -> Tuple[Database, Registry]:
        """
        This conenction is used in `myapp/apps/accounts/models.py.
        """
        database = Database(DATABASE_URL)
        return database, Registry(database=database)

    @property
    def simple_jwt(self) -> SimpleJWT:
        # from esmerald_auth.apps.accounts.backends import BackendAuthentication, RefreshAuthentication
        return SimpleJWT(
            signing_key=self.secret_key,
            backend_authentication=BackendAuthentication,
            backend_refresh=RefreshAuthentication,
        )
