import pymysql

# Replace with your actual credentials
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='ASHla1212!',
    database='bite',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Example query to test connection
        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()
        print("MySQL version:", result)
finally:
    connection.close()