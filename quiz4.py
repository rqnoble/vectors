from vector import Vector

a = Vector(['-7.579', '-7.88'])
b = Vector(['22.737', '23.64'])
print " p 1 "
print a.is_parallel_to(b)
print a.is_orthogonal_to(b)
print 

print " p 2 "
a = Vector(['-2.029','9.97','4.172'])
b = Vector(['-9.231','-6.639','-7.245'])
print a.is_parallel_to(b)
print a.is_orthogonal_to(b)
print 


a = Vector(['-2.328','-7.284','-1.214'])
b = Vector(['-1.821','1.072','-2.94'])
print " p 3 "
print a.is_parallel_to(b)
print a.is_orthogonal_to(b)
print 


a = Vector(['2.118','4.827'])
b = Vector(['0','0'])
print " p 4 "
print a.is_parallel_to(b)
print a.is_orthogonal_to(b)
print 


