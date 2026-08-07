def label(colors):
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

    value = (color_code[colors[0]] * 10 + color_code[colors[1]]) * (10 ** color_code[colors[2]])
    if value==0:
        return f"{value} ohms"
    elif value % 1_000_000_000 == 0:
        return f"{value // 1_000_000_000} gigaohms"
    elif value % 1_000_000 == 0:
        return f"{value // 1_000_000} megaohms"
    elif value % 1_000 == 0:
        return f"{value // 1_000} kiloohms"
    elif value >= 1000:
        return f"{value / 1000:g} kiloohms"
    else:
        return f"{value} ohms"
    
        
        
    
    
            
            
        
        
    
    
