from typing import TypeAlias
from .base import Base

# Custom class type for table schemas that inherit from Base
FormulaOneTableSchema: TypeAlias = type[Base]
