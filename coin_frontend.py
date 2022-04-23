import psycopg2
import click
import pyfiglet

from simple_term_menu import TerminalMenu
from blessings import Terminal
from termcolor import colored
from pyfiglet import Figlet

# Connect to database
conn = psycopg2.connect("dbname=cryptoproject user=houchins host=127.0.0.1")
cur = conn.cursor()

# Variables
t = Terminal()

# Functions
def welcome_page():
	font = Figlet(font='standard')
	print(colored(font.renderText('Welcome to the Cryptocurrency Database'), 'blue'))
    
	click.pause()
	click.clear()

def reset_screen():
	print(t.clear())
	font = Figlet(font='standard')
	print(colored(font.renderText('The Cryptocurrency Database'), 'blue'))
	
def reset_sub_screen(coin):
	my_text = pyfiglet.figlet_format(coin, font = 'standard')
	print(my_text)

def list_currencies():
	for table, in tables:
		print(table)

def view_highs(current_coin):
	font = Figlet(font='standard')
	print(colored(font.renderText('Daily High'), 'blue'))
	cur.execute(f"SELECT date, high FROM {current_coin};")
	print("\tdate\t\t\t|\thigh")
	print("--------------------------------------------------------")
	for (date, high) in cur:
		print("{}\t\t|\t{}".format(date, high))
	
	click.pause()
	click.clear()

def view_lows(current_coin):
	font = Figlet(font='standard')
	print(colored(font.renderText('Daily Low'), 'blue'))
	cur.execute(f"SELECT date, low FROM {current_coin};")
	print("\tdate\t\t\t|\tlow")
	print("--------------------------------------------------------")
	for (date, low) in cur:
		print("{}\t\t|\t{}".format(date, low))
	click.pause()
	click.clear()
		
def view_open(current_coin):
	font = Figlet(font='standard')
	print(colored(font.renderText('Opening Value'), 'blue'))
	cur.execute(f"SELECT date, open FROM {current_coin};")
	print("\tdate\t\t\t|\topening value")
	print("-------------------------------------------------------------")
	for (date, open) in cur:
		print("{}\t\t|\t{}".format(date, open))
	click.pause()
	click.clear()

def view_close(current_coin):
	font = Figlet(font='standard')
	print(colored(font.renderText('Closing Value'), 'blue'))
	cur.execute(f"SELECT date, close FROM {current_coin};")
	print("\tdate\t\t\t|\tclosing value")
	print("-------------------------------------------------------------")
	for (date, close) in cur:
		print("{}\t\t|\t{}".format(date, close))
	click.pause()
	click.clear()
	
def view_volume(current_coin):
	font = Figlet(font='standard')
	print(colored(font.renderText('Volume'), 'blue'))
	cur.execute(f"SELECT date, volume FROM {current_coin};")
	print("\tdate\t\t\t|\tvolume")
	print("--------------------------------------------------------")
	for (date, volume) in cur:
		print("{}\t\t|\t{}".format(date, volume))
	click.pause()
	click.clear()
	
def view_cap(current_coin):
	font = Figlet(font='standard')
	print(colored(font.renderText('Marketcap'), 'blue'))
	cur.execute(f"SELECT date, mcap FROM {current_coin};")
	print("\tdate\t\t\t|\tmarketcap")
	print("-------------------------------------------------------------")
	for (date, mcap) in cur:
		print("{}\t\t|\t{}".format(date, mcap))	
	click.pause()
	click.clear()

def get_avg(current_coin):
	font = Figlet(font='standard')
	print(colored(font.renderText('Average Price'), 'blue'))
	cur.execute(f"SELECT AVG(close) FROM {current_coin};")
	print(f"Average volume of {current_coin} = ${cur.fetchall()[0][0]}\n")
	click.pause()
	click.clear()

def get_avg_volume(current_coin):
	font = Figlet(font='standard')
	print(colored(font.renderText('Average Volume'), 'blue'))
	cur.execute(f"SELECT AVG(volume) FROM {current_coin};")
	print(f"Average daily volume of {current_coin} =  ${cur.fetchall()[0][0]}\n")
	click.pause()
	click.clear()

def get_max_market_cap(current_coin):
	font = Figlet(font='standard')
	print(colored(font.renderText('Max Market Capitalization'), 'blue'))
	cur.execute(f"SELECT MAX(mcap) FROM {current_coin};")
	print(f"Biggest Market Capitalization of {current_coin} = ${cur.fetchall()[0][0]}\n")
	click.pause()
	click.clear()

def view_help():
	font = Figlet(font='standard')
	print(colored(font.renderText('User Help'), 'blue'))
	print(t.bold + "Highs" + t.normal + " - Represents the highest value of the coin on the specified date\n" + t.bold + "Lows" + t.normal + " - Represents the lowest value of the coin on the specified date\n" + t.bold + "Opening Value" + t.normal + " - Represents the opening value of the coin on the specified date\n" + t.bold + "Closing Value" + t.normal + " - Represents the closing value of the coin on the specified date\n" + t.bold + "Volume of Transactions" + t.normal + " - Represents the volume of transactions in USD on the specified date\n" + t.bold + "Marketcap" + t.normal + " - Represents the marketcap of the coin on the specified date\n")
	click.pause()
	click.clear()

