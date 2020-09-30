import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from'] = 'varshini reddy'
email['to'] = 'fun@gmail.com'
email['subject'] = 'hey'

email.set_content('I have sent this without actually using my gmail account.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls() 
	smtp.login('crazy@gmail.com', 'abcdefghi')
	smtp.send_message(email)
	print('all good boss!')

