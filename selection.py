from sqlalchemy import select, insert, create_engine, MetaData, Table, Column, Integer, ForeignKey, String

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("fullname", String)
)

metadata_obj.create_all(engine)

stmt = select(user_table).where(user_table.c.name == 'Jackson')
# print(stmt)

with engine.connect() as conn:
    insert_stmt = insert(user_table).values(name="Katar", fullname="Katara The water bender")
    conn.execute(insert_stmt)
    conn.execute(insert(user_table).values(name="James", fullname="Matthewson"))
    conn.execute(insert(user_table).values(name="Angella", fullname='Malaika'))
    select_stmt = select(user_table.c['name'], user_table.c.fullname).where(user_table.c.name >="James")
    select_result = conn.execute(select_stmt)
    print(select_result.all())

