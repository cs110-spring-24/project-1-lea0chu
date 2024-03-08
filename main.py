def num_input(prompt):
    while True:
        user = input(prompt)
        if user.isdigit() == True:
            return int(user)
        else:
            print("Not a number, try again!")

def encrypt(password, shift):
  user = password
  updated = ""

  for i in range(len(user)):
      curr = user[i]
      curr = ord(curr) + shift
      curr = chr(curr)
      updated += curr
  return updated

def menu():
   print("Options:\n[1] Add a new note\n[2] Remove notes\n[3] View a note\n[4] List all notes\n[5] Exit the program")


def main():
  note = []
  stored_username = "lea0chu" 
  stored_password = encrypt("ihatepython", 2) 
  user = input("Enter your username: ")
  password = input("Enter your password: ")
  if user == stored_username and encrypt(password, 2) == stored_password:
     print("Logged in.")

  while True:
    menu()
    choice = num_input("Enter your choice: ")
    if choice == 1:
      item = input("Enter a new note: ")
      #add(note, item)
    elif choice == 2:
      item = input("Enter an item to remove: ")
     #remove(note, item)
    elif choice == 3:
      print("Viewing a note: {note}")
    elif choice == 4:
      print("Listing all notes: {print_list(note)}")
    elif choice == 5:
      print("Exiting Program..")
      return 
    print()

if __name__ == "__main__":
  # Leave this as is
  main()
  
