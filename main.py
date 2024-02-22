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
  # TODO Print out a menu of options for the user
  # TODO Delete the pass after writing your implementation
  pass

def main():
  stored_username = "john" # fill in your own here
  stored_password = encrypt("super safe password", 2) # fill in your own super safe password here

  # TODO Your implementation goes here


if __name__ == "__main__":
  # Leave this as is
  main()
  
