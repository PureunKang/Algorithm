def solution(s, n):
    password = []
    
    for char in s: 
        if char.isupper():
            new_char = chr((ord(char) - ord('A') + n)%26 + ord('A'))
        elif char.islower():
            new_char = chr((ord(char) - ord('a')+n)%26 + ord('a'))
        else:
            new_char = char
        password.append(new_char)
        
    return ''.join(password)