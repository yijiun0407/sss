## python101_0326

1. Anaconda install

2. Using jupyterlab as our coding tool

3. jupyterlab 

   - command mode :  press 'ESC' 
   - edit mode : press 'Enter'
   - each cell : 
     - markdown (in command mode : press 'm')
     - code (in command mode : press 'y')

   - write some codes in cell and execute
     - Alt + Enter (execute code and add new cell below)
     - Ctrl + Enter (execute code only)
     - Shift + Enter (execute code and move to new cell below)

   - install package/module in cell
     - !pip install emoji (if you want to install python packages you are interesting)
     - pypi is the official python packages/modules source

   - %run xxx.ipynb or %run xxxx.py (run ipynb or py file in the cell)
   - data = 'data here , please using me', %store data and using the data in another ipynb file
   - %%wirtefile pythocode.py (output the cell content to pythoncode.py)

4. python101 : 

   - 4 data_type
     - int : interger (1, 3, 5)
     - float : 小數 (1.3, 2.5)
     - string : 字串 ('i am a python string')
     - bool : True/False

   - assign variable using *=*
     - a = 15, b = 'i am a python string'
   - compare using *==*(等於) or *!=*(不等於)
     - a == 15, a !=16
     - b == 'i am a python string', b!='i am not a python string'

   - ```python
     if a is True:
         print (a) # 假設a這個是對的話，則執行下面這件事情
     ```