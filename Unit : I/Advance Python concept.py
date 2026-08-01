#Advance Python concept
def triple_output(func):
    def wrapper():
        return func() * 3
    return wrapper


def even_numbers(n):
    # yields even numbers from 2 to n
    i = 2
    while i <= n:
        yield i
        i += 2


@triple_output
def sum_evens():
    return sum(even_numbers(6))


print("Result:", sum_evens())

#Output
'''Result : 36'''