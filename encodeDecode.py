def encode(string,keyletters):
  alpha="abcdefghijklmnopqrstuvwxyz"
  secret = ""
  for letter in string:
    index = alpha.find(letter)
    secret = secret+keyletters[index]
  print secret

def decode(secret,keyletters):
  alpha="abcdefghijklmnopqrstuvwxyz"
  clear = ""
  for letter in secret:
    index = keyletters.find(letter)
    clear = clear+alpha[index]
  print clear