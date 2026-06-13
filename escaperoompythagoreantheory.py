import math
 
player_name = input("What's your name?\n")
 
print(f"\nWelcome, {player_name}! You enter the Temple of Right Triangles...")
print("To escape, you must solve puzzles using the Pythagorean Theorem.")
print("The formula is: a² + b² = c²")
print("a and b are the legs of a right triangle, and c is the hypotenuse.\n")
 
 
def get_choice(prompt, valid_options):
    """
    Keeps asking the player until they type a valid answer.
    """
    valid_set = {option.lower() for option in valid_options}
 
    while True:
        answer = input(prompt).strip().lower()
 
        if answer in valid_set:
            return answer
 
        print(f"Invalid choice. Please choose one of these: {', '.join(valid_options)}\n")
 
 
def ask_number(prompt, correct_answer):
    """
    Asks the user for a number and checks if it matches the correct answer.
    """
    while True:
        try:
            answer = float(input(prompt))
 
            if abs(answer - correct_answer) < 0.01:
                print("Correct!\n")
                return True
            else:
                print("Not quite. Try again!")
                print("Remember: a² + b² = c²\n")
 
        except ValueError:
            print("Please enter a number.\n")
 
 
def pythagorean_hypotenuse(a, b):
    """
    Finds the hypotenuse using c = sqrt(a² + b²).
    """
    return math.sqrt(a ** 2 + b ** 2)
 
 
def pythagorean_leg(c, known_leg):
    """
    Finds a missing leg using a² = c² - b².
    """
    return math.sqrt(c ** 2 - known_leg ** 2)
 
 
first_path = get_choice(
    "You reach two glowing doors.\n"
    "The left door says: 'Find the hypotenuse.'\n"
    "The right door says: 'Find the missing leg.'\n"
    "Which door do you enter? Type 'left' or 'right'\n",
    ["left", "right"]
)
 
 
if first_path == "left":
    print("\nYou enter the Hypotenuse Hall.")
    print("A stone triangle appears on the wall.")
    print("One leg is 3 feet. The other leg is 4 feet.")
    print("You need to find the hypotenuse, c.")
 
    print("\nUse the formula:")
    print("a² + b² = c²")
    print("3² + 4² = c²")
    print("9 + 16 = c²")
    print("25 = c²")
    print("c = √25")
 
    answer = ask_number(
        "\nWhat is the hypotenuse?\n",
        5
    )
 
    if answer:
        next_room = get_choice(
            "The door opens! Inside, you see a bridge shaped like a right triangle.\n"
            "A sign says: 'Only those who understand can cross.'\n"
            "Do you cross the bridge or inspect the sign? Type 'cross' or 'inspect'\n",
            ["cross", "inspect"]
        )
 
        if next_room == "inspect":
            print("\nThe sign explains:")
            print("The hypotenuse is always the longest side of a right triangle.")
            print("It is always across from the 90-degree angle.\n")
 
        print("You step onto the bridge safely and continue deeper into the temple.\n")
 
 
elif first_path == "right":
    print("\nYou enter the Missing Leg Chamber.")
    print("A glowing triangle floats in the air.")
    print("The hypotenuse is 13 meters.")
    print("One leg is 5 meters.")
    print("You need to find the missing leg.")
 
    print("\nUse the formula:")
    print("a² + b² = c²")
    print("5² + b² = 13²")
    print("25 + b² = 169")
    print("b² = 169 - 25")
    print("b² = 144")
    print("b = √144")
 
    answer = ask_number(
        "\nWhat is the missing leg?\n",
        12
    )
 
    if answer:
        print("The chamber lights up. You solved the missing side!\n")
 
 
second_challenge = get_choice(
    "You now reach the Final Triangle Gate.\n"
    "A guardian asks: 'Are the sides 6, 8, and 10 a right triangle?'\n"
    "Type 'yes' or 'no'\n",
    ["yes", "no"]
)
 
if second_challenge == "yes":
    print("\nLet's check:")
    print("6² + 8² = 10²")
    print("36 + 64 = 100")
    print("100 = 100")
    print("Yes! This is a right triangle.\n")
 
    final_choice = get_choice(
        "The guardian smiles and offers you two treasures:\n"
        "A golden ruler or a crystal calculator.\n"
        "Which do you choose? Type 'ruler' or 'calculator'\n",
        ["ruler", "calculator"]
    )
 
    if final_choice == "ruler":
        print("\nYou choose the golden ruler.")
        print("It helps you measure triangle sides perfectly.")
    elif final_choice == "calculator":
        print("\nYou choose the crystal calculator.")
        print("It helps you square numbers and find square roots.")
 
    print("\nCongratulations!")
    print("You escaped the Temple of Right Triangles.")
    print("You learned that the Pythagorean Theorem is used to find missing sides of right triangles.")
    print("\nTHE END")
 
else:
    print("\nThe guardian shakes his head.")
    print("Let's check it together:")
    print("6² + 8² = 10²")
    print("36 + 64 = 100")
    print("100 = 100")
    print("So yes, 6, 8, and 10 DO make a right triangle.")
    print("\nThe guardian lets you try again next time.")
    print("THE END")
 