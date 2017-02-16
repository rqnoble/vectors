from vector import Vector


v = Vector([8.218,-9.341])
vv = Vector([-1.129,2.111])
print v.plus(vv)


v = Vector([7.119,8.215])
vv = Vector([-8.223,0.878])
print v.minus(vv)

v = Vector([1.671,-1.012,-0.318])
c = 7.41
print v.times_scalar(c)
