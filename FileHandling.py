# Open the original file for reading
with open("original_file.txt", "r") as input_file:
    content = input_file.read()  # Read the entire content of the file

# Modify the content (e.g., convert to uppercase in this example)
modified_content = content.upper()

# Open a new file for writing the modified content
with open("modified_file.txt", "w") as output_file:
    output_file.write(modified_content)  # Write the modified content to the new file

print("The file has been modified and saved as 'modified_file.txt'.")
