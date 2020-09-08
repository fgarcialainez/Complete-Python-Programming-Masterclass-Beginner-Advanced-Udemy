# Import modules
import csv
import sys
import random


# Main class
class Magic8Ball:
    def __init__(self, name):
        self.__name = name
        self.__mQuestions = []
        self.__responses = ["It is certain",
                            "You may rely on it",
                            "As I see it, yes",
                            "Outlook looks good",
                            "Most likely",
                            "It is decidely so",
                            "Without a doubt",
                            "Yes, definetly"]

    def start_game(self):
        # Print welcome message
        print("Welcome " + self.__name + "!")

        # Main game loop
        while True:
            # Prompt the user to enter a question
            question = input("Ask a question. (Press ENTER to quit): ")

            if question != "":
                # Append the question to the list
                self.__mQuestions.append(question)

                # Generate a random index
                index = random.randint(0, len(self.__responses) - 1)

                # Print the response
                print(self.__responses[index])
            else:
                # Write the questions to the CSV file
                self.__write_questions()

                # Display end of game message
                print("Thank you for playing!")

                # Exit the program
                sys.exit()

    def __write_questions(self):
        # Open the .csv file in append mode
        with open('magic_questions.csv', 'a', newline="") as fh:
            # Create the writer
            writer = csv.writer(fh)

            # Write the questions to the file
            for question in self.__mQuestions:
                writer.writerow([question])

            # Close the file
            fh.close()


# Entry point of the program
if __name__ == '__main__':
    # Create an instance of the Magic8Ball class
    c = Magic8Ball("Felix")

    # Start the game
    c.start_game()
