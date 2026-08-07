def find_anagrams(word, candidates):
    word=word.lower()
    anagrams=[]
    for candidate in candidates:
        can= candidate.lower()
        if can!=word and sorted(can)==sorted(word):
            anagrams.append(candidate)
    return anagrams
            
        
