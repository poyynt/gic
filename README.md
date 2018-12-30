# GIC 

## An image compressor that compresses all images in the working directory.  

[Github](https://github.com/poyynt/gic)  
[PyPI](https://pypi.org/project/gic)

### To execute:  
#### In Linux|Unix|macOS:  
##### GUI:  
Run `gic` in a shell.  
##### CLI:  
Run `gic-cli` in a shell.  
#### In Windows:
##### Method 1:
In a `cmd` window, change working directory to your desired folder and run `gic`(GUI) or `gic-cli`(CLI).  
##### Method 2:
Copy the file `gic.exe`(GUI) or `gic-cli.exe`(CLI) from `pythoninstallation\Scripts\` to your desired folder and double-click it.  
#### To use in your python code:  
A code that the **user** sets the compression level.
###### GUI
```python
import gic.main
#change the working directory to whatever you want
gic.main.run()
```
###### CLI
```python
import gic.cli
#change the working directory to whatever you want
gic.cli.run()
```
#### To be quiet:  
A code that **you** set the compression level.
Set quality to 1|2|3|4 or a percentage. Lower percentage is lower size and lower quality. 1 Means best, 4 means worst.
```python
import gic.compress
gic.compress.compress(quality)
```
You can also pass another arguement to compress images in that directory.
```python
import gic.compress
gic.compress.compress(quality, dir)
```

