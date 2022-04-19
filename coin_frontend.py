import psycopg2
from consolemenu import ConsoleMenu

conn = psycopg2.connect("dbname=cryptoproject user=matt host=localhost")
cur = conn.cursor()

cur.execute("SELECT tablename FROM pg_tables WHERE pg_tables.tableowner = current_user;")
tables = cur.fetchall()

def list_tables():
    for table, in tables:
        print(table)

def get_avg():
    coin = input("Enter the coin to analyze: ")
    cur.execute(f"SELECT AVG(close) FROM {coin};")
    print(f"Average price of {coin}: ${cur.fetchall()[0][0]}")

def get_avg_volume():
    coin = input("Enter the coin to analyze: ")
    cur.execute(f"SELECT AVG(volume) FROM {coin};")
    print(f"Average daily volume of {coin}: ${cur.fetchall()[0][0]}")

def get_max_market_cap():
    coin = input("Enter the coin to analyze: ")
    cur.execute(f"SELECT MAX(mcap) FROM {coin};")
    print(f"Biggest Market Capitalization of {coin}: ${cur.fetchall()[0][0]}")

menu = ConsoleMenu("", {
    "List All Tables": list_tables,
    "Calculate Average Price of a Coin": get_avg,
    "Calculate Average Volume of a Coin": get_avg_volume,
    "Calculate the Biggest Market Capitalization": get_max_market_cap,
})
menu.execute()
