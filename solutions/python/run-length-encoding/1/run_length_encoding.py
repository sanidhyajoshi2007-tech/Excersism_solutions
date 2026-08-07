def decode(string):
    decoded_string = ""
    i = 0
    num = ""

    while i < len(string):
        if string[i].isdigit():
            num += string[i]

        else:
            if num == "":
                decoded_string += string[i]
            else:
                decoded_string += int(num) * string[i]
            num = ""

        i += 1

    return decoded_string


def encode(string):
    encoded_string = ""
    i = 0

    while i < len(string):
        count = 1

        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1

        if count == 1:
            encoded_string += string[i]
        else:
            encoded_string += f"{count}{string[i]}"

        i += 1

    return encoded_string