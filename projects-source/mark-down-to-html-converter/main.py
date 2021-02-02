# This will be a markdown to HTML converter

text = "## What is the # matter."
text2 = "[](aaa"
# Evaluate to see if text has heading
def heading(text):
  if text[0] == "#":
    heading_number = 0
    remaining_output = ""
    i = 0
    for i in range(len(text)):
      char = text[i]
      if char == "#":
        heading_number += 1
      else:
        break
    i += 1
    for j in range(i,len(text)):
      char = text[j]
      remaining_output += char
    output = "<h"+str(heading_number)+">"+remaining_output+"</h"+str(heading_number)+">"
    return output
  return ""

def link(string):
  open_p = open_b = close_p = close_b = False
  for i in range(len(string)):
    char = string[i]
    if char == "(":
      open_p = True
    elif char == ")":
      close_p = True
    elif char == "[":
      open_b = True
    elif char == "]":
      close_b = True
  if open_b and close_b and open_p and close_p:
    return True
  return False

print(heading(text))
print(link(text2))