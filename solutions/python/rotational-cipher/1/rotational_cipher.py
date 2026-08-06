def rotate(text, key):
    result = ""

    for char in text:
        if "a" <= char <= "z":
            rotated = (ord(char) - ord("a") + key) % 26
            result += chr(rotated + ord("a"))

        elif "A" <= char <= "Z":
            rotated = (ord(char) - ord("A") + key) % 26
            result += chr(rotated + ord("A"))

        else:
            result += char

    return result
