def cypher(word, shift, direction="encrypt"):
  word_array = list(word)
  if direction == "encrypt":
    for i in range(len(word)):
      char = word_array[i]
      new_char = ord(char)+shift
      if new_char <= ord('z'):
        word_array[i] = chr(new_char)
      else:
        remain = new_char%ord('z')-1
        word_array[i] = chr(ord('a')+remain)
  elif direction == "decrypt":
    for i in range(len(word)):
      new_char = ord(word[i])-shift
      if new_char >= ord('a'):
        word_array[i] = chr(new_char)
      else:
        remain = new_char-ord('a')+1
        word_array[i] = chr(ord('z')+remain)
  return "".join(word_array)

print(cypher("bkr", 2, "decrypt"))