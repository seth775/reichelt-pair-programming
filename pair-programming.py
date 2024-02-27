def convert_to_meter(feet, inches):
    """
    Convert measurements in feet and inches to meters.
    
    Parameters:
    feet (int, float): The feet part of the measurement.
    inches (int, float): The inches part of the measurement.
    
    Returns:
    float: The measurement in meters.
    
    Example:
    >>> convert_to_meters(5, 3)
    1.6002
    """
    
    total_inches = 12 * feet + inches
    meters = total_inches * 0.0254
    return meters

# Example usage:
feet = 5
inches = 3
print(f"{feet} feet and {inches} inches is equal to {convert_to_meter(feet, inches)} meters.")



