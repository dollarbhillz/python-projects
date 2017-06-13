def ordOfString(string):
  """figures out the ord value of a string"""
  n = 0
  for char in string:
    n+= ord(char)
  return n