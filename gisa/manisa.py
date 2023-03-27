def number_to_word(number):
    try:
        x = int(number)
        return int_to_word(x)
    except ValueError:
        try:
            x = float(number)
            return float_to_word(x)
        except ValueError:
            print("Input is not a number")

def float_to_word(number):
    WORD_SPLIT = "faingo"
    integer_part, decimal_part = str(number).split('.')
    result = "{0} {2} {1}".format(int_to_word(int(integer_part)), int_to_word(int(decimal_part)),WORD_SPLIT)
    return result

def int_to_word(number, grade = [False, False]):
    if number == 0:
        return "aotra"
    
    units = ["iray", "roa", "telo", "efatra", "dimy", "enina", "fito", "valo", "sivy"]
    tens = ["folo", "roapolo", "telopolo", "efapolo", "dimapolo", "enimpolo", "fitopolo", "valopolo", "sivifolo"]
    hundreds = ["zato", "roanjato", "telonjato", "efajato", "dimanjato", "eninjato", "fitonjato", "valonjato", "sivinjato"]
    thousands = ["arivo", "alina", "hetsy"]
    big = ["tapitrisa","miliara","lavitrisa"]
    
    result = ""
    digits = [int(digit) for digit in str(number)][::-1]  # Convert number to list of digits and reverse order
    
    # print(' '.join(str(digits)))
    
    for i in range(len(digits)):
        digit = digits[i]
        if i == 0 and digit == 0:
            result = ""
        elif i == 0:
            result = units[digit-1]
        elif i == 1 and digit != 0:
            result = result + ( "" if result == "" else " ambiny " ) + tens[digit-1]
        elif i == 2 and digit != 0:
            if digit == 1 :
            	con = ( "" if result == "" else " ambiny " ) + hundreds[digit-1]
            else:
            	con = ( "" if result == "" else " sy " ) + hundreds[digit-1] # units[digit-1] + "-njato"
            result = result + con 
        elif i == 3 and digit != 0 and not (grade[0] or grade[1] ):
            con = ( "" if digit < 2 else units[digit-1] + " "  )
            result = result + ( "" if result == "" else " sy " ) + con + thousands[i-3]
        elif i == 4 and digit != 0 and not (grade[0]  or grade[1] ):
            result = result + ( "" if result == "" else " sy " ) + units[digit-1] + " " + thousands[i-3]
        elif i == 5 and digit != 0 and not (grade[0]  or grade[1] ):
            result = result + ( "" if result == "" else " sy " ) + units[digit-1] + " " + thousands[i-3]
        elif i == 6 and digit != 0 and not grade[0] :
            grade = [True, grade[1]]
            result = result + ( "" if result == "" else " sy " ) + int_to_word((number // 10**6)%10**9, grade) + " " + big[0]
        elif i == 9 and digit != 0 and not grade[1]:
            grade = [grade[0], True]
            result = result + ( "" if result == "" else " sy " ) + int_to_word((number // 10**i)%10**12, grade) + " " + big[1]
        elif i == 12 and digit != 0:
            result = result + ( "" if result == "" else " sy " ) + int_to_word(number // 10**12, [False,False]) + " " + big[2]
    return result
