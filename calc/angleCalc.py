import math

# Function to clamp a value within a given range
def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def calculate_angles(x, y, l1, l2):
    sqrt = math.sqrt
    acos = math.acos
    atan2 = math.atan2
    degrees = math.degrees

    d = sqrt(x**2 + y**2)
    
    # Scale down the target if it's out of range
    if d > (l1 + l2):
        scale = (l1 + l2) / d
        x *= scale
        y *= scale
        d = l1 + l2

    # Avoid math domain error by clamping the value to the range [-1, 1]
    cos_theta2 = clamp((x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2), -1, 1)
    
    try:
        teta2 = degrees(acos(cos_theta2))
    except ValueError:
        return None, None  # If acos fails, return None
    
    # Check if d is zero to avoid zero division error
    if d == 0:
        return None, None

    alpha = atan2(y, x)
    # TODO: Handle zero division error on beta calculation
    beta = acos(clamp((l1**2 + d**2 - l2**2) / (2 * l1 * d), -1, 1))
    teta1 = degrees(alpha - beta)
    
    return teta1, teta2 
