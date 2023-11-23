import pymysql

conn = pymysql.connect(
    host='localhost',
    user='abhi',
    password='abhi',
    db='eagle_eye',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # Read data from database
        sql = "SELECT * FROM `ee`"
        cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)
finally:
    conn.close()