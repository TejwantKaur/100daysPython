alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(plain_text,shift):
  cipher_text = ""

  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift
    new_letter = alphabet[new_position]
    cipher_text += new_letter

  print(f"The encoded text is {cipher_text} ")

def decrypt(cipher_text,shift):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift
    new_letter = alphabet[new_position]
    plain_text += new_letter

  print(f"The decoded text is {plain_text}")

end = False
while end is not True:
  direction = input("Type encode to encrypt and decode to decrypt: ").lower()
  text = input("Type your message: ").lower()
  shift = int (input("Type shift num: "))
  
  if direction == 'en':
    encrypt(text,shift)
  elif direction == 'de':
    decrypt(text,shift)
  else:
    print("You wrote incorrect! ")

  cont = input("do you want to continue? Y / N ").lower()
  
  if(cont == 'n'):
    end = True
  elif cont == 'y':
    end = False
  else:
    print("Wrong input!")
  
  
