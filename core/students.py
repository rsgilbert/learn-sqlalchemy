from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session



# Use an in-memory only SQLite database
engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)


with engine.begin() as conn:
    conn.execute(text('CREATE TABLE students(id INT, name VARCHAR(100))'))
    conn.execute(
        text('INSERT INTO students(id, name) VALUES(:id, :name)'),
        [
            { 'id': 1000, 'name': 'James' },
            { 'id': 2000, 'name': 'Peter' },
            { 'id': 3000, 'name': 'Mary'}
        ]
    )
    # conn.commit()


# with engine.connect() as conn:
#     students_result = conn.execute(text('SELECT * FROM students WHERE id >= :minId'), { 'minId': 2000 })
#     print(students_result.all())


with Session(engine) as session:
    result = session.execute(text("SELECT * FROM students"))
    for row in result:
        print('row:', row)
    session.commit()
    