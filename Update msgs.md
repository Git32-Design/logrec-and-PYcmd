logrec Library Update Message

Version Release 3.3.2 (2026-01-17)  *Version error, must be 3.7.3(2026-01-17)*

🚀 Overview
The logrec library provides a lightweight and intuitive solution for log recording and management in Python applications. Designed as a simpler alternative to Python's built-in logging module, it offers essential logging functionality with an emphasis on ease of use and file-based log storage.

✨ Key Features

1. Five-Level Logging System
Record logs at different severity levels:
- **Normal**: log(filepath, text) - General information
- **Tips**: tip(filepath, text) - Helpful suggestions
- **Warning**: warn(filepath, text) - Potential issues
- **Error**: err(filepath, text) - Recoverable errors
- **Critical**: crit(filepath, text) or fatal(filepath, text) - Severe errors

2. Log Management Functions
- **Read**: read(filepath) - Display all logs
- **Search**: search(filepath, line) - Retrieve specific log line
- **Delete**: rem(filepath, line) - Remove a log entry
- **Clear**: clear(filepath) - Empty the log file
- **Modify**: change(filepath, line, text) - Update a log entry

3. Advanced Utilities
- **Log Parsing**: parse_log_line(line) - Extract timestamp, level, and message
- **Export**: export_logs(filepath, out_path, fmt='json') - Convert logs to JSON/CSV
- **Keyword Search**: search_by_keyword(filepath, keyword) - Find logs containing specific text
- **Tail**: tail(filepath, n=10) - View last *n* log entries
- **Metadata Extraction**: gettime(), getlevel() - Retrieve log timestamps and levels

🛠️ Error Handling
The library includes robust error handling with custom exceptions:
- LRFileNotFoundError - Handles missing log files
- LogOutError - Prevents out-of-range line access
- FileEmptyError - Detects empty log files
- InvalidTypeError - Ensures correct input types

💻 Usage Example
import logrec

Initialize log file
log_file = "app.log"

Record different log levels
logrec.log(log_file, "Application started")
logrec.tip(log_file, "Check configuration settings")
logrec.warn(log_file, "Low memory warning")
logrec.err(log_file, "Failed to connect to database")
logrec.crit(log_file, "Critical system failure")

Manage logs
logrec.read(log_file)  # View all logs
logrec.tail(log_file, 5)  # View last 5 logs
logrec.search_by_keyword(log_file, "warning")  # Search logs

Export logs to CSV
logrec.export_logs(log_file, "logs_export.csv", fmt='csv')

ℹ️ Additional Information
- **Compatibility**: Python 3.13.0+
- **License**: MIT License (see logrec.license())
- **Credits**: See logrec.credits() for contributor information
- **Version Info**: See logrec.version() for detailed version history

📌 Notes
- The library automatically creates log files if they don't exist
- All log entries include timestamps in ISO 8601 format
- The export_logs() function supports both JSON and CSV formats
- The search_by_keyword() function is case-insensitive by default

🙏 Acknowledgments
Thanks to the Python community for inspiration and guidance. Special recognition to the developers of the logging module, whose work informed the design of this simplified alternative.

## 📞 Contact

- Author: Git32-Design
- Developer page : [User page](https://github.com/Git32-Design)
- Email: git32mail@qq.com
- Steam : Git32-Games *In steam, You can call me "Git32stm"*
- Netease minecraft : Git32Design_ *I haven't money to buy release, But netease make me happy, You can call me "Git32"*
- Project URL: [Into main page for see updates](https://github.com/Git32-Design/logrec-and-PYcmd)
- PyPI project: [LogrecAndPYcmd](https://pypi.org/project/LogrecAndPYcmd/)
---
# Version Release 4.8.4 (2026-01-31)

## 🚀 Update fast report

## I.🔧 logrec \_\_init\_\_ change report

1. function name *fatal* fix to __crit__.

2. Added custom exception in init program.

## II.❌ PYcmd english and proper nouns fix

1. *github* to *GitHub*.

2. *netease* to *Netease*.

## III.📄 Version number fix for *Update msgs.md* and *PYcmd.py*

1. Update msgs: *3.3.2* to *3.7.3*

2. PYcmd.py: *Dev Alpha 1.0.0* to *Release 2.1.1*

## IV.🔗 Setup.py and pyproject.toml fix

1. Deleted __setup.py__ and __pyproject.toml__ dependencies 'pytest'.

2. Removed *pyproject.toml* line 48 comment.

## V.📄 PYcmd log

1. Clear PYcmd's log texts.
---