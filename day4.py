# Calculates total possible passwords within 124075-580769

# Criteria:
# 6 digit
# Two adjacent digits are same (122345)
# Digits never decrease (111123 or 134679)
# Cannot be three adjacent digits

low = 272091
high = 815432

password_test = [111111, 223450, 122345, 111123, 135679, 112233, 123444, 111122, 111233]
password_results = [True, False, True, True, False, True, False, True, True]

def double_digits(password):
    password = str(password)
    if len(password) == 2:
        if password[0] == password[1]:
            return True
    else:
        if double_digits(password[:2]):
            return True
        return double_digits(password[1:])
    return False

def increasing_digits(password):
    password = str(password)
    test = [False] * 5
    for n in range(5):
        if password[n] <= password[n+1]:
            test[n] = True
    result = sum([1 for n in test if n])
    if result == 5:
        return True
    else:
        return False

def counting_digits(password):
    check = [False] * 10
    password = str(password)
    count = 0
    for n in range(10):
        n = str(n)
        num = password.count(n)
        if num == 2:
            check[count] = True
    result = sum([1 for n in check if n])
    if result >= 1:
        return True
    return False

# count = 0
# for test in password_test:
#     result = double_digits(test)
#     if result != password_results[count]:
#         print('Error with %i' % (test))
#         print('Result was %s, but expected %s' % (result, password_results[count])) 
#     count += 1


count = 0
#nums = []
for password in range(low, high+1):
    if increasing_digits(password):
        if counting_digits(password):
            if double_digits(password):
                count +=1
            #nums.append(password)
print(count)
#print(nums)