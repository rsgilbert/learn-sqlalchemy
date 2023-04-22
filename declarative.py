# Define table in a declarative way

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

print(Base.metadata)
print(Base.registry)