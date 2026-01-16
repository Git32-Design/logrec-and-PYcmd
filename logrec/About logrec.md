# Log Recorder

A simple yet powerful Python library for recording and managing logs, providing quick logging to files, searching, and managing log entries.

## 🚀 Features

- **Simple & Easy**：Intuitive API design, easy to integrate
- **Multiple Log Levels**：Support for INFO, TIP, WARN, ERROR, CRITICAL levels
- **File Management**：Read, search, delete, modify, clear log files
- **Timestamps**：Each log entry automatically includes timestamps
- **Lightweight**：No external dependencies, uses Python standard library only
- **Object-Oriented**：Convenient LogRecorder class provided

## 📦 Installation

```bash
pip install logrec
```

Or copy the `logrec.py` file directly to your project.

## 📖 Usage

### Basic Usage

```python
import logrec

# Record different levels of logs
logrec.log("app.log", "Application started")      # Normal log
logrec.tip("app.log", "Tip information")          # Tip
logrec.warn("app.log", "Warning message")         # Warning
logrec.err("app.log", "Error message")            # Error
logrec.crit("app.log", "Critical error")          # Critical error

# Read logs
logrec.re("app.log")                               # Read all logs

# Search logs
logrec.search("app.log", "error")                  # Search logs containing "error"
```

### Using LogRecorder Class

```python
from logrec import LogRecorder

# Create logger
logger = LogRecorder("myapp.log")

# Record logs
logger.log("User logged in")
logger.warn("Password will expire soon")
logger.err("Login failed")

# Manage logs
logs = logger.read()                              # Read all logs
search_results = logger.search("login")            # Search specific content
logger.remove(3)                                   # Delete line 3
logger.clear()                                     # Clear all logs

# Get information
times = logger.get_time()                          # Get all timestamps
levels = logger.get_level()                        # Get all log levels
```

### Demo

A small demo script is included at `logrec/demo_logrec.py`. It shows a minimal workflow:

- create or ensure a `.log` file exists
- write several log entries using different levels
- read the file and print it
- search by line index and modify a line
- use the `LogRecorder` convenience class

Run the demo from the repository root:

```powershell
python logrec/demo_logrec.py
```

The demo is intended to be simple and educational — for production use prefer
structured logging or Python's `logging` module.

###  JSON logging

logrec supports exporting logs as JSON lines (jsonl) and provides a simple

- Export logs as json or csv:

```python
logrec.export_logs('app.log', 'out.jsonl', fmt='json')
logrec.export_logs('app.log', 'out.csv', fmt='csv')
```

# Create logger
logger = LogRecorder("myapp.log")

# Record logs
logger.log("User logged in")
logger.warn("Password will expire soon")
logger.err("Login failed")

# Manage logs
logs = logger.read()                              # Read all logs
search_results = logger.search("login")            # Search specific content
logger.remove(3)                                   # Delete line 3
logger.clear()                                     # Clear all logs

# Get information
times = logger.get_time()                          # Get all timestamps
levels = logger.get_level()                        # Get all log levels
```

### Log Management Functions

```python
import logrec

# Modify specific log line
logrec.change("app.log", 2, "New log content")

# Delete specific log line
logrec.rem("app.log", 5)

# Clear entire log file
logrec.clear("app.log")
```

## 📋 API Reference

### Log Recording Functions

| Function | Description | Parameters |
|----------|-------------|------------|
| `log(filepath, text)` | Record normal log | File path, Log content |
| `tip(filepath, text)` | Record tip | File path, Log content |
| `warn(filepath, text)` | Record warning | File path, Log content |
| `err(filepath, text)` | Record error | File path, Log content |
| `crit(filepath, text)` | Record critical error | File path, Log content |

### Log Management Functions

| Function | Description | Parameters |
|----------|-------------|------------|
| `re(filepath)` | Read and output logs | File path |
| `search(filepath, line)` | Search log line | File path, Search content |
| `rem(filepath, line)` | Delete specified line | File path, Line number |
| `clear(filepath)` | Clear all logs | File path |
| `change(filepath, line, text)` | Modify specified line | File path, Line number, New content |

### Information Functions

| Function | Description | Parameters |
|----------|-------------|------------|
| `gettime(filepath)` | Get all timestamps | File path |
| `getlevel(filepath)` | Get all log levels | File path |

### Appendix Functions

| Function | Description |
|----------|-------------|
| `credits()` | Show credits information |
| `version()` | Show version information |
| `license()` | Show license information |

## 🛠️ LogRecorder Class Methods

The LogRecorder class provides object-oriented interfaces for all the above functions with slightly different names:

- `read()` - corresponds to `re()`
- `remove()` - corresponds to `rem()`
- `get_time()` - corresponds to `gettime()`
- `get_level()` - corresponds to `getlevel()`

## ⚠️ Exception Handling

logrec defines the following custom exceptions:

- `LRFileNotFoundError` - File not found (Error code 001)
- `LogOutError` - Line number out of range (Error code 002)
- `FileEmptyError` - File is empty
- `InvalidTypeError` - File type is not supported

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📞 Contact

- Author: Git32-Design
- Developer page : [User page](https://github.com/Git32-Design)
- Email: git32mail@qq.com
- Steam : Git32-Games *In steam, You can call me "Git32stm"*
- Netease minecraft : Git32Design_ *I haven't money to buy release, But netease make me happy, You can call me "Git32"*
- Project URL: [Into main page for see updates](https://github.com/Git32-Design/logrec-and-PYcmd)

## 🙏 Acknowledgments

Thanks to Visual Studio Code and its extensions (CODEBUDDY, Python Extension Pack, Pylance) for their support!

---

> 💡 **Tip**: While logrec provides simple logging functionality, for production environments, it's recommended to use Python's built-in `logging` module.
