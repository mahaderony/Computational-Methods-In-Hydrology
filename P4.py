# Problem 4
import statistics
l = int(input('enter the lower number'))
h = int(input('enter the higher number'))
m = 1
a = []
mean = 0
if l % 2 == 0:
    print('The lower number is even, multiplying all even numbers in the range')
    for l in range(l, h + 1, 2):  # (start, stop, increment)
        m = int(l * m)
else:
    print('The lower number is odd, Creating the average of all numbers')
    for l in range(l, h + 1, 1):
        a.append(l)  # assigning value in array a
    mean = float(statistics.mean(a))
if m > 1:
    print(m)
else:
    print(mean)
