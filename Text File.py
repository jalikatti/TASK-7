##### write a python program using function to which will do the following 
	##### a. The function will create text file with the current timestamp 
    ##### b. The file content should have the content of the current timestamp

import time

def create_file_with_timestamp():
    # Get current timestamp
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")  

    # Create file name with current timestamp
    GUVI = f"file_{current_time}.txt"

    # Write content into the file
    with open(GUVI, 'w') as file:
        file.write(current_time)

    print(f"File '{GUVI}' created with content of the current timestamp.")

# Call the function to create the file
create_file_with_timestamp()
