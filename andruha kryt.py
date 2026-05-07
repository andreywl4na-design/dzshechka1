def calculator(func):
    def wrapper(expression):
        try:

            expression = expression.replace("^", "**")


            result = func(expression)

            return result

        except ZeroDivisionError:
            return "Помилка: ділення на нуль"

        except SyntaxError:
            return "Помилка: неправильний вираз"

        except NameError:
            return "Помилка: недопустимі символи у виразі"

        except Exception as e:
            return f"Помилка: {e}"

    return wrapper


@calculator
def calculate(expression):
    return eval(expression)



print(calculate("2 + 3 * 4"))
print(calculate("(10 + 5) / 3"))
print(calculate("2 ^ 3"))
print(calculate("10 / 0"))
print(calculate("2 +"))