
def safe_input(message, input_type):
    _continue = True
    value = None
    while _continue:
        try:
            user_input = input(message)
            if user_input == "":
                return None
            
            value = input_type(user_input)
            _continue = False
        except ValueError as e:
            print(f"Expected {input_type}. Please try again. Error: {e}")
            
    return value