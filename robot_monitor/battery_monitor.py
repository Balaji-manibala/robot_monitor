
def get_battery_status(battery_percentage):
    """Return the status of a battery based on its percentage."""

    if battery_percentage < 20.0:
        return "CRITICAL"
    elif battery_percentage < 30.0:
        return "LOW"
    else:
        return "NORMAL"
