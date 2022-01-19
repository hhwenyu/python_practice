from prime.prime import Prime
import prime.constant as c
from email.email import Email

def run():
	print(c.START,c.FINISH)
	p = Prime(start = c.START, finish = c.FINISH)
	print(p.calculate_primes())
	prettier = p.prettify()
	print(prettier)
        
	new_mail = Email()
	new_mail.to = 'JohnDoe@email.com'
	new_mail.subject = f'Prime Numbers execution between {c.START} to {c.FINISH}'
	new_mail.body = prettier
	new_mail.send()

## this is the indicator for python package that this is the runner file instead of scripts
if __name__ == '__main__':
	run()
