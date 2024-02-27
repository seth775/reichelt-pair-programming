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


# FEEDBACK - KATIE GONZALEZ
# code is well-documented and provides useful example documentation for the function
# code works well with both floats and integers, returning a float 
# consider adding in-code comments as documentation

# test function
def test_function():
    '''
    Tests Seth's implemented function to convert feet and inches to meters.

    No parameters, returns void.

    Test cases are integer and float cases.
    '''
    # Test Case 1: feet = 10, inches = 7
    result_1 = convert_to_meter(10, 7)
    assert result_1 == 3.2258, f"Test Case 1 Failed. Expected 3.2258, got {result_1}"

    # Test Case 2: feet = 0, inches = 12.5
    result_2 = convert_to_meter(0, 12.5)
    assert result_2 == 0.3175, f"Test Case 2 Failed. Expected 0.3175, got {result_1}"

    print("All test cases passed successfully.")
