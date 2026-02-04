# Logrec-And-PYcmd Update report ![Static Badge](https://img.shields.io/badge/Account-Git32Design__-red?logo=Bilibili)

Version Release 3.3.2 (2026-01-17)  *Version error, must be 3.7.3(2026-01-17)*

![Static Badge](https://img.shields.io/badge/Update-Fast%20report-blue?logo=RefinedGithub)

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

- Author: Git32-Design  ![Static Badge](https://img.shields.io/badge/author-Git32-c5c5ff?logo=github)

- Developer page : [User page](https://github.com/Git32-Design)  ![Static Badge](https://img.shields.io/badge/Dev-Github-blue?logo=SuperUser)

- Email: git32mail@qq.com  ![Static Badge](https://img.shields.io/badge/Mail-QQ-light_blue?logo=QQ)

- Steam : Git32-Games *In steam, You can call me "Git32stm"*  ![Static Badge](https://img.shields.io/badge/Git32-Steam-lightblue?logo=Steam)

- Netease minecraft : Git32Design_ *I haven't money to buy release, But netease make me happy, You can call me "Git32"*  ![Static Badge](https://img.shields.io/badge/Netease-MC-yellow?)

- Project URL: [Into main page for see updates](https://github.com/Git32-Design/logrec-and-PYcmd)   ![Static Badge](https://img.shields.io/badge/About-Project-skyblue?logo=github)

- PyPI project: [LogrecAndPYcmd](https://pypi.org/project/LogrecAndPYcmd/) ![Static Badge](https://img.shields.io/badge/PyPI-LogrecAndPYcmd-brightgreen?logo=PyPI)
---
# Version Release 4.8.4 (2026-01-31)

## 🚀 Update fast report

## I.🔧 change \_\_init\_\_ of logrec and PYcmd 

1. logrec:function name *fatal* fix to __crit__.

2. logrec:Added custom exception in init program.

3. PYcmd:Removed parent package invalid import.

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
# Version Release 4.8.5 (2026-02-04)

## 🚀 Update fast report

## I.🔧 Import statements fix for logrec and PYcmd

1. logrec: Changed *from logrec import* to *from .logrec import* for relative import.

2. PYcmd: Changed *from PYcmd import* to *from .PYcmd import* for relative import.

## II.📄 Log file cleanup

1. Cleared PYcmd log record.log file contents.

## III.📝 Documentation updates

1. README.md: Removed repository update times line at the end.

2. Update msgs.md: Added repository update times section.

## IV.🧪 Test file formatting

1. PYcmd/tests/test_PYcmd.py: Removed newline at end of file.

## V.📊 Version tracking

1. Repository update times(Repo datas version): 68 to 70

# Version Release 4.8.6 (2026-02-04)

## 🚀 Update fast report, very faster!!

## I.📦 Dependencies management

1. Created `dev-requirements.txt` for development dependencies.

2. Updated `requirements.txt` to remove unnecessary dependencies.

## II.📄 Documentation updates

1. `.readthedocs.yaml`: Updated configuration for Read the Docs documentation build.

2. `Update msgs.md`: Continued documentation of version changes and updates.

## III.🔧 Module improvements

1. logrec `__init__.py`: Version metadata and import structure refinements.

2. PYcmd `__init__.py`: Version metadata and module information updates.

## IV.📊 Project configuration

1. `pyproject.toml`: Updated project metadata and version information.

2. `README.md`: Documentation improvements and formatting updates.

## V.📊 Version tracking

1. Repository update times(Repo datas version): 70 to 72

## VI.📄 Original project identifiers

1. `Identifiers.txt` Included important information of this project.
---

# Format version=72