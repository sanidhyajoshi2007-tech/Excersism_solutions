def is_pangram(sentence):
    text=[chr(i) for i in range(ord("a"),ord("z")+1)]
    for char in text:
        if char not in sentence.lower():
            return False
    return True
            
            
 
    
