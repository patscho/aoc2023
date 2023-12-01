from line import line, document

FILE = "day01/input.txt"

def read_input(filename):
    with open(filename) as file:
        my_input = [x.strip() for x in file.readlines()]
    return my_input

def main():
    my_input = read_input(FILE)
    doc = document(my_input)
    print(doc.sum_of_calibration_values())


if __name__ == "__main__":
    main()
