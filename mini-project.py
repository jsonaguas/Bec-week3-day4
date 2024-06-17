rolodex = {1:{'name':'John Deer', 'phone':'212-708-2222', 'email':'johndeer@gmail.com'}, 
           2:{'name':'Jane Doe', 'phone':'708-333-5555', 'email':'janedoe@gmail.com'}}

def main():
    while True:
        ans = input('Select option from menu below: ')
        '''
        1. Add a new contact
        2. Edit an existing contact
        3. Delete a contact
        4. Search for a contact
        5. Display all contacts
        6. Export contacts to a text file
        7. Import contacts from a text file
        8. Quit \n
        '''
        if ans == '1':
            add_contact(input('Enter the name: '), input('Enter the phone number: '))
        elif ans == '2':
            edit_contact()
        elif ans == '3':
            delete_contact()
        elif ans == '4':
            search_contact()
        elif ans == '5':
            display_contacts()
        elif ans == '6':
            export_contacts()
        elif ans == '7':
            import_contacts()
        elif ans == '8':
            break 

def add_contact(name, phone, email):
    try:
        rolodex[len(rolodex) + 1] = {'name': name, 'phone': phone, 'email': email}
        print('Contact added')
    except Exception as e:
        print(f'Error adding contact: {e}')

def display_contacts():
    for key in rolodex:
        print(f'{key}: {rolodex[key]["name"]} - {rolodex[key]["phone"]}')

def edit_contact():
    display_contacts()
    contact_id = int(input('Enter the contact ID: '))
    name = input('Enter the new name: ')
    phone = input('Enter the new phone number: ')
    rolodex[contact_id] = {'name':name, 'phone':phone}
    print('Contact updated')

def delete_contact():
    display_contacts()
    contact_id = int(input('Enter the contact ID: '))
    del rolodex[contact_id]
    print('Contact deleted')


def search_contact():
    search_term = input("Enter search term (name, phone, email: ").lower()
    for id, contact in rolodex.items():
        if (search_term in contact['name'].lower() or
            search_term in contact['phone'] or
            search_term in contact['email'].lower() or
            print(f"Found: {contact}"))
            return
    print("No contact found.")


def export_contacts():
    with open('contacts.txt', 'w') as f:
        for key in rolodex:
            f.write(f'{key}: {rolodex[key]["name"]} - {rolodex[key]["phone"]}\n')
    print('Contacts exported')

def import_contacts():
    rolodex.clear()
    with open('contacts.txt', 'r') as f:
        for line in f:
            key, value = line.split(':')
            name, phone = value.split('-')
            rolodex[int(key)] = {'name':name.strip(), 'phone':phone.strip()}
    print('Contacts imported')


main()