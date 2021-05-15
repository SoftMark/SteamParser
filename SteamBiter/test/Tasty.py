# Task 6

def is_simple(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def find_friendly_couples(arrange):
    for number in range(3, arrange - 1, 2):
        if is_simple(number) and is_simple(number + 2):
            print("(", number, "and", number + 2, ")")


# find_friendly_couples(1000)


# Task 7

def NSD(a, b):
    while b > 0:
        n = a % b
        a = b
        b = n
    return a


# a = input("a = ")
# b = input("b = ")
# print("NSD(" + a + ", " + b + ") =", NSD(int(a), int(b)))

# Task 8

def is_coprime_integers(a, b):
    if NSD(a, b) == 1:
        return True
    else: return False


# a = input("a = ")
# b = input("b = ")
#
# if is_coprime_integers(int(a), int(b)):
#     print("Coprime integers!")
# else: print("Not coprime integers!")


# Task 9

print("First fraction")
numerator1 = input("First numerator: ")
denominator1 = input("First denominator: ")
print("\nSecond fraction")
numerator2 = input("Second numerator: ")
denominator2 = input("Second denominator: ")

print("\nExpression:\n" + numerator1 + "/" + denominator1 + " + " + numerator2 + "/" + denominator2 + " = ", end='')
result_denominator = int(denominator1) * int(denominator2)
result_numerator = int(numerator1) * int(denominator2) + int(numerator2) * int(denominator1)
print(str(result_numerator) + "/" + str(result_denominator))