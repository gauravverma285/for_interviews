# create a program that reads data from a file, performs some processing, and handles various 
#     exceptions that may occur during file reading, processing, or other operations.

        # ----------------------------------------------------------------------------
def read_file(file_path):
    """Reads numbers from a file and returns them as a list."""
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError as e:
                    print(f"Error: Unable to convert line to number: {line.strip()} - {e}")
    except FileNotFoundError as e:
        print(f"Error: File not found: {file_path} - {e}")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
    return numbers

def process_numbers(numbers):
    """Calculates the sum and average of a list of numbers."""
    try:
        if not numbers:
            raise ValueError("No numbers to process")

        total_sum = sum(numbers)
        average = total_sum / len(numbers)
        return total_sum, average
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing numbers: {e}")
    return None, None

def main():
    file_path = 'numbers.txt'  # Change this to your file path
    numbers = read_file(file_path)
    
    if numbers:
        total_sum, average = process_numbers(numbers)
        if total_sum is not None and average is not None:
            print(f"Sum: {total_sum}, Average: {average}")

if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------------

# generator function 

# load vs loads in json
# json all about json

# merge sort

# function for exception handling
