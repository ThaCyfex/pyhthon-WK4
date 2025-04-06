# pyhthon-WK4

# Error Handling Script

## Description
This Python script reads the content of a file named `madmax.txt`, converts its content to uppercase, and saves the modified content into a new file named `modified.txt`. The script includes error handling to manage common issues such as missing files, permission errors, and unexpected exceptions.

## Features
- Reads the content of `madmax.txt`.
- Converts the content to uppercase.
- Saves the modified content to `modified.txt`.
- Provides clear error messages for:
  - Missing `madmax.txt`.
  - Permission issues when accessing files.
  - Any other unexpected errors.

## Requirements
- Python 3.x
- Ensure `madmax.txt` exists in the same directory as the script.

## Usage
1. Place the script and `madmax.txt` in the same directory.
2. Run the script using the command:
   ```bash
   python error_handling.py
   ```
3. If successful, the script will create or overwrite a file named `modified.txt` with the uppercase content of `madmax.txt`.

## Error Handling
- **FileNotFoundError**: Displays an error message if `madmax.txt` is not found.
- **PermissionError**: Displays an error message if there are permission issues with `madmax.txt` or `modified.txt`.
- **General Exception**: Displays a message for any other unexpected errors.

## Example Output
If the script runs successfully:
```
The file has been modified and saved as 'modified.txt'.
```

If `madmax.txt` is missing:
```
Error: 'madmax.txt' was not found. Please ensure the file exists.
```

If there are permission issues:
```
Error: Permission denied while accessing 'madmax.txt' or 'modified.txt'.
```

## Notes
- Ensure you have the necessary permissions to read `madmax.txt` and write to `modified.txt`.
- The script overwrites `modified.txt` if it already exists.
