This python script simulates the packing of various sizes rectangles into a bin which can have any size. It doesn't give the optimal solution for every instances, but it's approximately optimal, the average wasted space is about 5-6%.

Documentation link from where the strategy was taken.
https://www.researchgate.net/publication/228974015_Optimizing_Three-Dimensional_current_bin_Packing_Through_Simulation
Consider that the strategy and the algorithm from the link have been changed for my needs, but it can be adapted for your needs.
    
For this code the dimensions need to be integers and items are rectangulars. The unpacked items remain in notPacked list, if they can't fit in the container.

