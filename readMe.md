# 3D bin-packing - text based python script
Simple python script that simulates the packaging of rectangular boxes of any size.
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Purpose](#purpose)
* [Examples of use](#examples-of-use)
* [Sources](#sources)
* [Other information](#other-information)
## General info
This simple and intuitive script allows you to use the **3D bin-packing simulation** in an easier way.
By writing the right keyword you can launch a certain action (like _create bin, add item, pack items_,..).
<br />
You can find the algorithm and objects (_Bin, Item, Item_List_) in __3dbp.py_, 
run _text_based_script.py_ for a simple **terminal UI** and 
check _examples_ directory if you want to see some examples about how can you use the code in your projects.
<br />
The algorithm doesn't offer the **optimal solution** sometimes but the average wasted space is below 5% which is pretty good for my needs (given that it's a NP hard problem).
#### Graphical version
Also, I developed a graphic version of **3D bin-packing** that uses the algorithm mentioned above.
<br />
[3D Bin Packing Graphic Version](https://github.com/DragosCosmin2000/3D-Bin-Packing-Python-Application)
## Technologies
* Python 3.8.3
* Modules:
    - copy
    - math
## Setup
Bin and Items dimensions need to be positive integers.
<br />
_python text_based_script.py_ - to run the terminal UI
## Purpose
This open source project is meant to provide an approximately optimal solution for the 3D bin packing problem.
<br />
It can be used for various things:
- deposit space management
- cargo vehicle space management (keep in mind that this algorithm doesn't take into account the boxes weight)
- others (**Example**: I needed it for a game feature)
## Examples of use
You can see some example code in example scripts from **examples** directory.
<br />
As I mentioned I already developed a graphic version of **3D bin-packing** (check here [3D Bin Packing Graphic Version](https://github.com/DragosCosmin2000/3D-Bin-Packing-Graphic-Version)).
<br />
But if you don't want to install the packages or to use the executable, you can represent the output data by yourself:
- Use pen and paper (kind of weird and not environmentally friendly:), I don't recommend)
- Use a 3D modeling web application (Example: [SketchUp](https://app.sketchup.com/app))
- Use some unusual ways (lego pieces, cubic shapes)
## Sources
The strategy is based on Erick Dube and Leon Reeves Kanavathy research [Optimizing Three-Dimensional Bin Packing Through Simulation](https://www.researchgate.net/publication/228974015_Optimizing_Three-Dimensional_Bin_Packing_Through_Simulation)
## Other information
#### Contact
* **gmail**: tudorachedragos2k@gmail.com
* **linkedin**: [My linkedin](https://www.linkedin.com/in/dragos-tudorache-8b15131b5/)
