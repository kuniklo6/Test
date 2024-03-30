
def hello(n, s):
    for x in range(n):
        print(x + 1, s)

while True:
    try:
        num = int(input('Hoe many times? '))
        break
    except ValueError:
        print('Please enter a whole number')

# print('Your age is: ' + str(age))

#Reference: https://www.easypythondocs.com/validation.html

hello(int(num), "Hello")
# print("Hiya")
# var1 = 4
# print(var1)