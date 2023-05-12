from sqlalchemy import create_engine, text

# Use an in-memory only SQLite database
engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 'hello world'"))
    print(result.all())

