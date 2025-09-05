''' Module  '''
import json
import os
from datetime import datetime



def calculation():
    ''' calculate functions '''
    while True:
        try:
            expression = input("Введи выражение: ").lower()
            if expression != "exit":
                num1, operation, num2 = expression.split()
                num1 = float(num1)
                num2 = float(num2)
                match operation:
                    case "+":
                        result = num1 + num2
                    case "-":
                        result = num1 - num2
                    case "*":
                        result = num1 * num2
                    case "/":
                        result = num1 / num2
                    case "**":
                        result = num1 ** num2
                    case "%":
                        result = num1 % num2
                    case "//":
                        result = num1 // num2
                print(result)
                dat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file_path = "calc.json"
                resultt = {
                    "результат": result,
                    "выражение": expression,
                    "дата_время": dat
                }
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8") as file:
                        history = json.load(file)
                else:
                    history = []
                history.append(resultt)
                with open (file_path, "w", encoding="utf-8") as file:
                    json.dump(history, file, ensure_ascii=False, indent=4)
            else:
                exit(0)
        except Exception as e:
            print(f'Произошла ошибка: {e}')
            continue

calculation()
