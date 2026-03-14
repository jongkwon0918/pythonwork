def mask_phone(number) : 
    if len(number)<4 : 
        return "****"
    return number[:-4]+"***"

def mask_name(name) : 
    if len(name)<2 : 
        return name
    return name[0]+"*"+name[2:]
