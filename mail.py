import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("zeng.warlon@gmail.com", "7183596771aA")
msg = "HI!"
server.sendmail("zeng.warlon@gmail.com", "zeng.warlon@gmail.com", msg)
server.quit()
