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

import os # Get file path.
import time # Get time to record logs.

# I want to add some error in this lib.
# 1.Path or file not found.
class FileNotFoundError(Exception):
    def __init__(self, filename, path="Logrec is good"):
        self.filename = filename
        self.path = path
        message = f"File '{filename}' not found"
        if path:
            message += f" in path '{path}'"
        super().__init__(message)
    
    def __str__(self):
        return f"FileError, Error code[001]: {super().__str__()}"

# 2.Line out of range.
class LogOutError(Exception):
    def __init__(self, line):
        self.line = line
        message = f"Line {line} out of range, Error code[002]"
        super().__init__(message)
    
    def __str__(self):
        return f"LogOutError: {super().__str__()}"
    
# 3.Don't read file text(File is empty)
class FileEmptyError(Exception):
    def __init__(self, filename):
        self.filename = filename
        message = f"File '{filename}' is empty, Error code[003]"
        super().__init__(message)
    
    def __str__(self):
        return f"FileEmptyError: {super().__str__()}"

# 4.Not a supported type.
class InvalidTypeError(Exception):
    def __init__(self, type):
        self.type = type
        message = f"Type '{type}' is not supported, Error code[004]"
        super().__init__(message)
    
    def __str__(self):
        return f"InvalidTypeError: {super().__str__()}"

# No more :]

# And, I want to add some function.
# 1.Test file type and path.
def check(filepath) -> None:
    if os.path.exists(filepath) :
        if (filepath.endswith(".txt",".log")) :
            pass
        else:
            raise InvalidTypeError(filepath.split(".")[1])
    else :
        raise FileNotFoundError(filepath)
    
# 2.Test file is empty.
def empty(filepath) -> None:
    check(filepath)
    with open(filepath, 'r') as file:
        if not file.read().strip():
            raise FileEmptyError(filepath)
        
# 3.Test line is out of range.
def out(filepath, line) -> None:
    check(filepath)
    with open(filepath, 'r') as file:
        if line > len(file.readlines()):
            raise LogOutError(line)

# Unit 1
# Record logs of 5 level.
# 1.Normal
def log(filepath, text) : 
    check(filepath)
    Get : str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filepath, "a+", "utf-8") as target :
        target.write(f"[{Get}] Normal log : {text}\n")

# 2.Tips
def tip(filepath, text) : 
    check(filepath)
    Get : str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filepath, "a+", "utf-8") as target :
        target.write(f"[{Get}] Tips log : {text}\n")

# 3.Warning
def warn(filepath, text) : 
    check(filepath)
    Get : str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filepath, "a+", "utf-8") as target :
        target.write(f"[{Get}] Warning log : {text}\n")

# 4.Error
def err(filepath, text) : 
    check(filepath)
    Get : str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filepath, "a+", "utf-8") as target :
        target.write(f"[{Get}] Error log : {text}\n")
        
# 5.Critical error
def crit(filepath, text) : 
    check(filepath)
    Get : str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filepath, "a+", "utf-8") as target :
        target.write(f"[{Get}] Critical error log : {text}\n")

# Unit 2
# Manage logs.
# 1.Read and output logs.
def read(filepath) : 
    check(filepath)
    empty(filepath)
    with open(filepath, "r") as target :
        print(target.read())

# 2.Search any logs.
def search(filepath, line) :
    check(filepath)
    out(filepath, line)
    empty(filepath)
    with open(filepath, "r") as target :
        print(target.readlines()[line])

# 3.Delete any logs.
def rem(filepath, line) :
    check(filepath)
    out(filepath, line)
    empty(filepath)
    with open(filepath, "r") as target :
        lines = target.readlines()
        lines.pop(line)
        with open(filepath, "w") as target :
            target.writelines(lines)

# 4.Clear logs
def clear(filepath) :
    check(filepath)
    empty(filepath)
    with open(filepath, "w") as target :
        target.write("")

# 5.Change log
def change(filepath, line, text) :
    check(filepath)
    out(filepath, line)
    empty(filepath)
    with open(filepath, "r") as target :
        lines = target.readlines()
        lines[line] = text
        with open(filepath, "w") as target :
            target.writelines(lines)

# Unit 3
# Log informations.
# 1.Get log's time.
def gettime(filepath, line) :
    check(filepath)
    out(filepath, line)
    empty(filepath)
    with open(filepath, "r") as target :
        lines = target.readlines(line)
        for line in lines :
            print(line.split(" ")[0])

# 2.Get log's level.
def getlevel(filepath, line) :
    check(filepath)
    out(filepath, line)
    empty(filepath)
    with open(filepath, "r") as target :
        lines = target.readlines(line)
        for line in lines :
            print(line.split(" ")[1])

# Unit 4
# Appendices
# 1.Credits
def credits() :
    print("""
              Credits below
             <------------->
               Programming
              git32-Design
                Codebuddy
                
                Re-Design
               git32-Design
                
                Processor
              Python 3.13.0
                
             Function design
              git32-Design
             
             Programming tool
            Visual Studio Code
            <----------------->
       Thanks for VScode's extensions
                 CODEBUDDY
           Python Extension Pack
                  Pylance
      <------------------------------>
             Thanks for you using!
       I'll Work hard to make it better!
      <--------------------------------->
                   END...
                  <------> 
    """)

# 2.Version
def version() :
    print("""
          Version
         Dev alpha
           1.0.0
           
        Fixed 0 bugs
       Founded 0 bugs
         1 Updates
          lastest
         2025/11/8
         
           Calls
       1.git32mail@qq.com
      2.Netease minecraft
        git32server
     &___________________&
          """)
        
# 3.License
def license() :
    print("""
                                  MIT License

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
    """)

# Original author's comments:
# Oh, It's end? Impossible!
# You can watch "version" function to know my calls, You can feedback to these.
# Thanks for your using!
# >:]      
