def resistor_label(colors):
    color_code = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    multiplier = {
        "silver": 0.01,
        "gold": 0.1,
        "black": 1,
        "brown": 10,
        "red": 100,
        "orange": 1_000,
        "yellow": 10_000,
        "green": 100_000,
        "blue": 1_000_000,
        "violet": 10_000_000,
        "grey": 100_000_000,
        "white": 1_000_000_000,
    }

    tolerance_band = {
        "grey": "±0.05%",
        "violet": "±0.1%",
        "blue": "±0.25%",
        "green": "±0.5%",
        "brown": "±1%",
        "red": "±2%",
        "gold": "±5%",
        "silver": "±10%",
    }

    if len(colors) == 1:
        return "0 ohms"

    elif len(colors) == 4:
        value = (
            (color_code[colors[0]] * 10 + color_code[colors[1]])
            * multiplier[colors[2]]
        )
        tolerance = tolerance_band[colors[3]]

    elif len(colors) == 5:
        value = (
            (
                color_code[colors[0]] * 100
                + color_code[colors[1]] * 10
                + color_code[colors[2]]
            )
            * multiplier[colors[3]]
        )
        tolerance = tolerance_band[colors[4]]

    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:g} gigaohms {tolerance}"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:g} megaohms {tolerance}"
    elif value >= 1_000:
        return f"{value / 1_000:g} kiloohms {tolerance}"
    else:
        return f"{value:g} ohms {tolerance}"