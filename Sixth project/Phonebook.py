def view_contacts(contacts):
    print("\n"+"-"*15,"view contacts","-"*15)
    print("")
    num = 1
    for i in contacts:
        print("{0} {1:^38} {2}".format(num, i[0],i[1]))
        num += 1
    
    
    print("\n"+"-"*46+"\n")
    
def add_contact(contacts):
    print("\n-"+"-"*15,"add contacts","-"*15)
    print("")
    contact_name = input("Enter Contact Name: ")
    contact_num = input("\nEnter Contact Number: ")
    
    contacts.append((contact_name,contact_num))
    
    print("\n",contact_name," - ",contact_num," Has been added to contacts\n",sep="")
    
    print("-"*46+"\n")
    
def delete_contact(contacts):
    print("\n"+"-"*15,"delete contact","-"*15)
    print("")
    delete_select = int(input("Enter contact number you would like to delete: "))
    idchecker = 0
    
    for i in range(1,len(contacts)+1):
        if delete_select == i:
            print("\n",contacts[i-1]," Has been deleted from contacts",sep="")
            contacts.pop(i-1)
            idchecker = 0
            
            break
        else:
            idchecker = 1
    if idchecker == 1:
        print("\nCould not find the contact")
    print("\n"+"-"*46)
    
def main(contacts=[('Stish','123'),('Rita','321')]):
    theswitch = 1
    
    while theswitch == 1:
        input_select = input("Select an operation: \nv: view contacts \na: add contacts \nd: delete contacts \nq: quit \n")
        if input_select == "v":
            view_contacts(contacts)
        elif input_select == "a":
            add_contact(contacts)
        elif input_select == "d":
            delete_contact(contacts)
        elif input_select == "q":
            print("\nProgram Closed Successfully")
            theswitch = 0
        else:
            print("\nPlease input a valid Operation\n")

if __name__ == "__main__":
    main()