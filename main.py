napoje = [
    {
        "nazwa": "pepsi",
        "cena": 3.50,
        "qnty": 12
    },
    {
        "nazwa": "cola",
        "cena": 3.80,
        "qnty": 9
    },
    {
        "nazwa": "fanta",
        "cena": 3.40,
        "qnty": 16
    },
    {
        "nazwa": "ice-tea",
        "cena": 2.90,
        "qnty": 13
    },
    {
        "nazwa": "sprite",
        "cena": 3.70,
        "qnty": 10
    }
]

print("0 - pepsi")
print("1 - cola ")
print("2 - fanta")
print("3 - ice-tea")
print("4 - sprite")

while True:

    pieniadze = float(input("Wrzuć odpowiednią sume."))
    wybor = int(input("Wybierz jaki napój chcesz."))

    if wybor == 0:
        reszta = pieniadze - napoje[0]["cena"]
        if reszta < 0:
            print("Not enough")
            insert_money = float(input("Insert more money"))
            pieniadze += insert_money
        print("Here is your Pepsi")
        print(f"Here is your change: {reszta:.2f}")


    elif wybor == 1:
        reszta = pieniadze - napoje[1]["cena"]
        if reszta < 0:
            print("Not enough")
            insert_money = float(input("Insert more money"))
            pieniadze += insert_money
        print("Here is your Cola")
        print(f"Here is your change: {reszta:.2f}")


    elif wybor == 2:
        reszta = pieniadze - napoje[2]["cena"]
        if reszta < 0:
            print("Not enough")
            insert_money = float(input("Insert more money"))
            pieniadze += insert_money
        print("Here is your Fanta")
        print(f"Here is your change: {reszta:.2f}")


    elif wybor == 3:
        reszta = pieniadze - napoje[3]["cena"]
        if reszta < 0:
            print("Not enough")
            insert_money = float(input("Insert more money"))
            pieniadze += insert_money
        print("Here is your Ice-tea")
        print(f"Here is your change: {reszta:.2f}")


    elif wybor == 4:
        reszta = pieniadze - napoje[4]["cena"]
        if reszta < 0:
            print("Not enough")
            insert_money = float(input("Insert more money"))
            pieniadze += insert_money
        print("Here is your Sprite")
        print(f"Here is your change: {reszta:.2f}")