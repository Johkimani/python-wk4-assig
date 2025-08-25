# Ask user for the input filename
filename = input("Enter the filename to read: ")

try:
    # Try opening the file
    with open(filename, "r") as infile:
        content = infile.read()

    print("\n Original File Content:\n")
    print(content)

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Create a new output filename
    output_filename = "modified_" + filename

    # Write the modified content to the new file
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"\n Modified content saved to '{output_filename}'")

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")

