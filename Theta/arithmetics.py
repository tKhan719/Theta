from random import randint


class BasicOperators(object):

    digit_dict = {'single': randint(0, 9),
                  'double': randint(10, 99),
                  'triple': randint(100, 999)}

    def check_ans(self):
        if int(self.userAnswer) == self.answer:
            print "\nCorrect!"
        else:
            print "\nWrong. Correct answer is:", self.answer

    def get_numbers(self, digit):
        number = self.digit_dict[digit]
        return number


class Addition(BasicOperators):

    def addition_func(self, digit1, digit2):
        number1 = self.get_numbers(digit1)
        number2 = self.get_numbers(digit2)
        self.answer = number1 + number2
        self.userAnswer = raw_input('%d + %d = ' % (number1, number2))
        self.check_ans()


class Subtraction(BasicOperators):
    # Needs some work...

    def __init__(self, neg):
        self.neg = neg

    def get_subtr_numbers(self, digit):
        # Continue working on getting non-negative numbers.
        pass

    def subtraction_func(self, digit1, digit2):
        number1 = self.get_numbers(digit1)
        number2 = self.get_numbers(digit2)
        self.answer = number1 - number2
        self.userAnswer = raw_input('%d - %d = ' % (number1, number2))
        self.check_ans()


class Multiplication(BasicOperators):

    def __init__(self):
        # Put some code about what type of mult you want
        pass

    def mult_func(self):
        self.answer = self.digit1 * self.digit2
        self.userAnswer = raw_input('%d\nx %d' % (self.digit1, self.digit2))
        self.check_ans()


class Division(BasicOperators):

    def __init__(self):
        # Put some code about what type of div you want
        pass

    # Some functions of division


if __name__ == '__main__':
    y = BasicOperators('double')
    x = Addition()
    x.addition_func()
