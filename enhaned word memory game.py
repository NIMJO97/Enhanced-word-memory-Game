import random
import time

# List of words to use in the game
fruits = ["apple", "banana", "grape", "orange", "lemon", "mango", "peach", "strawberry",
          "cherry", "pineapple", "watermelon", "blueberry", "kiwi", "pear", "plum"]

animals = ["dog", "cat", "lion", "tiger", "elephant", "giraffe", "monkey", "zebra",
           "rabbit", "bear", "wolf", "fox", "deer", "koala", "kangaroo"]

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown",
          "black", "white", "gray", "violet", "indigo", "cyan", "magenta"]


# Function to start the memory test game
def memory_test():
    print("WELCOME TO THE ENHANCED MEMORY TEST GAME!")

    # Loop until a valid category is entered
    while True:
        print("Choose a category: fruits, animals, or colors")
        category = input("Your choice: ").strip().lower()
        if category in ["fruits", "animals", "colors"]:
            break
        else:
            print("Invalid category! Please choose again.")

    rounds = int(input("How many rounds would you like to play? "))

    total_score = 0
    for i in range(1, rounds + 1):
        print(f"\nRound {i}: ")

        # Choose random words for the game based on the selected category
        if category == "animals":
            random_words = random.sample(animals, 5)
        elif category == "fruits":
            random_words = random.sample(fruits, 5)
        elif category == "colors":
            random_words = random.sample(colors, 5)

        print("Remember these words:")
        print(", ".join(random_words))

        # Wait for a few seconds to let the player memorize the words
        time.sleep(5)

        # Clear the screen (simply print new lines to push the words out of view)
        for _ in range(50):
            print("\n")

        # Prompt the player to recall the words
        print("Now, enter as many words as you remember!")
        recalled_words = set()

        start_time = time.time()
        print("You have 30 seconds.")
        while time.time() - start_time < 30 and len(recalled_words) < 5:
            word = input("Enter a word: ").strip().lower()
            recalled_words.add(word)

        # Calculate and display the score
        correct_words = recalled_words.intersection(random_words)
        score = len(correct_words)
        total_score += score

        print(f"\nYou remembered {score} out of 5 words correctly!")
        if score > 0:
            print("Correct words:", ", ".join(correct_words))
        print("The original words were:", ", ".join(random_words))

    print(f"Game over! Your total score across {rounds} rounds is {total_score} out of {5 * rounds}.")


# Run the memory test game
memory_test()