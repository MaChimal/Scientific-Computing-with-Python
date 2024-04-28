"""Project 01: Arithmetic Formater"""


def validate_conditions(problems):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for problem in problems:
        num1, operator, num2 = problem.split()

        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
    
    return None

def arithmetic_arranger(problems, show_answers=False):
    if validate_conditions(problems):
        return validate_conditions(problems)

    first_line = ""
    second_line = ""
    lines = ""
    results = ""

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator == "+":
            result = int(num1) + int(num2)
        else:
            result = int(num1) - int(num2)

        max_value = max((num1, num2), key=len)
        underlines = "-" * (len(max_value) + 2)

        if max_value == num1:
            spaces = " " * (len(underlines)-(len(num2)+1))
            num1 = f"  {num1}    "
            num2 = f"{operator}{spaces}{num2}    "

        if max_value == num2:
            spaces = " " * (len(underlines)-len(num1))
            num1 = f"{spaces}{num1}    "
            num2 = f"{operator} {num2}    "
        
        first_line += num1
        second_line += num2
        lines += f"{underlines}    "
        results += f"{' ' * (len(underlines)-len(str(result)))}{result}    "
    
    if show_answers == True:
        problems = f"{first_line[:-4]}\n{second_line[:-4]}\n{lines[:-4]}\n{results[:-4]}"
    else:
        problems = f"{first_line[:-4]}\n{second_line[:-4]}\n{lines[:-4]}"

    return problems

if __name__ == "__main__":
    print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
