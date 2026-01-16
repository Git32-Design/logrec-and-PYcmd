logrec Library Update Message

Version Alpha 1.1.1 (2025-12-09)

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

*This update message was generated automatically based on the logrec library metadata and functionality.*