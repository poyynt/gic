# GIC 

## An image compressor that compresses all images in the working directory.  

[Github](https://github.com/poyynt/gic)  
[PyPI](https://pypi.org/project/gic)

### To execute:  
#### In Linux|Unix|macOS:  
Run `gic` in a shell.  
#### In Windows:
##### Method 1:
In a `cmd` window, change working directory to your desired folder and run `gic`.  
##### Method 2:
Copy the file `gic.exe` from `pythoninstallation\Scripts\` to your desired folder and double-click it.  
#### To use in your python code:  
A code that the **user** sets the compression level.
```python
import gic.main
#change the working directory to whatever you want
gic.main.run()
```
#### To be quiet:  
A code that **you** set the compression level.
```python
import gic.main
#change the working directory to whatever you want
#set gic.main.image_quality to 1|2|3|4
gic.main.compress()
```

