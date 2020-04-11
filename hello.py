
c = 200
def add(a, b):
    c = 45
    total = a + b
    return total

x=10
y=10

def substract(a, b):
    diff = a - b
    return diff

#Variables: integer, decimal(float), string, character, boolean 
#Function, Variable

#Collection of values

def add_list(nums):
    total = 0
    for number in nums:
        total = total + number
    return total

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 0, 2,6]
total = add_list(arr)
print(total)

arr = [10, 20]
total = add_list(arr)
print(total)

arr = [10]
total = add_list(arr)
print(total)


arr = []
total = add_list(arr)
print(total)



total = add(10, 20)
print(total)


