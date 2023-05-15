def bank():
    balance = 230
    num = float(input("Deposit: "))

    balance += num
    print(f'Balance: {balance}')

bank()