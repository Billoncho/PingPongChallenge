# PingPongChallenge.py 
# Billy Ridgeway
# Calculates the height and weight of a given number of Ping Pong balls.

def convert_in2cm(inches):  # Defines the function to convert inches to centimeters.
    return inches * 2.54
def convert_lb2kg(pounds):  # Defines the function to convert pounds to kilograms.
    return pounds / 2.2
def convert_cm2in(cm):      # Defines a function to conver centimeters to inches.
    return cm / 2.54
def convert_kg2lb(kg):      # Defines a function to convert kilograms to pounds.
    return kg * 2.2

# Prompts the user to input the number of balls.
number_ping_pong = eval(input("Enter a number of Ping-Pong balls: "))

height_ping_pong_cm = 4 * number_ping_pong              # Calculates the height of the balls in centimeters.
weight_ping_pong_kg = 2.7 * number_ping_pong / 1000     # Calculates the weight of the balls in kilograms.

height_in = round(convert_cm2in(height_ping_pong_cm))   # Converts the number of balls to height in inches and rounds the number.
weight_lb = round(convert_kg2lb(weight_ping_pong_kg))   # Converts the number of balls to weight in pounds and rounds the number.

feet = height_in // 12  # Finds the quotient of the division.
inch = height_in % 12   # Finds the remainder of the division.

# Prints the results to the screen.
print("If you had", number_ping_pong, "Ping-Pong balls, they would measure")
print(feet, "feet", inch, "inches tall, and weigh", weight_lb, "pounds.")
