# 47 program PROFIT AND LOSS
CP = input("ENTER THE COST PRICE OF GOODs (in Rs.) : ")
SP = input("ENTER THE SELLING PRICE OF GOODs (in Rs. ) : ")
if  CP.isdigit() and SP.isdigit() :
    CP = int(CP)
    SP = int(SP)
    if SP > CP :
        profit = SP - CP
        print("THE PROFIT WILL BE",profit)
    elif CP > SP :
        loss = CP - SP
        print("THE LOSS WILL BE",loss)
    elif CP == SP :
        print("NO PROFIT NO LOSS.")
    else :
        print("INVALID DATA.")
else :
    print("ENTER VALID PRICES (in Rs).")