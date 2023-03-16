class Calculator:
    def calculate(expression):
        expression = expression.replace(" ", "")

        tokens = []
        current_token = ""

        for char in expression:
            if char.isdigit() or char == ".":
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)

        if current_token:
            tokens.append(current_token)
        
        output_queue = []
        operator_stack = []
        operator_precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

        for token in tokens:
            if token.isdigit() or "." in token:
                output_queue.append(float(token))
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack[-1] != "(":
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()
            elif token in operator_precedence:
                while operator_stack and operator_stack[-1] != "(" and operator_precedence[token] <= operator_precedence[operator_stack[-1]]:
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output_queue.append(operator_stack.pop())

        operand_stack = []
        for token in output_queue:
            if isinstance(token, float):
                operand_stack.append(token)
            elif token in operator_precedence:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    result = operand1 / operand2
                elif token == "^":
                    result = operand1 ** operand2

                operand_stack.append(result)

        print(str(result))
        return operand_stack[0]