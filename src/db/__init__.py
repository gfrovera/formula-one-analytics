from .base import Base
from .session import engine
from . import models


def init_db():
    '''Creates all tables that don't exist yet in database'''
    Base.metadata.create_all(engine)
