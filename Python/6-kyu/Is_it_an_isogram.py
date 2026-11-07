def is_isogram(word: str) -> bool:
    lower_words = word.lower()
    for i in lower_words :
        if i.isalpha() == False :
            return False
        else :
            if lower_words.count(i) > 1 :
                return False
            else:
                return True
        
        

print(is_isogram("moOse"))
