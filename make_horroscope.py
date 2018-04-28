import get_star_sign:


def make_horroscope_by_date_and_loc(date, location):

    star_sign = get_star_sign.get_star_sign(month, day)
    element, traits = get_star_sign.get_element(star_sign)
    modality, traits = get_star_sign.get_modality(star_sign)
    print '\n\nStar sign: ', star_sign, '\n\n' 
    print 'Element: ', element, '\t', traits
    print 'Modality: ', modality, '\t', traits

    #Get dictioanry of planets and their house and signs from Martin
    signs_and_houses = {"sun" : (taurus, 3),
			"moon" : (sagitarius, 3),
			"mercury" : (gemini, 2),
			"venus" : (taurus, 3),
			"mars" : (taurus, 1),
			"jupiter" : (taurus, 12),
			"saturn" : (taurus, 3),
			"uranus" : (taurus, 8),
			"neptune" : (taurus, 3,
			"pluto" : (taurus, 3)}
   



    return

def make_horroscope_by_name(name):

    #Get date and location of this person's birth
    date = 0
    location = 0
    make_horroscope_by_date_and_loc(date, location)

    return
