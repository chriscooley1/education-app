from sqlalchemy import create_engine, text


engine = create_engine("sqlite+pysqlite:///education.db", echo=True)


create_students_table = """
Create table students (
    student_id integer primary key,
    first_name text,
    last_name text,
    email text,
    enrollment_year integer
)
"""

insert_student = """
Insert into students 
    (first_name, last_name, email, enrollment_year)
    values ('Chris', 'Cooley', 'ccooley@msn.com', 2024)
"""


with engine.connect() as conn:
    conn.execute(text(create_students_table))
    conn.execute(text(insert_student))
    conn.commit()
    result = conn.execute(text("select * from students"))
    print(result.all())