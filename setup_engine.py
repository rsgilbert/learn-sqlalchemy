from sqlalchemy import create_engine

# Use an in-memory only SQLite database
engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)
print(engine)