"""
Algorithm to take the derivative of a polynomial
"""

#Polynomial defined as a_0 + a_1*x + a_2*x**2 + ....
def deriv_poly(poly):
	deriv = []
	for i in range(1,len(poly)):
		deriv.append(poly[i]*i)	
	return deriv

def print_poly(poly):
	string = ''
	for i in range(len(poly)):
		if i==0:
			string = '%f' %poly[i]
		else:
			temp = " + %fx^%d" %(poly[i], i)
			string = string + temp

	return string	


#      1 + 2x + 0 + 4x^3
poly = [1.0,2.0,0,4.0]
d_poly = deriv_poly(poly)

print "Polynomial"
print print_poly(poly)
print "Derivative of polynomial"
print print_poly(d_poly)
