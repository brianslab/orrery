def to_seconds(val, unit):
    match unit:
        case 's':
            return val
        case 'm':
            return val*60
        case 'h':
            return val*60*60
        case 'd':
            return val*60*60*24
        case 'y':
            return val*60*60*24*365
        case _:
            return -1
