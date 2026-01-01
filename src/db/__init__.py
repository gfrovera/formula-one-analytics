from .base import Base
from .session import engine
from .session import get_session
from . import models


def init_db():
    '''Creates all tables that don't exist yet in database'''
    Base.metadata.create_all(engine)


def get_data_loader():
    '''Lazy import to avoid circular dependency'''
    from .loaders import data_loader
    return data_loader

__all__ = [
    'Base',
    'engine',
    'get_session',
    'models',
    'init_db',
    'get_data_loader',
]

