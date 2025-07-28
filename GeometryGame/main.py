from game import start_game
from tests import test_Point, test_Rectangle, test_Square, test_Cuboid

if __name__ == "__main__":
    
    play_game_or_test = str.casefold(input("Do you want to play the game or test individual geometries ? [y/n] : "))
    
    if play_game_or_test == "y":
        # Let us now play the game 
        start_game()
    else:
        print("Testing Point")
        test_Point()
        print("\nTesting Recatngle")
        test_Rectangle()
        print("\nTesting Square")
        test_Square()
        print("\nTesting Cuboid")
        test_Cuboid()


