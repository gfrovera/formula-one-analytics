import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

# Used for easy dev config
load_dotenv()


@dataclass(frozen=True)
class DatabaseSettings:
    '''
    This is a container for all connection parameters.
    
    - The `frozen=True` makes it immutable (can't be changed after creation),
    which is a good practice for configuration objects—you don't want something
    accidentally modifying your database credentials mid-execution.

    - The @property method url constructs a SQLalchemy connection string
    '''
    user: str
    password: str
    host: str
    port: int
    name: str
    echo: bool

    @property
    def url(self) -> str:

        return (
            f'postgresql+psycopg://{self.user}:{self.password}'
            f'@{self.host}:{self.port}/{self.name}'
        )
    

def get_db_settings() -> DatabaseSettings:
    '''
    Read DB settings from environment variables

    All values must be defined in the environment (or .env file)
    Raises KeyError if any required variable is missing
    '''

    return DatabaseSettings(
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        port=int(os.environ['DB_PORT']),
        name=os.environ['DB_NAME'],
        echo=os.environ['DB_ECHO'].lower() == 'true',
    )


if __name__ == '__main__':
    raise SystemExit()