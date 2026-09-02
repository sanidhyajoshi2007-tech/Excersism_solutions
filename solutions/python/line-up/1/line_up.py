def line_up(name, number):
    number = str(number)

    if number.endswith("1") and number != "11":
        suffix = "st"
    elif number.endswith("2") and number.endswith("12")==False:
        suffix = "nd"
    elif number.endswith("3") and number != "13":
        suffix = "rd"
    else:
        suffix = "th"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"