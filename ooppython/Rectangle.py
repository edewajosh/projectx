#! /usr/bin/env python3

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def output(self):
        return ("Length = " + str(self.length) + " Width = " + str(self.width))
        
    def compute(self):
    	return (self.width * self.length)

class Volume(Rectangle):
	def __init__(self,length, width, height):
		Rectangle.__init__(self, length, width)
		self.height = height

	def output(self):
		return ("Length = " + str(self.length) + " Width = " + str(self.width) + " Height = "+str(self.height))

	def compute(self):
		return (self.width * self.length * self.height)

rect1 = Rectangle(45,65)
box = Volume(10,15,20)
print(rect1.output())
print("Rectangle Area : " + str(rect1.compute()))
print(box.output())
print("Box Volume : " + str(box.compute()))