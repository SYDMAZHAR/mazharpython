def fibonacci_series(n):
    fib_series = [0, 1]
    while fib_series[-1] + fib_series[-2] <= n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

upper_limit = 50
fibonacci_result = fibonacci_series(upper_limit)
print("Fibonacci series up to", upper_limit, ":", fibonacci_result)



def reverse_word(word):
    return word[::-1]

user_input = input("Enter a word: ")
reversed_word = reverse_word(user_input)
print("Reversed word:", reversed_word)



numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
