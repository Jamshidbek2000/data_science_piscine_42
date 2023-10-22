import numpy as np
import matplotlib.pyplot as plt
import psycopg2

dbname = "piscineds"
user = "jergashe"
password = "msp"
host = "localhost"
port = "5432"


try:
    # with keyword makes sure the file is closed
    # after the block is executed even if exception is raised
    with open("cart.sql", "r") as sql_file:
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
    print("Data has been fetched from the table.")

    conn.commit()
    cursor.close()
    conn.close()

    prices = []
    for line in data:
        prices.append(float(line[1]))


    plt.figure(figsize=(10, 6))
    plt.boxplot(prices, vert=False, widths=0.5, notch=True,
                boxprops=dict(facecolor='blue', edgecolor='black'),
                flierprops=dict(marker='D', markersize=8, markerfacecolor='lightgray', markeredgecolor='none'),
                patch_artist=True, whis=0.2)
    plt.xticks(np.arange(5, 181, step=8))
    plt.tight_layout()
    plt.xlim(5,181)
    plt.yticks([])
    plt.show()


# ----------------------------------------------------------------


except Exception as e:
    print(f"Error: {e}")