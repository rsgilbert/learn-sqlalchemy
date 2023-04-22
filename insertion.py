from sqlalchemy import insert, create_engine, MetaData, Table, Column, Integer, ForeignKey, String

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("fullname", String)
)

stmt = insert(user_table).values(name="Katar", fullname="Katara The water bender")
print(stmt)
compiled = stmt.compile()
print(compiled)
print(compiled.params)

metadata_obj.create_all(engine)

with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result)
    print('inserted pk', result.inserted_primary_key)
    conn.commit()
    conn.execute(insert(user_table)) # inserts default values only
    print(insert(user_table))

