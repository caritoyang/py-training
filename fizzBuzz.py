for i in range(1,100):
    print(((''if i%3 else 'fizz') + (''if i%5 else 'buzz')) or i)