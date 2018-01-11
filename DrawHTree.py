#https://www.pramp.com/challenge/EmYgnOgVd4IElnjAnQqn
import matplotlib.pyplot as plt

def drawLine(x0,y0,x1,y1):
    plt.plot([x0,x1],[y0,y1])


def drawHTree(x,y,length,depth):
    if depth == 0 or length <= 0:
        return None
    
    x0 = x-length/2
    x1 = x+length/2
    y0 = y-length/2
    y1 = y+length/2

    #left
    drawLine(x0,y0,x0,y1)
    #right
    drawLine(x1,y0,x1,y1)
    #middle
    drawLine(x0,y,x1,y)

    newLength = length/2**0.5

    drawHTree(x0,y0,newLength,depth-1)
    drawHTree(x0,y1,newLength,depth-1)
    drawHTree(x1,y0,newLength,depth-1)
    drawHTree(x1,y1,newLength,depth-1)

drawHTree(0,0,30,2)
plt.show()
