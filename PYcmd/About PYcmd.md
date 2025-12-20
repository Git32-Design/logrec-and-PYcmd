# PYcmd (Python Command Tool)

A powerful command-line tool written in Python for file management, calculations, random number generation, and system operations with logging capabilities.

## 🚀 Features

- **File Management**: Read, write, create, delete, list, copy, rename files
- **Directory Operations**: Create and remove directories, navigate paths
- **File Operations**: Get file info, show file statistics, compare files
- **Mathematical Operations**: Math constants and expression calculator
- **Random Utilities**: Generate random numbers (integer and floating-point)
- **Time Functions**: Display current time and date with weekday
- **Command Interface**: Interactive command-line interface
- **Logging**: Integrated logging with custom logrec library

## 📦 Installation

1. Clone or download this repository
2. Ensure Python 3.10 or higher is installed
3. Copy the `logrec` library to your Python site-packages directory:

```
# Example path for Windows
C:/Users/Administrator/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0/LocalCache/local-packages/Python313/site-packages
```

## 📖 Usage

### Running PYcmd

```bash
# Run the interactive command interface
python PYcmd.py
```

### Available Commands

#### File Operations
```bash
read <filepath>                    # Read file contents
write <filepath> <line> <pos> <content>  # Write content at specific position
create <filename> <filepath> <type> <text>  # Create new file
delete <filepath>                  # Delete file
listdir [directory]                # List directory contents (default: current)
copy <source> <destination>        # Copy file
rename <filepath> <new_name>       # Rename file
info <filepath>                    # Get file information
stats <filepath>                   # Show detailed file statistics
compare <file1> <file2>            # Compare two files
```

#### Directory Operations
```bash
pwd                                # Show current working directory
cd <path>                          # Change directory
mkdir <dirpath> <dirname>          # Create directory
rmdir <dirname>                    # Remove directory
```

#### System & Utilities
```bash
mathfunc <function>                # Get math constants (pi, tau, phi, e)
calc <expression>                  # Calculate mathematical expressions
rand <mode> <start> <end>          # Generate random numbers
showt                               # Show current time, date and weekday
help                               # Show help information
clear                               # Clear screen
exit                               # Exit program
```

### Programming Interface

You can also use PYcmd functions directly in your Python code:

```python
import PYcmd

# File operations
PYcmd.read("example.txt")
PYcmd.create("test.txt", ".", "txt", "Hello World")
PYcmd.copy("source.txt", "destination.txt")

# Directory operations
PYcmd.mkdir(".", "new_folder")
PYcmd.listdir("path/to/directory")

# Math operations
PYcmd.math_func("pi")
PYcmd.calc("2 + 3 * 4")

# Random numbers
PYcmd.rand("int", 1, 100)

# Time functions
PYcmd.showt()
```

## 📋 Function Reference

### File Management Functions

| Function | Description | Parameters |
|----------|-------------|------------|
| `read(filepath)` | Read file contents | File path |
| `write(filepath, line, bitnum, content)` | Write content at specific position | File path, line number, position, content |
| `create(filename, filepath, type, text)` | Create new file | Filename, path, file type, initial content |
| `delete(filepath)` | Delete file | File path |
| `listdir(directory=".")` | List directory contents | Directory path (optional) |
| `copy(source, destination)` | Copy file | Source path, destination path |
| `rename(filepath, new_name)` | Rename file | Current path, new name |
| `info(filepath)` | Get file information | File path |
| `compare(file1, file2)` | Compare two files | First file, second file |
| `stats(filepath)` | Show detailed file statistics | File path |

### Directory Functions

| Function | Description | Parameters |
|----------|-------------|------------|
| `pwd()` | Show current working directory | None |
| `cd(path)` | Change directory | Target path |
| `mkdir(dirpath, dirname)` | Create directory | Parent path, directory name |
| `rmdir(dirname)` | Remove directory | Directory path |

### Utility Functions

| Function | Description | Parameters |
|----------|-------------|------------|
| `math_func(function)` | Get math constants | Math constant name (pi, tau, phi, e) |
| `calc(exp)` | Calculate expressions | Mathematical expression |
| `rand(mode, start, end)` | Generate random numbers | Mode (int/float), start, end |
| `showt()` | Show current time, date, weekday | None |
| `help()` | Show help information | None |
| `clear()` | Clear screen | None |

## 🛠️ Math Constants Available

When using `mathfunc` command, you can access mathematical constants:
- `pi` or `π` - Pi constant (3.14159...)
- `tau` or `τ` - Tau constant (6.28318...)  
- `phi` or `Φ` - Golden ratio (1.618)
- `e` or `euler` - Euler's number (2.71828...)

The `calc` command supports standard Python mathematical expressions using `eval()`.

## 📝 Logging

PYcmd automatically logs all operations using the custom `logrec` library:
- Logs are saved to `PYcmd log record.log`
- Successful operations are logged as normal entries
- Errors are logged with error details
- Helps with debugging and tracking usage

## 🔧 Requirements

- Python 3.10 or higher
- logrec library (included in this repository)
- Standard Python libraries: os, math, random, time, pathlib

## 📄 License

This project is licensed under the GNU General Public License v3.0.

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📞 Contact

- Author: Git32-Design
- Developer page : [User stats page](https://github.com/Git32-Design)
- Email: git32mail@qq.com
- Steam : Git32-Games *In steam, You can call me "Git32Play"*
- Netease minecraft : git32mcplay *I haven't money to buy release, But netease make me happy, You can call me "git32mc"*
- Project URL: [Into main page for see updates](https://github.com/Git32-Design/logrec-and-PYcmd)

## 🙏 Acknowledgments

Thanks to Visual Studio Code and its extensions (CODEBUDDY, Python Extension Pack, Pylance) for their support!

---

> 💡 **Note**: PYcmd is currently in development (Dev Alpha 1.0.0). Features and functionality may change as the project evolves.