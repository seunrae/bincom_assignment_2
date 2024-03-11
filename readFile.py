


name_file = open("/Users/mac/Documents/nameFile.txt", "r");
text = name_file.read().split();
first_name = text[0];
middle_name = text[1];
last_name = text[2];
print("First name: ", first_name);
print("Middle name: ", middle_name);
print("Last name: ", last_name);
print(text)

