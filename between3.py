def between3(somestring):
  target = ">"
  for char in somestring:
    target = target + char + "<"
  print target