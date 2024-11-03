class Calculator:
    def __init__(self):
        self.last_result = 0
        self.history = []
        self.max_history = 10
        self.operation_symbols = {
            'addition': '+',
            'subtraction': '-',
            'multiplication': 'x',
            'division': '÷'
        }


    def _add_to_history(self, operation, args, result):
        entry = {
            'operation': operation,
            'numbers': args,
            'result': result
        }
        self.history.append(entry)
        if len(self.history) > self.max_history:
            self.history.pop(0)


    def subtraction(self, *args):
        if len(args) < 2:
            raise ValueError("You should provide at least two numbers")
        self.last_result = args[0]
        for num in args[1:]:
            self.last_result -= num
        self._add_to_history('subtraction', args, self.last_result)
        return self.last_result


    def addition(self, *args):
        self.last_result = sum(args)
        self._add_to_history('addition', args, self.last_result)
        return self.last_result


    def multiplication(self, *args):
        self.last_result = 1
        for num in args:
            self.last_result *= num
        self._add_to_history('multiplication', args, self.last_result)
        return self.last_result


    def division(self, *args):
        if len(args) < 2:
            raise ValueError("You should provide at least two numbers")
        self.last_result = args[0]
        for num in args[1:]:
            self.last_result /= num
        self._add_to_history('division', args, self.last_result)
        return self.last_result


    def square_root(self, num):
        if num < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        self.last_result = num ** 0.5
        self._add_to_history('square_root', (num,), self.last_result)
        return self.last_result
    
    def view_history(self):
        if not self.history:
            return "No calculations in history."
        
        formatted_history = []
        for entry in self.history:
            if entry['operation'] == 'square_root':
                formatted_entry = f"√{entry['numbers'][0]} = {entry['result']}"
            else:
                symbol = self.operation_symbols[entry['operation']]
                numbers_str = f" {symbol} ".join(str(num) for num in entry['numbers'])
                formatted_entry = f"{numbers_str} = {entry['result']}"
            formatted_history.append(formatted_entry)
        
        return '\n'.join(formatted_history)
    
    def clear_history(self):
        self.history = []
        return "History cleared."

    def get_last_calculation(self):
        if not self.history:
            return "No calculations in history."
        entry = self.history[-1]
        if entry['operation'] == 'square_root':
            return f"Last calculation: √{entry['numbers'][0]} = {entry['result']}"
        symbol = self.operation_symbols[entry['operation']]
        numbers_str = f" {symbol} ".join(str(num) for num in entry['numbers'])
        return f"Last calculation: {numbers_str} = {entry['result']}"

if __name__ == "__main__":
    calc = Calculator()

    # Addition
    print(calc.addition(10, 20, 30))      # Output: 60

    # Multiplication
    print(calc.multiplication(2, 3, 4))   # Output: 24

    # Square Root
    print(calc.square_root(16))           # Output: 4.0

    # View History
    print(calc.view_history())

    # Get Last Calculation
    print(calc.get_last_calculation())

    # Clear History
    print(calc.clear_history())
