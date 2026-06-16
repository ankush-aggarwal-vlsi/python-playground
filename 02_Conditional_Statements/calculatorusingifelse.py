# 49 program CALCULATOR USING IF-ELSE 
x = input("ENTER THE FIRST NUMBER : ")
y = input("ENTER THE SECOND NUMBER : ")
operator = input("ENTER THE OPERATOR ('+','-','/','*','%') : ")
output = None
if x.isdigit() and y.isdigit() :
    x = int(x)
    y = int(y)
    if operator == "/" :
        if y != 0 :
            output = x / y
        else :
            print("DENOMINATOR CANNOT BE ZERO") 
    elif operator == "+" :
        output = x + y
    elif operator == "-" :
            output = x - y 
    elif operator == "*" :
        output = x * y
    elif operator == "%" :
        output = (x*y)/100
    else :
        print("SELECT THE OPERATOR BETWEEN ('+','-','/','*','%')")
else :
    print("PLEASE ENTER CORRECT VALUES")
if output is not None :
    print("THE ANSWER WILL BE :",output)

        
