alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesen(text, shift, dir):
  textt = ""

  if dir == 'de':
    shift *= -1
    
  for i in text:
    pos = alphabet.index(i)

    new_pos = pos + shift
    textt += alphabet[new_pos]

  print(f"The {dir} text is {textt}")
  

dir = input("Type encode to encypt and decode to decrypt: ")
text = input("Type your message: ").lower()
shift = int (input("Type shift num: "))

caesen(text, shift, dir)
