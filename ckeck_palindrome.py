def palindromes(input_string):
    store_strg = []
    n = len(input_string)
    for i in range(n):
        for j in range(i+1, n+1):
            newstring = input_string[i:j]
            if newstring == newstring[::-1] and len(newstring) > 1:
                store_strg.append(newstring)
    return store_strg
