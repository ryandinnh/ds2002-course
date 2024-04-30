def write_data_to_file(data, filename):
  try:
    with open(filename, 'w', encoding='utf-8') as file:
      file.write(data)
  except FileNotFoundError as e:
    print(f"Error: File {filename} not found.")
  except PermissionError as e:
    print(f"Error: Permission denied to write to {filename}.")
  finally:
    if 'file' in locals():  # Check if 'file' variable exists (was opened)
      file.close()  # Close the file if it was opened

# Example usage
data = "This is some data to write to the file."
filename = "my_data.txt"
write_data_to_file(data, filename)

#Response to "Explain the function of the finally block in this snippet. What purpose does it serve?"
"""
In the code chunk above the "finally" block is used to close the file, if it was opened in the first place or not, regardless of if the actual code function succeeds or an error occurs. 
Using "finally" here is important as it serves the purpose of saving computer resources. Ie. in the case of an exception error occuring, it is still important to close the file after the exception is thrown as system resources could leak with the file staying open.
"""