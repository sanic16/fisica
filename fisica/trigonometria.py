from math import cos, sin, tan, pi, atan, asin, acos

class Math(object):
    PI = pi
    
    @classmethod
    def sin(cls, teta):
        return sin(cls.PI*teta/180)
    
    @classmethod
    def cos(cls, teta):
        return cos(cls.PI*teta/180)

    @classmethod
    def tan(cls, teta):
        return tan(cls.PI*teta/180)
    
    @classmethod
    def atan(cls, xy):
        return atan(xy)*(180/cls.PI)
    
    @classmethod
    def asin(cls, xy):
        return asin(xy)*(180/cls.PI)
    
    @classmethod
    def acos(cls, xy):
        return acos(xy)*(180/cls.PI)