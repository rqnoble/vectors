from vector import Vector

v = Vector(['3.039', '1.879'])
b = Vector(['0.825', '2.036'])
print " proj of V onto b "
print v.project_onto(b)

v = Vector(['-9.88', '-3.264', '-8.159'])
b = Vector(['-2.155', '-9.353', '-9.473'])
print "v perp"
print v.component_orthogonal_to(b)

v = Vector(['3.009', '-6.172', '3.692', '-2.51'])
b = Vector(['6.404', '-9.144', '2.759', '8.718'])
print "V is equal to:"
print v.project_onto(b)
print "plus"
print v.component_orthogonal_to(b)