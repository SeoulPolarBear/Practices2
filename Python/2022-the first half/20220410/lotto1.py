import random

def get_random_number():
    number = random.randint(1,45)#1과 45 포함
    return number

lotto_num = []
count = 0

while True:
    if count >5:
        break
    
    random_number = get_random_number()
    
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1
    else:
        continue

lotto_num.sort()
for num in lotto_num:
    print(num, end = " ")
    