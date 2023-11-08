alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,dir):
  end_text = ""

  if dir == 'de':
    shift *= -1

  for i in text: #text=hello
    if i in alphabet:
      position = alphabet.index(i)
      new_position = position + shift
      end_text += alphabet[new_position]
    else:
      end_text += i

  print(f"Here's the {dir} text is {end_text}")

from art import logo
print(logo)

end = False
while not end:

  dir = input("Type en to encypt and de to decrypt: ")
  text = input("Enter text: ")
  shift = int(input("Type shift num: "))

  shift = shift % 26
  caesar(text,shift,dir)

  restart = input("Type yes 'y' if you wanna continue else 'n' ")
  if restart == 'n':
    end = True
    print('GoodBye')
    
    
    
    
    
    
    
  