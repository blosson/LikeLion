
lunch = ['pizza','hamburger','chicken']

while True:
    item = input('What is your lunch? : ')
    if item == 'q':
        break
    else: 
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)


