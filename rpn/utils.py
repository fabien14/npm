def is_int(value: str) -> bool:
    try: 
        int(value)
    except ValueError:
        return False
    else:
        return True
    
def is_float(value: str) -> bool:
    try: 
        float(value)
    except ValueError:
        return False
    else:
        return True