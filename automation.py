import re

# phone_number = r'/^\\(?([0-9]{3})\\)?[-.\\s]?([0-9]{3})[-.\\s]?([0-9]{4})$/'
# email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
list =  []
# file = open('potential-contacts.txt','r')
with open("./potential-contacts.txt")as f:
  text = f.read()

print(text)
# text = file.read()
# pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# pattern = re.compile(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')
# matches = pattern.findall(text)
# for match in matches:
#     print(match)


