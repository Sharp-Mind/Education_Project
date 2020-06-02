with open('004.txt', 'r') as file:
    file.seek(0)
    lines = file.readlines()

for i in range(len(lines)):
    if 'one' in lines[i].lower():
        lines[i] = lines[i].lower().replace('one', 'один'.capitalize())
    elif 'two' in lines[i].lower():
        lines[i] = lines[i].lower().replace('two', 'два'.capitalize())
    elif 'three' in lines[i].lower():
        lines[i] = lines[i].lower().replace('three', 'три'.capitalize())
    elif 'four' in lines[i].lower():
        lines[i] = lines[i].lower().replace('four', 'четыре'.capitalize())

with open('004_out.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)
