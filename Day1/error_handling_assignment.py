


class FormulaError(Exception):
    def __init__(self, message = "raised FormulaError exception."):
        self.message = message
        super().__init__(self.message)


def calculate(input_str):
    input_split = input_str.split()
    print(input_split)
    if len(input_split) !=3:
        raise FormulaError("number of input is not equal to 3")
    try:
        num1 = float(input_split[0])
        num2 = float(input_split[2])
    except ValueError as value_error:
        raise FormulaError("String not convertable to float")
    input_operator = input_split[1]
    if input_operator  not in ['+', '-']:
        raise FormulaError("operator doesnt match with + or -")
    result  = num1 + num2 if input_operator == '+' else num1 - num2
    return result


def main():
    while True:
        input_str = input()
        if input_str == 'quit' or input_str ==  'QUIT':
            break
        result = calculate(input_str)    
        print(result)
    
if __name__ == "__main__":
    main()