# Import modules
import sys
import random

# Define the responses in a list
responses = ["IT IS CERTAIN",
             "YOU MAY RELY ON IT",
             "AS I SEE IT, YES",
             "OUTLOOK LOOKS GOOD",
             "MOST LIKELY",
             "IT IS DECIDELY SO",
             "WITHOUT A DOUBT",
             "YES, DEFINETLY"]

# Main loop
while True:
    # Prompt the user to enter a question
    question = input("Ask a question. (Press ENTER to quit)")

    if len(question) > 0:
        # Generate a random index
        index = random.randint(0, len(responses) - 1)

        # Print the response
        print(responses[index])
    else:
        # Exit the program
        sys.exit()
