class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return f"Rect({self.x1},{self.y1},{self.x2},{self.y2})"

    def perimeter(self):
        return (2 * (self.x2 - self.x1 + self.y2 - self.y1))

    def area(self):
        return ((self.x2 - self.x1) * (self.y2 - self.y1))

    def __eq__(self, other):
        if self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2:
            return True
        
        return False

    def __contains__(self, other):
        if self.x1 <= other.x1 and self.y1 <= other.y1 and self.x2 >= other.x2 and self.y2 >= other.y2:
            return True

        return False

    def __and__(self, other):
        prunik_x1 = self.x1
        prunik_y1 = self.y1
        prunik_x2 = self.x2
        prunik_y2 = self.y2

        if other.x1 > prunik_x1:
            prunik_x1 = other.x1

        if other.y1 > prunik_y1:
            prunik_y1 = other.y1

        if other.x2 < prunik_x2:
            prunik_x2 = other.x2

        if other.y2 < prunik_y2:
            prunik_y2 = other.y2
        
        if prunik_x1 < prunik_x2 and prunik_y1 < prunik_y2:
            return Rect(prunik_x1, prunik_y1, prunik_x2, prunik_y2)        
        else:    
            return Rect(0, 0, 0, 0)