def sub_menu_show(coin):
	print(t.clear())

	selection_sub_menu = ["[1] Highs", "[2] Lows", "[3] Opening Values", "[4] Closing Values", "[5] Volume of Transactions", "[6] Marketcap of Coin", "[7] Calculate Average Price", "[8] Calculate Average Volume", "[9] Calculate Biggest Market Capitalization", "[h] Help", "[q] Return to Main Menu"]

	sub_menu = TerminalMenu(selection_sub_menu)

	my_return = False

	while my_return == False:
		reset_sub_screen(coin)
		selection_sub_index = sub_menu.show()
		selection_choice = selection_sub_menu[selection_sub_index]

		if (selection_choice == "[q] Return to Main Menu"):
			print(t.clear())
			my_return = True
		if (selection_choice == "[1] Highs"):
			print(t.clear())
			view_highs(coin)
		if (selection_choice == "[2] Lows"):
			print(t.clear())
			view_lows(coin)
		if (selection_choice == "[3] Opening Values"):
			print(t.clear())
			view_open(coin)
		if (selection_choice == "[4] Closing Values"):
			print(t.clear())
			view_close(coin)
		if (selection_choice == "[5] Volume of Transactions"):
			print(t.clear())
			view_volume(coin)
		if (selection_choice == "[6] Marketcap of Coin"):
			print(t.clear())
			view_cap(coin)
		if (selection_choice == "[7] Calculate Average Price"):
			print(t.clear())
			get_avg(coin)
		if (selection_choice == "[8] Calculate Average Volume"):
			print(t.clear())
			get_avg_volume(coin)
		if (selection_choice == "[9] Calculate Biggest Market Capitalization"):
			print(t.clear())
			get_max_market_cap(coin)
		elif (selection_choice == "[h] Help"):
			print(t.clear())
			view_help()


# Menu Creation
selection_menu = ["[a] Aave", "[b] Binance Coin", "[c] Bitcoin", "[d] Cardano", "[e] Chain Link","[f] Cosmos", "[g] Cryptocom Coin", "[h] Dogecoin", "[i] EOS", "[j] Ethereum", "[k] Iota", "[l] Litecoin", "[m] Monero", "[n] NEM", "[o] Polkadot", "[p] Solana", "[r] Stellar", "[s] Tether", "[t] Tron", "[u] Uniswap", "[v] USD Coin", "[w] Wrapped Bitcoin", "[x] XRP", "[q] Quit"]

main_menu = TerminalMenu(selection_menu)

quit = False

welcome_page()

while quit == False:
	reset_screen()

	selection_index = main_menu.show()

	selection_choice = selection_menu[selection_index]

	if (selection_choice == "[q] Quit"):
		print(t.clear())
		quit = True
	if (selection_choice == "[a] Aave"):
		sub_menu_show("aave")
	if (selection_choice == "[b] Binance Coin"):
		sub_menu_show("binancecoin")
	if (selection_choice == "[c] Bitcoin"):
		sub_menu_show("bitcoin")
	if (selection_choice == "[d] Cardano"):
		sub_menu_show("cardano")
	if (selection_choice == "[e] Chain Link"):
		sub_menu_show("chainlink")
	if (selection_choice == "[f] Cosmos"):
		sub_menu_show("cosmos")
	if (selection_choice == "[g] Cryptocom Coin"):
		sub_menu_show("cryptocomcoin")
	if (selection_choice == "[h] Dogecoin"):
		sub_menu_show("dogecoin")
	if (selection_choice == "[i] EOS"):
		sub_menu_show("eos")
	if (selection_choice == "[j] Ethereum"):
		sub_menu_show("ethereum")
	if (selection_choice == "[k] Iota"):
		sub_menu_show("iota")
	if (selection_choice == "[l] Litecoin"):
		sub_menu_show("litecoin")
	if (selection_choice == "[m] Monero"):
		sub_menu_show("monero")
	if (selection_choice == "[n] NEM"):
		sub_menu_show("nem")
	if (selection_choice == "[o] Polkadot"):
		sub_menu_show("polkadot")
	if (selection_choice == "[p] Solana"):
		sub_menu_show("solana")
	if (selection_choice == "[r] Stellar"):
		sub_menu_show("stellar")
	if (selection_choice == "[s] Tether"):
		sub_menu_show("tether")
	if (selection_choice == "[t] Tron"):
		sub_menu_show("tron")
	if (selection_choice == "[u] Uniswap"):
		sub_menu_show("uniswap")
	if (selection_choice == "[v] USD Coin"):
		sub_menu_show("usdcoin")
	if (selection_choice == "[w] Wrapped Bitcoin"):
		sub_menu_show("wrappedbitcoin")
	elif (selection_choice == "[x] XRP"):
		sub_menu_show("xrp")


