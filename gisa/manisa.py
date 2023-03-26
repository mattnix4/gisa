def number_to_word(number, grade = 0):
    if number == 0:
        return "aotra"
    if number >= 10**13:
    	print("Gisa mainty")
    	return
    
    units = ["iray", "roa", "telo", "efatra", "dimy", "enina", "fito", "valo", "sivy"]
    tens = ["folo", "roapolo", "telopolo", "efapolo", "dimapolo", "enimpolo", "fitopolo", "valopolo", "sivipolo"]
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
        elif i == 3 and digit != 0 and grade < i:
            con = ( "" if digit < 2 else units[digit-1] + " "  )
            result = result + ( "" if result == "" else " sy " ) + con + thousands[i-3]
        elif i == 4 and digit != 0 and grade < i:
            result = result + ( "" if result == "" else " sy " ) + units[digit-1] + " " + thousands[i-3]
        elif i == 5 and digit != 0 and grade < i:
            result = result + ( "" if result == "" else " sy " ) + units[digit-1] + " " + thousands[i-3]
        elif i == 6 and digit != 0 and grade < i:
            result = result + ( "" if result == "" else " sy " ) + number_to_word(number // 10**6, i) + " " + big[0]
        elif i == 9 and digit != 0 and grade < i:
            result = result + ( "" if result == "" else " sy " ) + number_to_word(number // 10**i, i) + " " + big[1]
        elif i == 12 and digit != 0:
            result = result + ( "" if result == "" else " sy " ) + number_to_word(number // 10**i, 0) + " " + big[2]
    return result
