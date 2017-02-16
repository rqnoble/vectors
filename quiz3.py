from vector import Vector
from math import acos
from math import degrees

A = Vector(['7.887', '4.138'])
B = Vector(['-8.802', '6.776'])
print A.dot(B)

C = Vector(['-5.955', '-4.904', '-1.874'])
D = Vector(['-4.496', '-8.755', '7.103'])
print C.dot(D)

W = Vector(['3.183', '-7.627'])
X = Vector(['-2.668', '5.319'])
print W.angle_with(X)

Y = Vector(['7.35', '0.221', '5.188'])
Z = Vector(['2.751', '8.259', '3.985'])
print Y.angle_with(Z, in_degrees=True)


