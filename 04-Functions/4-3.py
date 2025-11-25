###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a,b,c):
    s= (1/2)*(a+b+c)
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return Area

wynik1= triangle_area(3,4,5)
wynik2= triangle_area(5,12,13)

print(f'The area of ​​a triangle with sides (3,4,5) is {wynik1}')
print(f'The area of ​​a triangle with sides ... is {wynik2}')
print('The area of ​​a triangle with sides ... is ...')


# nie dokonczone trzeba  z petla for