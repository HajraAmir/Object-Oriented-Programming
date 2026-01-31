def sum_even_recursive(n):
    if n == 0:
        return 0
    return 2 * n + sum_even_recursive(n - 1)

print("Recursive Sum of first N even numbers")
print(sum_even_recursive(1))  
print(sum_even_recursive(2))  
print(sum_even_recursive(5))  
def harmonic_sum_recursive(n):
    if n == 1:
        return 1
    return 1 / n + harmonic_sum_recursive(n - 1)


print("Recursive Harmonic Sum")
print(harmonic_sum_recursive(1))  
print(harmonic_sum_recursive(2))  
print(harmonic_sum_recursive(5))  
def arithmetic_sequence_recursive(a1, d, n):
    if n == 1:
        return a1
    return d + arithmetic_sequence_recursive(a1, d, n - 1)


print("Recursive Arithmetic Sequence")
print(arithmetic_sequence_recursive(1, 2, 1))  
print(arithmetic_sequence_recursive(1, 2, 2)) 
print(arithmetic_sequence_recursive(1, 2, 5))  

def binomial_coefficient_recursive(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient_recursive(n - 1, k - 1) + binomial_coefficient_recursive(n - 1, k)


print("Recursive Binomial Coefficient")
print(binomial_coefficient_recursive(5, 2)) 
print(binomial_coefficient_recursive(6, 3))  
print(binomial_coefficient_recursive(7, 4))  
def reverse_number_recursive(n, result=0):
    if n == 0:
        return result
    return reverse_number_recursive(n // 10, result * 10 + n % 10)

print("Recursive Reverse of a Number")
print(reverse_number_recursive(123769))  
print(reverse_number_recursive(456))     
print(reverse_number_recursive(1001))   