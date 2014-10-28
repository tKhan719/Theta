from arithmetics import Addition


def main():
    subject_dict = {'1': BasicArithmetics.basic_arith(), '2': Algebra.algebra(),
                    '3': BasicGeometry.basic_geo(), '4': Geometry.geometry(),
                    '5': Trigonometry.trigonometry(), '6': Calculus.calculus()}
    print """1) Basic Arithmetics\n2) Algebra\n3) Basic Geometry\n
    4) Geometry\n5) Trigonometry\n6) Calculus"""
    next = raw_input("> ")
    subject_dict[next]


class BasicArithmetics(object):

    def __init__(self):
        pass

    def basic_arith(self):
        sub_subject_dict = {'1': self.addition(), '2': self.subtraction(),
                            '3': self.multiplication(), '4': self.division()}
        print """1) Addition\n2) Subtraction\n 3) Multiplication\n 4)Division"""
        next = raw_input("> ")
        sub_subject_dict[next]

    def addition(self):
        addition_dict = {'1': Addition.addition_func('double', 'double'),
                         '2': Addition.addition_func('triple', 'triple'),
                         '3': Addition.addition_func('triple', 'double')}
        print """1) Double digits\n2)Triple digits\n3) Double-triple digits"""
        next = raw_input("> ")
        addition_dict[next]

    def subtraction(self):
        pass

    def multiplication(self):
        pass

    def division(self):
        pass


class Algebra(object):

    def __init__(self):
        pass

    def algebra(self):
        pass


class BasicGeometry(object):

    def __init__(self):
        pass

    def basic_geo(self):
        pass


class Geometry(object):

    def __init__(self):
        pass

    def geometry(self):
        pass


class Trigonometry(object):

    def __init__(self):
        pass

    def trigonometry(self):
        pass


class Calculus(object):

    def __init__(self):
        pass

    def calculus(self):
        pass


if __name__ == '__main__':
    main()
