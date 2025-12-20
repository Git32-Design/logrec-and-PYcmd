"""
    Information of logrec below
    <===================================================================>
    Code lib : logrec
    Fill name : Log Recorder
    Author : Git32-Design
    Version : Alpha 1.1.1
    create at : 2025/11/8
    lastest update : 2025/12/9
    Used lib : os(Operating system)|time(Time)
    IDE : Visual Studio Code
    Developing language : Python 3.13.0
    Licence : MIT License
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    Description : A quick record log's lib, Can search log file, And record(Or write) logs to a file. It's easy, Please use "logging" library. I know, My lib is sucks, But I well publish it to github.
"""

from .logrec import (\
    
    # Log recording functions
    log, tip, warn, err, crit,
    
    # Log management functions
    re, search, rem, clear, change,
    
    # Log information functions
    gettime, getlevel,
    
    # Appendix functions
    credits, version, license
)

# Module metadata (PEP 396 compliant)
__version__ = "1.0.0.dev0"
__version_info__ = (1, 0, 0, 'dev', 0)
__author__ = "Git32-Design"
__author_email__ = "git32-design@example.com"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2025 Git32-Design"
__maintainer__ = "Git32-Design"
__maintainer_email__ = "git32-design@example.com"

# PyPI package metadata
__title__ = "Log Recorder"
__summary__ = "A quick record log's library with search and management capabilities"
__description__ = "A quick record log's library with search and management capabilities"
__long_description__ = """\
Log Recorder is a simple yet powerful Python library for recording and managing log files.
It provides easy-to-use functions for writing logs of different levels, searching through
log entries, and managing log files. While Python's built-in logging module is recommended
for production use, this library offers a lightweight alternative for quick logging tasks.
"""
__keywords__ = ["log", "logger", "recording", "search", "management", "file", "logging", "debug"]
__project_urls__ = {
    "Homepage": "https://github.com/Git32-Design/logrec-and-PYcmd",
    "Documentation": "None",
    "Repository": "https://github.com/Git32-Design/logrec.git",
    "Bug Tracker": "https://github.com/Git32-Design/logrec/issues",
}
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Logging",
    "Topic :: System :: Systems Administration",
    "Topic :: Utilities",
]
__python_requires__ = ">=3.8"

# Standard metadata
__doc__ = """
    Information of logrec below
    <===================================================================>
    Code lib : logrec
    Fill name : Log Recorder
    Author : Git32-Design
    Version : Alpha 1.1.1
    create at : 2025/11/8
    lastest update : 2025/12/9
    Used lib : os(Operating system)|time(Time)
    IDE : Visual Studio Code
    Developing language : Python 3.13.0
    Licence : MIT License
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    Description : A quick record log's lib, Can search log file, And record(Or write) logs to a file. It's easy, Please use "logging" library. I know, My lib is sucks, But I well publish it to github.
"""


# Export all public functions
__all__ = [
    # Log recording
    'log', 'tip', 'warn', 'err', 'fatal',
    
    # Log management
    're', 'search', 'rem', 'clear', 'change',
    
    # Log information
    'gettime', 'getlevel',
    
    # Appendix
    'credits', 'version', 'license'
]

# Convenience imports for common use cases
class LogRecorder:
    """Convenience class for log recording operations"""
    
    def __init__(self, filepath):
        self.filepath = filepath
    
    def log(self, text):
        """Record normal log"""
        return log(self.filepath, text)
    
    def tip(self, text):
        """Record tip log"""
        return tip(self.filepath, text)
    
    def warn(self, text):
        """Record warning log"""
        return warn(self.filepath, text)
    
    def err(self, text):
        """Record error log"""
        return err(self.filepath, text)
    
    def fatal(self, text):
        """Record fatal error log"""
        return fatal(self.filepath, text)
    
    def read(self):
        """Read and output logs"""
        return re(self.filepath)
    
    def search(self, line):
        """Search specific log line"""
        return search(self.filepath, line)
    
    def remove(self, line):
        """Remove specific log line"""
        return rem(self.filepath, line)
    
    def clear(self):
        """Clear all logs"""
        return clear(self.filepath)
    
    def change(self, line, text):
        """Change specific log line"""
        return change(self.filepath, line, text)
    
    def get_time(self):
        """Get log times"""
        return gettime(self.filepath)
    
    def get_level(self):
        """Get log levels"""
        return getlevel(self.filepath)
    
    def credits(self):
        """Show credits"""
        return credits()
    
    def version(self):
        """Show version"""
        return version()
    
    def license(self):
        """Show license"""
        return license()