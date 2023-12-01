class line:
    def __init__(self, line_string):
        self.line = line_string

    def first_digit(self):
        for char in self.line:
            if char.isdigit():
                return char
            
    def last_digit(self):
        for char in self.line[::-1]:
            if char.isdigit():
                return char

    def calibration_value(self):
        first = self.first_digit()
        last = self.last_digit()
        return int(first + last)
    
    def find_string_digits(self):
        digit_names = ["zero", "one", "two","three", "four","five", "six", "seven", "eight", "nine"]
        for num, name in enumerate(digit_names):
            self.line = self.line.replace(name, f"{name}{num}{name}")

class document:
    def __init__(self, input_list):
        self.lines = input_list

    def sum_of_calibration_values(self):
        total = 0
        for l in self.lines:
            my_line = line(l)
            # Part 2
            my_line.find_string_digits()
            # End of part 2
            total += my_line.calibration_value()
        return total
