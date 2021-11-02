# fizzbuzz using list comprehension (easy)
fizzbuzz = ['fizzbuzz' if v%3 == 0 and v%5 == 0 else 'fizz' if v % 3 == 0 else 'buzz' if v % 5 == 0 else v for v in range(1, 51)]
print('First way\n',fizzbuzz)

# fizzbuzz using list comprehension (intermediate) from github
fizzbuzz = ["Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in range(1, 51)]
print('\n Second way\n',fizzbuzz)

# fizzbuzz using lambda -(intermediate) from github
fizzbuzz = list(map(lambda i: "Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i), range(1,51)))
print('\n Third way\n', fizzbuzz)
