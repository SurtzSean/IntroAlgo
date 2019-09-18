#line segment cannot have multiple y values for each x value.
class Line_Segment:
	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0
	slope = 0
	def __init__(self, x1,x2,y1,y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.slope = (self.y2-self.y1)/(self.x2-self.x1)
	def calc_y_int(self):
		return self.y1-self.x1*self.slope

#checks if y is between x and z
def is_between(x,y,z):
	if(x<=y and z>=y):
		return True
	else:
		return False

#finds whether there is an intersection
def find_intersection(ls1,ls2):
	if ls1.slope == ls2.slope:
		if ls1.calc_y_int() - ls2.calc_y_int() == 0:
			if(is_between(ls1.x1,ls2.x1,ls1.x2) or is_between(ls2.x1,ls2.x2,ls1.x2)):
				return True
	else:
		#what the point of intersection is or would be if it was a function y=mx+b
		x = (ls1.calc_y_int() - ls2.calc_y_int())/(ls2.slope - ls1.slope)
		if is_between(ls1.x1,x,ls1.x2) and is_between(ls2.x1,x,ls2.x2):
			return True
	return False

#creates object
def make_line_segment(x1,x2,y1,y2):
	if x1>x2:
		x1,x2 = x2,x1
	ls = Line_Segment(x1,x2,y1,y2)
	return ls

#main
if __name__ == '__main__':
	line_one = input("Enter points seperated by commas for line 1 in the order x1,x2,y1,y2 \n").split(',')
	line_two = input("Enter points seperated by commas for line 2 in the order x1,x2,y1,y2 \n").split(',')
	line_one = list(map(float, line_one))
	line_two = list(map(float, line_two))
	ls1 = make_line_segment(line_one[0],line_one[1],line_one[2],line_one[3])
	ls2 = make_line_segment(line_two[0],line_two[1],line_two[2],line_two[3])
	if(find_intersection(ls1,ls2)):
		print("There is an intersection.")
	else:
		print("no intersection")
	k=input('press close to exit')