def bank():
    balance = 230
    num = float(input("Deposit: "))

    balance += num
    print(f'Your balance is: {balance}')

bank()