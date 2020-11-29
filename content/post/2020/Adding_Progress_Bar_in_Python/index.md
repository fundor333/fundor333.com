---
title: "Adding Progress Bar in Python"
date: 2020-11-30T13:24:20+01:00
feature_image: "Adding_Progress_Bar_in_Python.jpg"
feature_link: "https://unsplash.com/photos/BKfsCuFQ5R8"
feature_text: "Photo by Najib Kalil on Unsplash"
tags:
- python
- coding
- devops
slug: "Adding Progress Bar in Python"
categories: 
description: "Sometime you need to add a Progress Bar to your script and this is how"
type: "post"
---

Sometime you need to make a script or a program with some task and show to the user you are doing something so you need to write something as output: a Progress Bar.

You have multiple way to do it and now I will show some way to do it with packages.

# Progress

The first package I present is __[progress](https://github.com/verigak/progress)__, an easy python package with a lot of configuration.

![Progress.py gif](progress.gif)

This package is base of one object, the __Bar__, and you set it, you use it for update the progressbass or end it.

## For example

You have this _base_ code:

~~~python 
from time import sleep

for i in range(100):
	sleep(1)
	print(i)
~~~

This code print the first 100 number one for row. If I want to use a progress's progress bar I need to to something like this:

~~~ python
from time import sleep
from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(100):
	sleep(1)
	print(i)
	bar.next()
bar.finish()
~~~ 

This is a base version of the code for a _bar_ but you can add a lot of configs like suffix, max value, remaing and other things.[^1]

# Progressbar2

This is a package wich use iterators for working. You can also create custo widgets (or bars) for creating your custom expirences.

## Example

Using the example code

~~~ python
from time import sleep
import progressbar

for i in progressbar.progressbar(range(100)):
	sleep(1)
	print(i)
~~~ 

you can have a progress bar using an iterator.
If you need to edit the navbar you can make a custom widgets like the next example

~~~ python
from time import sleep
import progressbar

widgets=[
    ' [', progressbar.Timer(), '] ',
    progressbar.Bar(),
    ' (', progressbar.ETA(), ') ',
]

for i in progressbar.progressbar(range(100), widgets=widgets):
	sleep(1)
	print(i)
~~~

This is a custom output for the progress bar following the docs find in the project documentation[^2]

# TQDM

THe fastest one for install and a very easy one.

![Tqdm.py gif](tqdm.gif)

Not huge for the customizing part but a good one. It also skip unnecessary iteration displays.

## Example

Allwayse with our lovely code:

~~~ python
from time import sleep
from tqdm import tqdm

for i in tqdm(range(100)):
	sleep(1)
	print(i)
~~~

Here[^3] for the docs.

# Alive progress

This is the fancy package for progress bar. 

![Alive gif](alive-progress.gif)

If you need a fancy progress bar this is the best one.

## Example

With our favorite example this is an example

~~~ python
from time import sleep
from alive_progress import alive_bar

items = range(100)              
with alive_bar(len(items)) as bar:  
	for i in items:
		sleep(1)
		print(i) 
		bar()                
~~~

With the correct config[^4] you can have some of the best animation ever.

![Alive loading gif](showtime-spinners.gif)

Wich progress bar is your favorite?

[^1]: [Progress, easy progress reporting for Python](https://github.com/verigak/progress/)
[^2]: [Progressbar2, A Python Progressbar library to provide visual (yet text based) progress to long running operations.](https://pypi.org/project/progressbar2/)
[^3]: [Tqdm](https://tqdm.github.io/)
[^4]: [Alive-Progress, A new kind of Progress Bar, with real-time throughput, eta and very cool animations!](https://github.com/rsalmei/alive-progress)
