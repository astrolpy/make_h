def get_star_sign(month, day):

    if month == 1:
	if day < 20:
	    star_sign = 'capricorn'
	else:
    	    star_sign = 'aquarius'
    elif month == 2:
	if day < 19:
	    star_sign = 'aquarius'
	else:
    	    star_sign = 'pisces'
    elif month == 3:
	if day < 21:
	    star_sign = 'pisces'
	else:
    	    star_sign = 'aries'
    elif month == 4:
	if day < 20:
	    star_sign = 'aries'
	else:
    	    star_sign = 'taurus'
    elif month == 5:
	if day < 21:
	    star_sign = 'taurus'
	else:
    	    star_sign = 'gemini'
    elif month == 6:
	if day < 21:
	    star_sign = 'gemini'
	else:
    	    star_sign = 'cancer'
    elif month == 7:
	if day < 23:
	    star_sign = 'cancer'
	else:
    	    star_sign = 'leo'
    elif month == 8:
	if day < 23:
	    star_sign = 'leo'
	else:
    	    star_sign = 'virgo'
    elif month == 9:
	if day < 23:
	    star_sign = 'virgo'
	else:
    	    star_sign = 'libre'
    elif month == 10:
	if day < 23:
	    star_sign = 'libre'
	else:
    	    star_sign = 'scorpio'
    elif month == 11:
	if day < 22:
	    star_sign = 'scorpio'
	else:
    	    star_sign = 'sagittarius'
    elif month == 12:
	if day < 22:
	    star_sign = 'sagittarius'
    else:
        star_sign = 'capricorn'

    return star_sign

def get_element(star_sign):

    if (star_sign == 'aries') or (star_sign == 'leo') or (star_sign == 'sagittarius'):
	element = 'fire'
	traits = 'Enthusiasm; drive to express self; faith'
    elif (star_sign == 'gemini') or (star_sign == 'libra') or (star_sign == 'aquarius'):
	element = 'air'
 	traits = 'Communication; socialization; conceptualization'
    elif (star_sign == 'taurus') or (star_sign == 'virgo') or (star_sign == 'capricorn'):
	element = 'earth'
	traits = 'Practicality; caution; material world'
    else:
 	element = 'water'
	traits = 'Emotion; empathy; sensitivity'

    return element, traits

day = 10
for month in range(1,13):
    star_sign = get_star_sign(month, day)
    element, traits = get_element(star_sign)
    print star_sign, element, traits


















print get_star_sign(6, 19)
