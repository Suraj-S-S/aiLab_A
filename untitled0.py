# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 11:49:53 2023

@author: 20pt04
"""

class Point():
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
        
def regionCode(lb,tr,p):
    code=[0,0,0,0]
    code[2]=int(p.x>tr.x)
    code[3]=int(p.x>lb.x)
    code[1]=int(p.y>lb.y)
    code[0]=int(tr.y>p.y)
    print(code)        
        
leftBottom=Point(2,9)
topRight=Point(9,10)


l1=Point(5,10)
l2=Point(11,9)

regionCode(leftBottom,topRight,l1)
regionCode(leftBottom,topRight,l2)


        