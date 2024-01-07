def arithmetic_arranger(problems, show_answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(str(operand1)) > 4 or len(str(operand2)) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        formatted_operand1 = operand1.rjust(width)
        formatted_operand2 = operator + operand2.rjust(width-1)
        first_line += formatted_operand1 + '    '
        second_line += formatted_operand2 + '    '
        third_line += "-" * width + '    '

        if show_answer:
            if operator == "+":
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))

            formatted_answer = answer.rjust(width)
            fourth_line += formatted_answer + '    '

    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip()
    if show_answer:
        arranged_problems += "\n" + fourth_line.rstrip()

    return arranged_problems
