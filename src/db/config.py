import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

# Used for easy dev config
load_dotenv()


@dataclass(frozen=True)
class DatabaseSettings:
    user: str
    password: str
    host: str = 'localhost'
    port: int = 5432
    name: str = 'f1db'
    echo: bool = False

    @property
    def url(self) -> str:

        return (
            f'postgresql+psycopg://{self.user}:{self.password}'
            f'@{self.host}:{self.port}/{self.name}'
        )
    

def get_db_settings() -> DatabaseSettings:
    '''Read DB settings from environment variables
    '''

    return DatabaseSettings(
        user=os.getenv('DB_USER', 'f1user'),
        password=os.environ['DB_PASSWORD'],
        host=os.getenv('DB_HOST', 'localhost'),
        port=int(os.getenv('DB_PORT', '5432')),
        name=os.getenv('DB_NAME', 'f1db'),
        echo=os.getenv('DB_ECHO', 'false').lower() == 'true',
    )