import math
class Rectangle:
    def __init__(self, h, w):
        self.h = int(h)
        self.w = int(w)

        def is_square():
            if h == w:
                return True
            else:
                return False

        def diagonal_len():
            square_c = int((h*h)) + int((w*w))
            c = math.sqrt(int((square_c)))
            return c

        def height():
            return h

        def width():
            return w

        def area():
            area = (h*2) *2
            return area

        def perimeter():
            perimeter = (h * 2) + (w * 2)
            return perimeter

        is_square(), diagonal_len(), height(), width(), area(), perimeter()
