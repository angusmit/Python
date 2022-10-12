# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.

# solution 1
#x = 121
#x = str(x)
# observe the sequence between each of the indices of the number
# validate each digit all indicies from left to right and right to left 
#x[0] == x[-1]
#x[1] == x[-2]
def isPalindrome(x):
    h=[]
    for i in range(len(x)-1):
        h.append(x[i] == x[-i-1])
    return (all(h))

# solution 2
def isPalindrome(x):
    return str(x) == str(x)[::-1]

# solution 3
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    xl = list(str(x))
    n = len(xl)
    if n == 1:
        return True
    k = int(n / 2)
    a = xl[:k]
    b = xl[-k:]
    b.reverse()
    if n % 2 == 0:
        return a == b
    else:
        return a == b



# solution 4
# without using converting integers to strings
def isPalindrome(x):
    if x < 0 or x % 10 == 0:
        return False  
    reverted_number = 0
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        x = x // 10
    return  x == reverted_number or x == reverted_number // 10