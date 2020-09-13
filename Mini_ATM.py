print("""Welcome to Mini-ATM
Choose the Transaction
1. Balance
2. Deposit
3. Withdraw
4. Exit """)
balance=3000
while True:
    i=int(input('Enter your transaction :'))
    if(i==1):
        print('Your balance :',balance)
        aTrans=input('Do want to continue Y/N: ')
        if(aTrans=='Y' or aTrans=='y'):
            continue
        else:
            print('"Thank you for using Mini-ATM"')
            break
    elif(i==2):
        deposit=float(input('Enter Amout :'))
        total=balance+deposit
        print(' Your balance :',total)
    elif(i==3):
        Twithdraw=int(input('Enter amount :'))
        withdraw=balance-Twithdraw
        print('Available balance ',withdraw)
    elif(i==4):
        print('Transaction Exit')
        exit()
    else:
        print('"Invalid transaction" \n"Please enter correct transaction"')
