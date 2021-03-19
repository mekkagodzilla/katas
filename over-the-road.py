'''
You've just moved into a perfectly straight street with exactly n identical houses
on either side of the road. 
Naturally, you would like to find out the house number of the people on the other side of the street. 
The street looks something like this:

1|   |6
3|   |4
5|   |2
 
Given your house number address and length of street n, 
give the house number on the opposite side of the street.
'''

def over_the_road(address, n):
    return ( 2 * n ) +1 - address


