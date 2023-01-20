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


bodies = {
    # orbiting - major body the object is orbiting
    # radius - disttance from orbiting body in au
    # full_orbit - time in earth seconds to complete full orbit
    'mercury': {
        'orbiting': 'sun',
        'radius': 0.39,
        'full_orbit': to_seconds(88, 'd')
    },
    'venus': {
        'orbiting': 'sun',
        'radius': 0.72,
        'full_orbit': to_seconds(225, 'd')
    },
    'earth': {
        'orbiting': 'sun',
        'radius': 1,
        'full_orbit': to_seconds(1, 'y')
    },
    'luna': {
        'orbiting': 'earth',
        'radius': 0.00257,
        'full_orbit': to_seconds(28, 'd')
    },
    'mars': {
        'orbiting': 'sun',
        'radius': 1.524,
        'full_orbit': to_seconds(687, 'd')
    }
}
