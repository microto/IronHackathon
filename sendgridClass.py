import sendgrid

# configuration:
username = 'korkile'
password = "hackathon1510"
fromEmail = "service@ironblock.com"
subject = "Firewall has been updated"

class sendgridClass(object):
	# sendEmail - will send over emails for all of the recipients
	# 	@param recipients 	- array - holds array of strings (email) to be send to
	#   @param ips 		 	- array - holds array of strings (IP's) to be send over

	def sendEmail(self, recipients = [] , ips = []):
		# make a secure connection to SendGrid
		s = sendgrid.Sendgrid(username, password, secure=True)

		ipsText = ', '.join(ips)

		html = """
			<html>
			  <head></head>
			  <body>
			  		The IP list has been updated:
			  		<br>
			  		""" + ipsText + """
			       	<br>
			       	Thanks, IronBlock
			  </body>
			</html>
			""";

		# make a message object
		message = sendgrid.Message(fromEmail, subject, "",
		    html)

		for recipientItem in recipients:
			# Add recipient to message
			message.add_to(recipientItem)

		# use the Web API to send your message
		s.web.send(message)
		return True;


# ---------------
# Demo how to Use
# ---------------

#mySendGrid = sendgridClass();

#recipients = []
#recipients.append('korkile@gmail.com')
#recipients.append('or@ironsrc.com')

#ips = []
#ips.append('10.0.2.255')
#ips.append('10.1.2.255')
#ips.append('10.2.2.255')

#mySendGrid.sendEmail(recipients,ips);
