
def isValidInput(string):
    if string.find("+") != -1 or string.find("-") != -1 or string.find("*") != -1 or string.find(":") != -1
        if string.count("+") <= 1 or string.count("-") <= 1 or string.count("*") <= 1 or string.count(":") <= 1:
            return True
        else:
            return False
def calculate(string:str,sign:str):
    try:
        num1 = float(string[:string.find(sign)])
        num2 = float(string[string.find(sign)+1:])
        rez = 0
        if sign == "+":
            rez = num1+num2
        elif sign == "-":
            rez = num1-num2
        elif sign == "/":
            rez= num1/num2
        elif sign == "*":
            rez = num1*num2
        return rez

    except:
        pass
if__name__=="__main__":
    while True:
        chose = input("считаем или выходим").strip().lower()
        if chose == "считаем":
            viragenie = input("Введите выражение")
            if isValidInput(viragenie):
                sign = ""
                if viragenie.find("+") !=1:
                    sign = "+"
                elif viragenie.find("-") !=1:
                    sign = "-"
                elif viragenie.find(":") !=1:
                    sign = ":"
                elif viragenie.find("*") !=1:
                    sign = "*"
                num = calculate(viragenie,sign)
                print(f"{viragenie} = {num}")
            else:
                print("Некорректный формат выражения")
                continue
        elif chose == "выходим":
            break
    print("досвидания")