from tkinter import *
import requests
import json
import sqlite3

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap("favicon.ico")

con = sqlite3.connect('crypto.db')
cursorObj = con.cursor()
cursorObj.execute("CREATE TABLE IF NOT EXISTS crypto(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)")
con.commit()

cursorObj.execute("INSERT INTO crypto VALUES(1, 'BTC', 2, 3200)")
con.commit()


def font_color(amout):
    if amout >= 0:
      return "green"
    else:
      return "red"


def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=e856bbd3-c1b5-4e52-859f-a12c095b722b")
    api = json.loads(api_request.content)

    coins = [
      {
        "symbol": "BTC",
        "amount_owned": 2,
        "price_per_coin": 3200
      },
      {
        "symbol": "SOL",
        "amount_owned": 100,
        "price_per_coin": 2.05
      },
      {
        "symbol": "ETH",
        "amount_owned": 5,
        "price_per_coin": 1000
      },
      {
        "symbol": "XMP",
        "amount_owned": 10,
        "price_per_coin": 400.05
      },
      {
        "symbol": "USDT",
        "amount_owned": 75,
        "price_per_coin": 1
      }
    ]

    total_pl = 0
    coin_row = 1
    total_current_value = 0

    for i in range(0, 300):
      for coin in coins:
        if api["data"][i]["symbol"] == coin["symbol"]:
          total_paid = coin["amount_owned"] * coin["price_per_coin"]
          current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
          pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
          total_plpercoin = pl_percoin * coin["amount_owned"]

          total_pl = total_pl + total_plpercoin
          total_current_value = total_current_value + current_value

          name = Label(pycrypto, text=api["data"][i]["symbol"], bg="#F3F4F6", fg="black", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
          name.grid(row=coin_row, column=0, sticky=N+S+E+W)

          price = Label(pycrypto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6", fg="black", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
          price.grid(row=coin_row, column=1, sticky=N+S+E+W)

          no_coins = Label(pycrypto, text=coin["amount_owned"], bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, padx="2", pady="2", relief="groove")
          no_coins.grid(row=coin_row, column=2, sticky=N+S+E+W)

          amount_paid = Label(pycrypto, text="${0:.2f}".format(total_paid), bg="#F3F4F6", fg="black",  font="Lato 12", borderwidth=2, padx="2", pady="2", relief="groove")
          amount_paid.grid(row=coin_row, column=3, sticky=N+S+E+W)

          current_val = Label(pycrypto, text="${0:.2f}".format(current_value), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(current_value))), font="Lato 12", borderwidth=2, padx="2", pady="2", relief="groove")
          current_val.grid(row=coin_row, column=4, sticky=N+S+E+W)

          pl_coin = Label(pycrypto, text="${0:.2f}".format(pl_percoin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(pl_percoin))), font="Lato 12", borderwidth=2, padx="2", pady="2", relief="groove")
          pl_coin.grid(row=coin_row, column=5, sticky=N+S+E+W)

          totalpl = Label(pycrypto, text="${0:.2f}".format(total_plpercoin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_plpercoin))), font="Lato 12", borderwidth=2, padx="2", pady="2", relief="groove")
          totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)

          coin_row = coin_row + 1

    totalcv = Label(pycrypto, text="${0:.2f}".format(total_current_value), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, padx="2", pady="2", relief="groove")
    totalcv.grid(row=coin_row, column=4, sticky=N+S+E+W)

    totalpl = Label(pycrypto, text="${0:.2f}".format(total_pl), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_plpercoin))), font="Lato 12", borderwidth=2, padx="2", pady="2", relief="groove")
    totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)

    api = ""

    update = Button(pycrypto, text="Update", bg="#142E54", fg="white", command=my_portfolio, font="Lato 12", borderwidth=2, padx="2", pady="2", relief="groove")
    update.grid(row=coin_row + 1, column=6, sticky=N+S+E+W)


name = Label(pycrypto, text="Coin Name", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycrypto, text="Price", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
price.grid(row=0, column=1, sticky=N+S+E+W)

no_coins = Label(pycrypto, text="Number of Coins", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
no_coins.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pycrypto, text="Total Amout Paid", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_val = Label(pycrypto, text="Current Value", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
current_val.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(pycrypto, text="P/L per Coin", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

totalpl = Label(pycrypto, text="Total P/L woth coin", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
totalpl.grid(row=0, column=6, sticky=N+S+E+W)


my_portfolio()
pycrypto.mainloop()

cursorObj.close()
con.close()

print("Program Completed")