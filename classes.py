# volume/ area Calculator of some shapes

class Dimensions:
	def __init__(self, length, width, height, radius):
		self.length = length
		self.width = width
		self.height = height
		self.radius = radius

	def areaS(self):
		return self.radius**2 * 3.14 *4
	def volS(self):
		return self.radius**3 * 3.14 *(4/3)
	def areaQ(self):
		return 2*(self.length * self.width + self.length * self.height + self.width * self.height)
	def volQ(self):
		return self.length * self.width * self.height

class Sphere(Dimensions):
	def __init__(self, radius):
		super().__init__(radius, radius, radius, radius)

class Rectangle(Dimensions):
	def __init__(self, length, width, height):
		super().__init__(length, width, height, height)


#x=Dimensions(5,0,0,12)
x=Sphere(4)
y=Rectangle(2,3,6)

x.areaS
print('area and volume of sphere with radius 4')
print(x.areaS())
print(x.volS())
print('\narea and volume of rectangle with LWH of 2x3x6')
print(y.areaQ())
print(y.volQ())