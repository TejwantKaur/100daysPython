alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type encode to encypt and decode to decrypt: ")
text = input("Type your message: ").lower()
shift = int (input("Type shift num: "))

def encrypt(text,shift):
  cipher_text = ""
  
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    new_letter = alphabet[new_position]
    cipher_text += new_letter
    
  print(f"The encoded text is {cipher_text} ")

encrypt(text,shift)
