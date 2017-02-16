from math import sqrt, acos, pi
from decimal import Decimal, getcontext


getcontext().prec = 10

class Vector(object):

        CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize zero vector'
        NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique prallel component'
        NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'No unique orthogonal component'

	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple([Decimal(x) for x in coordinates])
			self.dimension = len(self.coordinates)

		except ValueError:
			raise ValueError('The coordinates must be nonempty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable')

	def magnitude(self):
		coordinates_squared = [x**2 for x in self.coordinates]
		return sqrt(sum(coordinates_squared))

	def normalize(self):
		try:
			magnitude = self.magnitude()
			return self.times_scalar(Decimal(1.0/magnitude))
		except ZeroDivisionError:
			return 0
			#raise Exception('Cannot normalize the zero vector')

	def plus(self, v):
		new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def minus(self, v):
		new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def times_scalar(self, c):
		new_coordinates = [Decimal(c)*x for x in self.coordinates]
		return Vector(new_coordinates)

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	def __eq__(self, v):
		return self.coordinates == v.coordinates


	def dot(self, v):
	        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])


        def angle_with(self, v, in_degrees=False):
            try:
                u1 = self.normalize()
                u2 = v.normalize()
                angle_in_radians = acos(u1.dot(u2))

                if in_degrees:
                    degrees_per_radian = 180. / pi
                    return angle_in_radians * degrees_per_radian 
                else:
                    return angle_in_radians

            except Exception as e:
                if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                    raise Exception('Cannot compute anangle with the zero vector')
                else:
                    raise e



	def is_orthogonal_to(self, v, tolerance=1e-10):
		return abs(self.dot(v)) < tolerance

	def is_parallel_to(self, v):
		return ( self.is_zero() or
			v.is_zero() or
			self.angle_with(v) == 0 or
			self.angle_with(v) == pi )

	def is_zero(self, tolerance=1e-10):
		return self.magnitude() < tolerance

	def times_scalar(self, c):
		new_coordinates = [Decimal(c)*x for x in self.coordinates]
		return Vector(new_coordinates)

	def project_onto(self, b):
		try:
			U = b.normalize()
			weight = self.dot(U)
			return U.times_scalar(weight)

		except Exception as e:
			if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
				raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
			else:
				raise e

	def component_orthogonal_to(self, b):
		try:
			projection = self.project_onto(b)
			return self.minus(projection)

		except:
			if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
				raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
			else:
				raise e

	def cross_product(self, b):
		x = self.coordinates[1] * b.coordinates[2] - b.coordinates[1] * self.coordinates[2]
		y = -1 * (self.coordinates[0] * b.coordinates[2] - b.coordinates[0] * self.coordinates[2])
		z = self.coordinates[0] * b.coordinates[1] - b.coordinates[0] * self.coordinates[1]
		return Vector([x, y, z])

	def area_of_parallelogram(self, w):
		cp = self.cross_product(w)
		area = cp.magnitude()
		return area

	def area_of_triangle(self, w):
		AoP = self.area_of_parallelogram(w)
		return AoP * 0.5