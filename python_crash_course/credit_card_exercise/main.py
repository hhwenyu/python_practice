## hide credit card number
# provide a functionshould replace the first 12 digits, of the given number witrh *, display only the last 4 digits
# final format should like **** **** **** 3456


def is_credit_card(cc_number: str):
        if len(cc_number) == 16: return True
        return False

def hide_cc_num(cc_number: str):
	## first check if the given number followed the 16 convention cc number
	if is_credit_card(cc_number):
		#return "**** **** **** " + cc_number[-4:]
		return f"**** **** **** {cc_number[-4:]}"
#print(hide_cc_num('1234567890123456'))

def hide_ccards(cards : list):
	res = []
	for card in cards:
		if is_credit_card(card):
			res.append("**** **** **** " + card[-4:])	
		else:
			assert len(card)== 16, 'digits are not length of 16' & exit(1)	
	return res
print(hide_ccards(['1234567890123456','98765432109876540']))
