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
    
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance