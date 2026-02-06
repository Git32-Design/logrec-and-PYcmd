# logrec and PYcmd

Welcome to the logrec and PYcmd project repository! This repository contains two complementary Python tools designed to enhance your development and file management experience.

## 📦 What's Included

### 📝 logrec - Log Recorder Library
A simple yet powerful Python library for recording and managing logs with search capabilities.

**Key Features:**
- Simple & intuitive API design
- Multiple log levels (INFO, TIP, WARN, ERROR, CRITICAL)
- File management (read, search, delete, modify, clear)
- Automatic timestamps
- Lightweight with no external dependencies
- Object-oriented LogRecorder class

**Perfect for:**
- Application logging
- Debugging sessions
- Quick record keeping
- Learning logging concepts

### 🖥️ PYcmd - Python Command Tool
A powerful command-line tool for file management, calculations, and system operations with integrated logging.

**Key Features:**
- Complete file management suite
- Directory operations
- Mathematical calculations
- Random number generation
- Time and date utilities
- Interactive command interface
- Integrated logging with logrec

**Perfect for:**
- System administration tasks
- File batch operations
- Quick calculations
- Learning command-line tool development

## 🚀 Quick Start

### Using logrec

```python
import logrec

# Simple logging
logrec.log("app.log", "Application started")
logrec.err("app.log", "Error occurred")

# Using the LogRecorder class
logger = LogRecorder("myapp.log")
logger.log("User logged in")
logger.warn("Session expiring soon")
```

### Using PYcmd

