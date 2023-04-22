from sqlalchemy import MetaData, Table, Column, Integer, String

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("fullname", String)
)

print(user_table)
print(user_table.c)
print(user_table.c.keys)
print(user_table.c.name)
print(user_table.c.fullname)
print(user_table.primary_key)

