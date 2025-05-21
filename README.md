# Rename-Files
Script to rename files in a directory.

## How to Use This Script

1. Save the script as `rename_files.py`
2. Run it from the command line with various options:

Basic usage:
```bash
python rename_files.py /path/to/your/directory
```

Add a prefix to all files:
```bash
python rename_files.py /path/to/directory --prefix "new_"
```

Add a suffix to all files:
```bash
python rename_files.py /path/to/directory --suffix "_v2"
```

Replace text in filenames:
```bash
python rename_files.py /path/to/directory --replace-from "oldtext" --replace-to "newtext"
```

Change file extensions:
```bash
python rename_files.py /path/to/directory --extension "txt"
```

Combine options:
```bash
python rename_files.py /path/to/directory --prefix "project_" --suffix "_2023" --extension "jpg"
```