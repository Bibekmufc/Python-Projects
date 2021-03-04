number = 10

def check(number):
    a = 0
    for i in range(1,11):
        a = number%i
        if a: break
    return a

while True:
    number += 2
    result = check(number)
    if result:
        continue
    else: 
        print(number)
        break
    