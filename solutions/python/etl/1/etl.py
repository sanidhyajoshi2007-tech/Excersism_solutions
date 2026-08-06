def transform(legacy_data):
    update_data={}
    for score,letters in legacy_data.items():
         for letter in letters:
             update_data[letter.lower()]=score
    return update_data
