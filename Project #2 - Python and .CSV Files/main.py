# Import modules
import csv


# Read CVS function
def readcsv(dept=None):
    # Open the .csv file in read mode
    with open('example.csv', 'r') as fh:
        # Read the contents of the file
        reader = csv.reader(fh, delimiter=',')

        # Included a new line before the output
        print()

        # Print the contents of the .csv
        for row in reader:
            # Filter by department
            if dept:
                if row[3] == dept:
                    print(row)
            else:
                print(row)

        # Close the file
        fh.close()


# Write CVS function
def writecsv():
    # Open the .csv file in append mode
    with open('example.csv', 'a') as fh:
        # Create the writer
        writer = csv.writer(fh)

        # Create a new record
        record = ["1006", "Felix", "Garcia", "IT"]

        # Write the new record to the file
        writer.writerow(record)

        # Close the file
        fh.close()


# Entry point of the program
if __name__ == "__main__":
    # Print the contents of the file
    readcsv()

    # Update the contents of the file
    writecsv()

    # Print the contents of the file again
    readcsv()

    # Print the contents of the file filtering by IT department
    readcsv("IT")
