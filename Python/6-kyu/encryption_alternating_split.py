"""
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
"""

# My Solution :

def decrypt(encrypted_text, n):
    result = encrypted_text

    if result == None :
        return None
    if result == "":
        return ""
    else:
        for i in range(n):
            flag = ""
            mid = len(result) // 2
            even = result[:mid]
            odd = result[mid:]
            for i in range(len(even)):
                flag += odd[i]
                flag += even[i]

            flag += odd[len(even):]
            result = flag
        return result

def encrypt(text, n):
    result = text
    if result == None :
            return None
    if result == "":
        return ""
    else:
        for i in range(n):
            odd = ""
            even = ""
            for index, words in enumerate(result, start=1):
                if index % 2 == 0:
                    even += words
                else :
                    odd += words

            result = even + odd

        return result

print(decrypt("hsi  etTi sats!", 1))
print(encrypt("This is a test!", 2))