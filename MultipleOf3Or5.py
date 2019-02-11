natural_numbers = int(input('Enter number till which you need a natual numbers'))
sum = 0
for i in range(1, natural_numbers):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
        print(i)

print('The Sum of multiple of 3 or 5 from 0 till  {0} is {1} '.format(natural_numbers, sum))
