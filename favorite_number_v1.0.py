import json

def get_check_fn():
    """Gets and checks the user's favorite number."""
    fn = input("Enter your favorite number.\n\t")
    while True:
        try:
            fn = float(fn)
        except ValueError:
            fn = input("Must enter a number.\n\t")
        else:
            return fn
            
def store_fn(fn):
    """Stores the user's favorite number."""
    filename = 'user_fn.json'
    with open(filename, 'w') as f:
        json.dump(fn, f)
    print(f"{fn} has been saved as your favorite number.")

def modify_stored_fn():
    """Allows user to modify and save a new favorite number."""
    fn = get_check_fn()
    store_fn(fn)

def previous_fn():
    """Recalls a previously entered favorite number."""
    filename = 'user_fn.json'
    try:
        with open(filename) as f:
            fn = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fn

def response_y_n(response):
    """Checks if a user's response is 'yes' or 'no'.
    Loops until 'yes' or 'no' answer is given."""
    while True:
        if response.lower() == 'yes':
            modify_stored_fn()
            break
        elif response.lower() == 'no':
            break
        else:
            response = input("Enter yes or no.\n\t")

fn = previous_fn()
if fn == None:
    print("Welcome.")
    fn = get_check_fn()
    store_fn(fn)
    response_initial = input("Would you like to modify your favorite number?\n\t")
    response_y_n(response_initial)
else:
    response_modify = input(f"{fn} is saved as your favorite number. Would you like to modify this?\n\t")
    response_y_n(response_modify)