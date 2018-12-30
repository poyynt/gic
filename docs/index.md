# GIC 

## An image compressor that compresses all images in the working directory.  

[Github](https://github.com/poyynt/gic)   
[PyPI](https://pypi.org/project/gic)   
[Download ZIP]({{ site.github.zip_url }})   
[Download TAR]({{ site.github.tar_url }})   
[Releases]({{ site.github.releases_url }})   
<!--Latest Release: {{ site.github.latest_release}}-->
[RSS](feed.xml)

### To install:
Run `pip install gic`.


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
{% highlight python linenos %}
import gic.main
#change the working directory to whatever you want
gic.main.run()
{% endhighlight %}
###### CLI
{% highlight python linenos %}
import gic.cli
#change the working directory to whatever you want
gic.cli.run()
{% endhighlight %}
#### To be quiet:  
A code that **you** set the compression level.
Set quality to 1|2|3|4 or a percentage. Lower percentage is lower size and lower quality. 1 Means best, 4 means worst.
{% highlight python linenos %}
import gic.compress
gic.compress.compress(quality)
{% endhighlight %}
You can also pass another arguement to compress images in that directory.
{% highlight python linenos %}
import gic.compress
gic.compress.compress(quality, dir)
{% endhighlight %}


[Contact Me](mailto:parsa@programmer.net)
