import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = '<your database>'
)

cursor = con.cursor()

# Create function to access the database
def user_login(tup):
    try:
        cursor.execute("SELECT * FROM `admin` WHERE `user_name`=%s AND `password`=%s", tup)
        return(cursor.fetchone())
    except:
        return False


def add_income(tup):
    cursor.execute("INSERT INTO `income` (`income_source`, `description`) VALUES (%s, %s)", tup)
    con.commit()
    return True

# Fetch all data from the income table
def show_income():
    cursor.execute("SELECT * FROM `income`")
    return cursor.fetchall()

# Delete item from db
def delete_income(tup):
    cursor.execute("DELETE FROM `income` WHERE id= %s", tup)
    con.commit()
    return True

# Update item in db
def update_income(tup):
    cursor.execute("update income set income_source=%s, description=%s where id=%s", tup)
    con.commit()
    return True