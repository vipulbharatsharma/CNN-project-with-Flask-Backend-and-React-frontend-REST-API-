import sqlite3



connection = sqlite3.connect('data.db')
cursor = connection.cursor()
sql = "SELECT * FROM employees WHERE designation = 'Frontend Developer'"
val = [('John', 'Frontend Developer', '5 lpa'),
       ('Max', 'Backend Developer', '6 lpa'),
       ('Linda', 'UI/UX Designer', '5 lpa'),
       ('James', 'Tester', '4 lpa'),
       ('Ava', 'Team Lead', '7 lpa'),
       ('Emily', 'ML Engineer', '6 lpa'),
       ('Olivia', 'Cloud Engineer', '6 lpa'),
       ('William', 'Product Manager', '7 lpa'),
       ('George', 'Frontend Developer', '6 lpa'),
       ('Thomas', 'Backend Developer', '6 lpa'),
       ('Mason', 'Manager', '8 lpa'),
       ('Joanne', 'Data Analyst', '6 lpa'),
       ('Ethan', 'Data Scientist', ' 5 lpa'),
       ('Michael', 'Product Manager', '8 lpa'),
       ('Susan', 'HR', '5 lpa'),
       ('Charlie', 'QA Lead', '6 lpa')
       
       ]
result = cursor.execute(sql)
print(result.fetchall())
connection.commit()
connection.close()


def get_employee(_id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    sql = 'SELECT * FROM employees WHERE id = ?'
    val = (_id,)
    result = cursor.execute(sql, val)
    #print(result.fetchall())
    

    return result.fetchall()





