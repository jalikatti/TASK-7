##### Write a python program for function to read from a text file. The function will take the name of 
##### the text file and display the content of the file into the console


def read_file(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the content of the file
            file_content = file.read()
            # Display the content in the console
            print("Content of the file:")
            print(file_content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
file_name = input("Enter the name of the text file: ")
read_file(file_name)
