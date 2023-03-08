name = input("Hello and welcome to generic bank . What is your name? ")
on_off = 0
balance = 1000
while on_off !=-1:
    on_off = input("""What service do you require? Please enter any of the following
                   Withdraw
                   Deposit
                   Balance
                    Quit\n""").lower()
    if on_off == "withdraw":
        calculating_withdraw = int(input("How much would you like to withdraw? "))
        if calculating_withdraw >= balance:
            print("Insufficent Balance")
        else:
            balance =  balance - calculating_withdraw
            print("Please wait a moment.... Your new balance is", balance)
    if on_off == "deposit":
        calculating_deposit = int(input("How much you like to deposit? "))
        balance = calculating_deposit + balance
        print("Depositing amount please wait a moment.... Your new balance is", balance)
    if on_off == "balance":
        print("Your current balance is", balance)
    if on_off == "quit":
        on_off = -1
print("Thanks for banking with us today", name)        