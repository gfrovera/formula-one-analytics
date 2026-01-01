from contextlib import contextmanager
from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from .config import get_db_settings


_settings = get_db_settings()

engine = create_engine(
    _settings.url,
    echo=_settings.echo,
    future=True # default in SQLalchemy 2.0+ leaving in for back compat
)

SessionLocal = (
    sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False
    )
)


@contextmanager
def get_session() -> Iterator[Session]:
    '''Provide a transactional scope around a series of ops'''

    session: Session = SessionLocal()

    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == '__main__':
    raise SystemExit()
