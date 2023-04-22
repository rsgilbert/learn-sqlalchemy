from sqlalchemy import create_engine, text

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


with engine.connect() as conn:
    students = conn.execute(text('SELECT * FROM students'))
    print(students.all())

