import psycopg2

dbname = "piscineds"
user = "jergashe"
password = "msp"
host = "localhost"
port = "5432"


try:
    # with keyword makes sure the file is closed
	# after the block is executed even if exception is raised
    with open("items_table.sql", "r") as sql_file:
        sql_script = sql_file.read()
    print("SQL code have been imported!")
    
	# to establish connection to the postgres database
	# conn holds the connection object
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to postgres!")

    cursor = conn.cursor()
    # curson is an object that allows you to
	# interact with the database
	# Mostly used for: 
	# 1. Executing SQL statements
    # 2. Fetching data from the database
	# 3. Transaction management
	# 4. Data manipulation

    cursor.execute(sql_script)
    print("SQL script executed successfully!")

    conn.commit()
    # commit is used to save the changes made to the database

except Exception as e:
    print("Error:", e)

finally:
    conn.close()
    cursor.close()
