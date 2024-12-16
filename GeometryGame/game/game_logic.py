from geometry.rectangle import Rectangle
from geometry.point import Point
import random

def start_game():
    """Start the area guessing game."""
    print("Welcome to the Rectangle Area Guessing Game!\n")

    # Generate a random rectangle
    lowleft_x, lowleft_y  = random.randint(1, 10), random.randint(1, 10)
    upright_x, upright_y  = random.randint(10, 20), random.randint(10, 20)
    
    lowleft = Point(lowleft_x, lowleft_y)
    upright = Point(upright_x, upright_y)
    
    rectangle = Rectangle(lowleft , upright)

    print("A rectangle has been generated with random dimensions.")
    print("Try to guess its area!\n")

    # Game loop
    correct_area = rectangle.area()
    while True:
        try:
            guess = int(input("Enter your guess for the area: "))
            if guess == correct_area:
                print("🎉 Correct! You've guessed the area!")
                break
            elif guess < correct_area:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print("\nGame Over. Thanks for playing!")
