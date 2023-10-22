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
    with open("mustache.sql", "r") as sql_file:
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
        prices.append(float(line[0]))

    count = len(prices)
    mean_price = np.mean(prices)
    std_price = np.std(prices)
    min_price = np.min(prices)
    quartiles = np.percentile(prices, [25, 50, 75])
    max_price = np.max(prices)

    print(f"count {count:.6f}")
    print(f"mean {mean_price:.6f}")
    print(f"std {std_price:.6f}")
    print(f"min {min_price:.6f}")
    print(f"25% {quartiles[0]:.6f}")
    print(f"50% {quartiles[1]:.6f}")
    print(f"75% {quartiles[2]:.6f}")
    print(f"max {max_price:.6f}")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    boxes = ax1.boxplot(prices, vert=False, widths=0.5, notch=True,
                        boxprops=dict(facecolor='lightgray', edgecolor='none'),
                        flierprops=dict(marker='D', markersize=8, markerfacecolor='lightgray', markeredgecolor='none'),
                        patch_artist=True)
    ax1.set_yticks([])
    ax1.set_xlabel("Price")
    ax1.set_title("Full Box Plot")

    boxprops = dict(facecolor='green', edgecolor='black')
    medianprops = dict(linestyle='-', linewidth=2, color='black')
    ax2.boxplot(prices, vert=False, widths=0.5, notch=True,
                boxprops=boxprops, medianprops=medianprops, showfliers=False,
                patch_artist=True)
    ax2.set_yticks([])
    ax2.set_xlabel("Price")
    ax2.set_title("Interquartile range (IQR)")

    plt.tight_layout()
    plt.show()

# ----------------------------------------------------------------

except Exception as e:
    print(f"Error: {e}")