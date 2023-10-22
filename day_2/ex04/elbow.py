import matplotlib.pyplot as plt
import psycopg2
from sklearn.cluster import KMeans

dbname = "piscineds"
user = "jergashe"
password = "msp"
host = "localhost"
port = "5432"


try:
    # with keyword makes sure the file is closed
    # after the block is executed even if exception is raised
    with open("elbow.sql", "r") as sql_file:
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


# ----------------------------------------------------------------


    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    wss = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=0, n_init=10).fit(data)
        wss.append(kmeans.inertia_)

    plt.plot(range(1, 11), wss)
    plt.xlabel("Number of clusters")
    plt.title("The Elbow Method")
    plt.show()

# ----------------------------------------------------------------



    # conn.commit()
    # commit is used to save the changes made to the database

except Exception as e:
    print("Error:", e)

finally:
    conn.close()
    cursor.close()
