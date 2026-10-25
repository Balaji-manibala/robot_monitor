
def get_temperature_status(temperature_celsius):
    """Return the status of a temperature reading."""

    if temperature_celsius >= 45.0:
        return "CRITICAL"
    elif temperature_celsius >= 35.0:
        return "HIGH"
    else:
        return "NORMAL"
