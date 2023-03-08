ok = input("input number")

def digitcal(intger):
    eventotal = 0
    oddtotal = 0
    zerocounter = 0
    for i in str(intger):
        if int(i) % 2 == 0:
            eventotal = eventotal + 1
            if int(i) == 0:
                zerocounter = zerocounter + 1
        else:
            oddtotal = oddtotal + 1
            
    print(eventotal,"Even numbers")
    print(oddtotal,"Odd numbers")
    print(zerocounter,"Zero's")

    
digitcal(ok)