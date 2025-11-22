"""
    Information of logrec below
    <===================================================================>
    Code lib : logrec
    Fill name : Log Recorder
    Author : git32-programmer
    Version : Dev Alpha 1.0.0
    create at : 2025/11/8
    lastest update : 2025/11/8
    Used lib : os(Operating System)|time(Time)
    Developing at : Visual Studio Code
    Developing language : Python 3.10.0
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
    Description : A quick record log's lib, Can search log file, And record(Or write) logs to a file. It's easy, Please use "logging" library.
"""

import os # Manage file texts.
import time # Get time to record logs.

# Unit 1
# Record logs of 5 level.
# 1.Normal
def log(filepath, text) -> any : 
    Get : str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filepath, "a+") as target :
        target.write(f"[{Get}] Normal log : {text}\n")

# 2.Tips
def tip(filepath, text) -> any : 
    Get : str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filepath, "a+") as target :
        target.write(f"[{Get}] Tips log : {text}\n")

# 3.Warning
def warn(filepath, text) -> any : 
    Get : str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filepath, "a+") as target :
        target.write(f"[{Get}] Warning log : {text}\n")

# 4.Error
def err(filepath, text) -> any : 
    Get : str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filepath, "a+") as target :
        target.write(f"[{Get}] Error log : {text}\n")
        
# 5.Fatal error
def fatal(filepath, text) -> any : 
    Get : str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filepath, "a+") as target :
        target.write(f"[{Get}] Fatal error log : {text}\n")

# Unit 2
# Manage logs.
# 1.Read and output logs.
def re(filepath) -> any : 
    with open(filepath, "r") as target :
        print(target.read())

# 2.Search any logs.
def search(filepath, line) -> any :
    with open(filepath, "r") as target :
        print(target.readlines()[line])

# 3.Delete any logs.
def rem(filepath, line) -> any :
    with open(filepath, "r") as target :
        lines = target.readlines()
        lines.pop(line)
        with open(filepath, "w") as target :
            target.writelines(lines)

# 4.Clear logs
def clear(filepath) -> any :
    with open(filepath, "w") as target :
        target.write("")

# 5.Change log
def change(filepath, line, text) -> any :
    with open(filepath, "r") as target :
        lines = target.readlines()
        lines[line] = text
        with open(filepath, "w") as target :
            target.writelines(lines)

# Unit 3
# Log informations.
# 1.Get log's time.
def gettime(filepath, line) -> any :
    with open(filepath, "r") as target :
        lines = target.readlines(line)
        for line in lines :
            print(line.split(" ")[0])

# 2.Get log's level.
def getlevel(filepath, line) -> any :
    with open(filepath, "r") as target :
        lines = target.readlines(line)
        for line in lines :
            print(line.split(" ")[1])

# Unit 4
# Appendices
# 1.Credits
def credits() -> any :
    print("""
              Credits below
             <------------->
               Programming
              git32-Design
                Codebuddy
                
                Re-Design
               git32-Design
                
                Processor
              Python 3.10.0
                
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
def version() -> any :
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
       1.sb3_2025@qq.com
      2.Netease minecraft
        git32server
     &___________________&
          """)
        
# 3.License
def license() -> any :
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