try:
    # I'm opening 'madmax.txt' in read mode to read its content
    with open("madmax.txt", "r") as source_file:
        content = source_file.read()  # I read the entire content of the file
    
    # I'm converting the content to uppercase
    modified_content = content.upper()
    
    # I'm saving the modified content to 'modified.txt'
    with open("modified.txt", "w") as modified_file:
        modified_file.write(modified_content)  # I write the modified content to the file
    
    # I'm notifying the user that the operation was successful
    print("The file has been modified and saved as 'modified.txt'.")
except FileNotFoundError:
    # I'm handling the case where 'madmax.txt' does not exist
    print("Error: 'madmax.txt' was not found. Please ensure the file exists.")
except PermissionError:
    # I'm handling permission issues when accessing the files
    print("Error: Permission denied while accessing 'madmax.txt' or 'modified.txt'.")
except Exception as e:
    # I'm handling any other unexpected errors and displaying what went wrong
    print(f"An unexpected error occurred: {e}")