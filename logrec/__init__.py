"""
Log Recorder Module (logrec)

A quick record log's library that can search log files and record/write logs to a file.

Author: git32-programmer
Version: Dev Alpha 1.0.0
License: MIT License
"""

from .logrec import (
    # Log recording functions
    log, tip, warn, err, fatal,
    
    # Log management functions
    re, search, rem, clear, change,
    
    # Log information functions
    gettime, getlevel,
    
    # Appendix functions
    credits, version, license
)

# Module metadata
__version__ = "Dev Alpha 1.0.0"
__author__ = "git32-programmer"
__license__ = "MIT License"

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