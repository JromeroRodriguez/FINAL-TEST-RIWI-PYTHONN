# Input validation functions - protects the system from incorrect data

def validate_text(prompt):
    value = input(prompt).strip() # removes leading and trailing spaces
    
    if not value:  # checks that the field is not empty
        print("Error: Field cannot be empty.")
        return validate_text(prompt)  # recursion: asks again until valid data is obtained
    
    if not value.isalpha():  # checks only letters
        print("Error: Text must not contain numbers or symbols.")
        return validate_text(prompt)  # recursion: asks again if numbers or symbols are found
        
    return value  # returns clean and validated text

# data_type receives int depending on what the field needs\

def validate_number(prompt, data_type=int):
    try:
        value = data_type(input(prompt))  # converts the input to the specified data type (int)
        if value <= 0:  # validates greater than zero - negative prices or quantities make no sense
            print("Error: Number must be greater than zero.")
            return validate_number(prompt, data_type)  # recursion: asks again if negative
        return value  # returns clean and validated number
    except ValueError:  # catches the error if user types a letter instead of a number
        print("Error: Invalid input. Please enter a number.")
        return validate_number(prompt, data_type)  # recursion: asks again if invalid