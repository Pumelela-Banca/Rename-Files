"""
Renames files in dir
"""

import os


def rename_files(directory=os.getcwd(), prefix="", suffix="", replace_from="",
                 replace_to="", extension=None):
    """
    Renames all files in a directory with optional prefix, suffix, string replamement, 
    and extension change.    
    Args:
        directory (str): Path to the directory containing files to rename
        prefix (str): Text to add at the beginning of each filename
        suffix (str): Text to add at the end of each filename (before extension)
        replace_from (str): Text to replace in filenames
        replace_to (str): Text to replace with in filenames
        extension (str): New file extension (without dot), None to keep original
    """
    
    # Check if the directory exists
    try:
        # Get list of files in the directory
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        if not files:
            print("No files found in the directory.")
            return
        
        print(f"Found {len(files)} files to rename in '{directory}'")
        
        for filename in files:
            # Split filename and extension
            base, ext = os.path.splitext(filename)
            
            # Apply string replacement if specified
            if replace_from:
                base = base.replace(replace_from, replace_to)
            
            # Apply prefix and suffix
            new_base = f"{prefix}{base}{suffix}"
            
            # Use new extension if specified, otherwise keep original
            new_ext = f".{extension}" if extension else ext
            
            # Construct new filename
            new_filename = f"{new_base}{new_ext}"
            
            # Skip if filename hasn't changed
            if new_filename == filename:
                continue
                
            # Construct full paths
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # Check if new filename already exists
            if os.path.exists(new_path):
                print(f"Warning: '{new_filename}' already exists. Skipping '{filename}'")
                continue
                
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: '{filename}' -> '{new_filename}'")
            
        print("File renaming completed.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    import argparse
    
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Rename files in a directory.')
    parser.add_argument('directory', help='Directory containing files to rename')
    parser.add_argument('--prefix', default='', help='Prefix to add to filenames')
    parser.add_argument('--suffix', default='', help='Suffix to add to filenames (before extension)')
    parser.add_argument('--replace-from', default='', help='Text to replace in filenames')
    parser.add_argument('--replace-to', default='', help='Text to replace with in filenames')
    parser.add_argument('--extension', help='New file extension (without dot)')
    
    args = parser.parse_args()
    
    # Call the rename function with provided arguments
    rename_files(
        directory=args.directory,
        prefix=args.prefix,
        suffix=args.suffix,
        replace_from=args.replace_from,
        replace_to=args.replace_to,
        extension=args.extension
    )
