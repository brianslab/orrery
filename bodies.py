from utils import to_seconds

bodies = {
    # orbiting - major body the object is orbiting
    # radius - disttance from orbiting body in au
    # full_orbit - time in earth seconds to complete full orbit
    'mercury': {
        'orbiting': 'sun',
        'radius': 0.39,
        'full_orbit': to_seconds(88, 'd'),
        'theta': 0
    },
    'venus': {
        'orbiting': 'sun',
        'radius': 0.72,
        'full_orbit': to_seconds(225, 'd'),
        'theta': 0
    },
    'earth': {
        'orbiting': 'sun',
        'radius': 1,
        'full_orbit': to_seconds(1, 'y'),
        'theta': 0
    },
    'luna': {
        'orbiting': 'earth',
        'radius': 0.00257,
        'full_orbit': to_seconds(28, 'd'),
        'theta': 0
    },
    'mars': {
        'orbiting': 'sun',
        'radius': 1.524,
        'full_orbit': to_seconds(687, 'd'),
        'theta': 0
    }
}
