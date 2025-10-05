def safe_divide(numerator, denominator):
    """Perform division with error handling."""
    try:
        num = float(numerator)  # Convert numerator to float
        denom = float(denominator)  # Convert denominator to float
        
        if denom == 0:  # Check for division by zero
            return "Error: Cannot divide by zero."
        
        return num / denom  # Return the result if no errors occur

    except ValueError:  # Handle non-numeric input
        return "Error: Please enter numeric values only."