```bash
# Run the interactive command interface
python PYcmd.py

# Available commands include:
# read, write, create, delete, listdir, copy, rename
# mkdir, rmdir, cd, pwd, compare, stats
# math, calc, rand, showt, help, clear, exit
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Standard Python libraries (os, math, random, time, pathlib)

### Installation Steps

1. **Clone this repository:**
```bash
git clone https://github.com/Git32-Design/logrec-and-PYcmd.git
cd logrec-and-PYcmd
```

2. **From PyPI install:**
```bash
pip install LogrecAndPYcmd
```

## 📁 Repository Structure

```
logrec-and-PYcmd/                     # Main repository folder
|-- .github/                          # GitHub settings
|   |__ workflows/                    # CI/CD workflows
|       |-- python-package.yml        # Package testing workflow
|       |__ python-publish.yml        # PyPI publishing workflow
|-- logrec/                           # Log Recorder Library
|   |-- tests/                        # Tests for logrec
|   |   |__ test_logrec.py            # Unit test script
|   |-- __init__.py                   # Library initialization and metadata
|   |-- logrec.py                     # Core logging functionality
|   |__ About logrec.md               # Detailed logrec documentation
|-- PYcmd/                            # Python Command Tool
|   |-- tests/                        # Tests for PYcmd
|   |   |__ test_PYcmd.py             # Unit test script
|   |-- __init__.py                   # Library initialization and metadata
|   |-- PYcmd.py                      # Main command tool implementation
|   |__ About PYcmd.md                # Detailed PYcmd documentation
|-- dist/                             # Distribution packages (generated)
|   |-- logrecandpycmd-5.8.8-py3-none-any.whl  # Wheel package
|   |__ logrecandpycmd-5.8.8.tar.gz            # Source distribution
|-- LogrecAndPYcmd.egg-info/          # Package metadata (generated)
|   |-- dependency_links.txt          # It's air :[
|   |-- PKG-INFO                      # Package information, included README.md
|   |-- requires.txt                  # Only pytest
|   |-- SOURCES.txt                   # Package sources
|   |-- top_level.txt                 # Package import names
|-- .gitignore                        # Git ignore rules
|-- .readthedocs.yaml                 # ReadTheDocs configuration
|-- dev-requirements.txt              # Development dependencies
|-- Identifiers.txt                   # Project identifiers
|-- LICENSE                           # MIT License
|-- pyproject.toml                    # Project configuration and build system
|-- README.md                         # This file - project documentation
|-- requirements.txt                  # Runtime dependencies
|__ Update msgs.md                    # Version update history and changelog
```

## 🔗 Integration

### logrec + PYcmd Integration
PYcmd uses logrec internally for all operation logging:
- Successful operations are logged as normal entries
- Errors are logged with detailed error information
- Logs are saved to `PYcmd log record.log`
- Provides complete audit trail of all operations

## 📋 Version Information

### Current Versions
- **logrec**: Release 3.7.3
- **PYcmd**: Release 2.1.2
- **Package**: Release 5.8.8
- **Project Status**: Release

### Release Status
- [x] Stable and production-ready
- [x] Published on PyPI
- [x] Comprehensive documentation available
- [x] Tested and verified
- [x] Continuous integration and testing

## 🎯 Use Cases

### For Developers
- **Application Logging**: Use logrec in your Python applications
- **Development Tools**: Use PYcmd for quick file operations
- **Learning Resources**: Study the code to understand Python concepts
- **Script Development**: Extend or modify for custom needs

### For System Administrators
- **File Management**: Use PYcmd for batch file operations
- **Log Analysis**: Use logrec for custom logging solutions
- **Automation**: Integrate into existing workflows
- **Quick Tasks**: Use PYcmd's interactive interface

### For Students
- **Learning Python**: Study well-commented code examples
- **Understanding File I/O**: Learn practical file operations
- **API Design**: Study clean function interfaces
- **Project Structure**: Learn repository organization

## 🔧 Technical Specifications

### Dependencies
- **logrec**: Python standard library only (os, time)
- **PYcmd**: Python standard library (os, math, random, time, pathlib) + logrec

### Compatibility
- **Python**: >= 3.8 (recommended 3.13)
- **Operating System**: Cross-platform (Windows, Linux, macOS)
- **Memory Usage**: Lightweight, minimal footprint

### Performance
- **Logging Speed**: Fast file I/O with minimal overhead
- **Command Response**: Quick execution for most operations
- **Resource Usage**: Low CPU and memory requirements

## 📄 Licensing

This project uses dual licensing:
- **logrec**: MIT License
- **PYcmd**: MIT License

See individual LICENSE files for details.

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Issues
- Use GitHub Issues for bug reports
- Provide detailed reproduction steps
- Include system information
- Add screenshots if applicable

### Submitting Pull Requests
- Fork the repository
- Create a feature branch
- Make your changes
- Test thoroughly
- Submit pull request with description

### Code Standards
- Follow PEP 8 guidelines
- Add comments to complex code
- Update documentation
- Include tests when possible

## 📞 Contact Information

- Author: Git32-Design
- Developer page : [User stats page](https://github.com/Git32-Design)
- Email: git32mail@qq.com
- Steam : Git32-Games *In steam, You can call me "Git32Play"*
- Netease minecraft : Git32Design__ *I haven't money to buy release, But netease make me happy, You can call me "git32mc"*
- Project URL: [Into main page for see updates](https://github.com/Git32-Design/logrec-and-PYcmd)
- PyPI project: [LogrecAndPYcmd](https://pypi.org/project/LogrecAndPYcmd/)

## 🙏 Acknowledgments

### Development Tools
- **Visual Studio Code**: Primary development environment
- **CODEBUDDY**: AI coding assistant
- **Python Extension Pack**: Python language support
- **Pylance**: Python linting and intelligence

### Community
- **Python Community**: For excellent documentation and examples
- **GitHub Community**: For hosting and collaboration tools
- **Open Source Contributors**: For inspiration and best practices
- **PyPI Python Package Index**: For easy installation of pip

## 🚀 Roadmap

### Upcoming Features
- [ ] Enhanced error handling in PYcmd
- [ ] Configuration file support
- [ ] Plugin system for PYcmd
- [ ] Advanced search capabilities in logrec
- [ ] Performance optimizations
- [ ] Additional file format support

### Long-term Goals
- [ ] GUI interface for PYcmd
- [ ] Web interface for log management
- [ ] Integration with popular frameworks
- [ ] Comprehensive test suite
- [ ] Internationalization support
- [ ] Package distribution (PyPI)

---

## 💡 Getting Help

### Documentation
- Read the individual `About*.md` and `README.md` files for detailed information
- Check code comments for implementation details
- Review function docstrings for usage examples

### Community Support
- GitHub Issues for bug reports and feature requests
- Discussions for general questions and ideas
- Pull Requests for contributions

### Learning Resources
- Python official documentation
- File I/O tutorials
- Command-line tool development guides
- Logging best practices

---

**Thank you for using logrec and PYcmd!** 

We're constantly working to improve these tools and would love to hear your feedback, suggestions, and ideas. Whether you're a developer, system administrator, or student, we hope these tools make your work easier and more productive.

Happy coding! 🎉