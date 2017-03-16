class Matrix:
	def __init__(self, first, second, third, fourth):
		self.f= first;
		self.s= second;
		self.t= third;
		self.fo=fourth;
	@staticmethod
	def add(matriz):
		one=self.f+matriz.f;
		two=self.s+matriz.s;
		three=self.t+matriz.t;
		four=self.fo+matriz.fo;
		return Matrix(one,two,three,four);
	

matrix_1 = Matrix(4,5,6,7);
matrix_2 = Matrix(2,2,2,1);
matrix_3 = matrix_2.add(matrix_1);

