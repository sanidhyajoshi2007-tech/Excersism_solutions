def is_isogram(phrase):
    test =[]
    for char in phrase.lower():
        if char.isalpha():
            test.append(char)
    test_1=set(test)
    return len(test)==len(test_1)
            
        
