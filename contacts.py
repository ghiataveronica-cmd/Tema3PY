contacts={
    "Ana": {"Phone":"0722000001","email": "anitagigilove@yahoo.com"},
    "Mihai": {"Phone":"0722000002","email": "mihai@gmail.com"},
}

def ListContacts():
    print(f"{'Name':<10}{'Phone':<15}{'Email':>5}")
    for name in contacts:
        print(f"{name:<10}{contacts[name]['Phone']:<15}{contacts[name]['email']:>5}")

def AddContacts():
    name=input("Plese enter the name:")
    phoneNumber=input("Please enter the phone number:")
    email=input("Please enter the email:")
    if name in contacts:
        print("Do you want to overwrite?\n1.YES\n2.NO")
        choice=input("What do you want to do?\n")
        match choice:
            case "1":
                contacts[name]["Phone"]=phoneNumber
                contacts[name]["email"]=email
            case "2":
                return
            case _:
                print("Invalid choice")
    else:
        contacts[name]={"Phone":phoneNumber,"email":email}


def SearchByName():
    searched=input("🔍:")
    for name in contacts:
        if searched.lower()==name.lower():
            print(contacts[name])
            return
    print("Contacts not found!")

def DeleteContact():
    wantToDelete=input("Who do you want to delete?:\n")
    if wantToDelete not in contacts:
        print("No one was found with this name!")
    else:
        contacts.pop(wantToDelete)
        print(f"{wantToDelete} was deleted!")


while True:
    print("1.List contacts\n2.Add contact\n3.Search by name\n4.Delete contact\n5.Quit")
    value=input("What do you wanna do??:\n")
    match value:
        case "1":
            ListContacts()
        case "2":
            AddContacts()
        case "3":
            SearchByName()
        case "4":
            DeleteContact()
        case "5" | "Quit" | "quit":
            print("Bye")
            break
        case _:
            print("Invalid choice!")