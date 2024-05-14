#count all palindrome sub string in a given string. Length of palindrome sub string is greater than or equal to 2
def count_palindromes(s):
    count = 0
    palindromes = []
    n = len(s)
    
    # Helper function to check if a substring is a palindrome
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    # Iterate through all substrings of length 2 or more
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                count += 1
                palindromes.append(substring)
    
    print("Palindromic substrings:", palindromes)
    return count

# Test the function
input_string = "abcbabcdcbd"
print("Number of palindrome substrings:", count_palindromes(input_string))
