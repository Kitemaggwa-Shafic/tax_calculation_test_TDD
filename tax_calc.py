# Tax calculation logic

def cal_tax(earnings):
    # tax =0
    if(earnings <= 12000):
        tax = 0
        return tax
    elif (earnings > 12000 and earnings <= 36000):
        tax = (0.2)
        return tax
