import re

# phone_number = r'/^\\(?([0-9]{3})\\)?[-.\\s]?([0-9]{3})[-.\\s]?([0-9]{4})$/'
# email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# file = open('potential-contacts.txt','r')
with open("potential-contacts.txt") as f:
    text_file = f.read()


# print(text)
# r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
# pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
def validate_phone_number():
    match_list = []
    new_list = []
    pattern = re.compile(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
    matches = pattern.findall(text_file)
    for match in matches:
        match_list.append(match)
        #print(match_list)

    for num in match_list:
        if num not in new_list:
            new_list.append(num)
            print(new_list)

    with open('phone_numbers.txt', 'w') as file:
        for number in new_list:
            file.write(str(number))
            file.write('\n')




def validate_email():
    match_list = []
    new_list = []
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    matches = pattern.findall(text_file)
    for match in matches:
        match_list.append(match)
        # print(match_list)

    for text in match_list:
        if text not in new_list:
            new_list.append(text)

    with open('emails.txt', 'w') as file:
        for text in new_list:
            file.write(str(text))
            file.write('\n')

    # print(new_list)


validate_email()
validate_phone_number()
