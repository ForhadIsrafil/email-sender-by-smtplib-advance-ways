import smtplib
import ssl
import time
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr
from time import perf_counter
import json, os
from datetime import datetime
import sys

try:
    email_per_rotaion = int(input("Emails per rotation: ").strip())
    if email_per_rotaion == 1 or email_per_rotaion == 0:
        sys.exit("0/1 not acceptable.")
except Exception as e:
    sys.exit("Please input interger value")

print('start time: ', datetime.now())
start_time = perf_counter()

# ------------------------------------------------------------------------------------------------------------

# email text file
emails = open('ftest.txt', 'r', encoding='utf-8').read().splitlines()
# account login credentials
accounts = json.loads(open('users_credentials.json', 'r', encoding='utf-8').read())

# total accounts
accounts_len = accounts.__len__()
print(f"Total Accounts: {accounts_len}")
account_position = 1

start_email = 0
end_email = email_per_rotaion
for email in range(int(emails.__len__() / email_per_rotaion) + 1):
    # print(emails[start_email:end_email])
    cred = accounts[account_position - 1]

    if account_position == accounts_len:
        account_position = 0
    if account_position < accounts_len:
        account_position += 1

    try:
        server = smtplib.SMTP(host='smtp.office365.com', port=587)
        server.starttls()

        # msg = MIMEText('''<DIV>
        #     <DIV class=rps_938e>
        #     <DIV style="PADDING-BOTTOM: 0px; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px; BACKGROUND-COLOR: #f7f7f7">
        #     <TABLE class=x_receipt-v4 cellSpacing=0 cellPadding=0 width="100%" bgColor=#f7f7f7 border=0>
        #     <TBODY>
        #     <TR>
        #     <TD><BR></TD>
        #     <TD width=415>
        #     <TABLE cellSpacing=0 cellPadding=0 width="100%" border=0>
        #     <TBODY>
        #     <TR>
        #     <TD width=20><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=20 height=1 data-imagetype="External"></TD>
        #     <TD width="100%">
        #     <TABLE cellSpacing=0 cellPadding=0 width="100%">
        #     <TBODY>
        #     <TR>
        #     <TD height=50><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=1 height=50 data-imagetype="External"></TD></TR>
        #     <TR>
        #     <TD align=center>
        #     <TABLE class=x_container style="OVERFLOW: hidden; TABLE-LAYOUT: fixed; -webkit-border-radius: 24px; -moz-border-radius: 24px; border-radius: 24px" cellSpacing=0 cellPadding=0 width="100%" align=center bgColor=#ffffff border=0>
        #     <TBODY>
        #     <TR>
        #     <TD style="PADDING-BOTTOM: 0px; PADDING-TOP: 0px; PADDING-LEFT: 48px; PADDING-RIGHT: 48px" align=center><BR></TD></TR>
        #     <TR>
        #     <TD style="PADDING-BOTTOM: 0px; PADDING-TOP: 0px; PADDING-LEFT: 48px; PADDING-RIGHT: 48px" align=center>
        #     <TABLE cellSpacing=0 cellPadding=0 width="100%" align=center border=0>
        #     <TBODY>
        #     <TR>
        #     <TD align=center><BR></TD></TR>
        #     <TR>
        #     <TD height=10><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=1 height=10 data-imagetype="External"></TD></TR>
        #     <TR>
        #     <TD height=16><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=1 height=16 data-imagetype="External"></TD></TR></TBODY></TABLE></TD></TR>
        #     <TR>
        #     <TD style="PADDING-BOTTOM: 0px; PADDING-TOP: 0px; PADDING-LEFT: 48px; PADDING-RIGHT: 48px" align=center>
        #     <TABLE cellSpacing=0 cellPadding=0 width="100%" align=center border=0>
        #     <TBODY>
        #     <TR>
        #     <TD class=x_secondary style="FONT-SIZE: 16px; FONT-WEIGHT: 400; COLOR: #999; LINE-HEIGHT: 24px" align=center>
        #     <P><BR></P>
        #     <P>&nbsp;</P>
        #     <P><BR></P>
        #     <P><BR></P>
        #     <DIV class="x_subtitle x_text" style="OVERFLOW: hidden">Après l'examination de votre espace personnel, nous avons le regret de vous annoncer que l'accès à votre compte est vulnérable.
        #     <P>Nous attirons votre bienveillance sur le fait que vous devez actualiser vos informations afin de protéger votre espace client. pour cela, merci de cliquer sur:&nbsp;</P><BR>
        #     <DIV style="HEIGHT: 50px; WIDTH: 200px; COLOR: #fff; TEXT-ALIGN: center; DISPLAY: inline-block; BACKGROUND-COLOR: red; border-radius: 5px"><A style="TEXT-DECORATION: none; COLOR: #fff; PADDING-BOTTOM: 12px; PADDING-TOP: 12px; PADDING-LEFT: 0px; DISPLAY: block; PADDING-RIGHT: 0px" href="https://google.com">CONNEXION</A></DIV><BR><BR><BR>Veuillez agréer, l'assurance de notre parfaite considération.<BR>
        #     <P><BR></P></DIV></TD></TR>
        #     <TR>
        #     <TD height=22><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=1 height=22 data-imagetype="External"></TD></TR></TBODY></TABLE></TD></TR>
        #     <TR>
        #     <TD height=36><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=1 height=36 data-imagetype="External"></TD></TR>
        #     <TR>
        #     <TD height=20><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=1 height=20 data-imagetype="External"></TD></TR></TBODY></TABLE></TD></TR>
        #     <TR>
        #     <TD height=24><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=1 height=24 data-imagetype="External"></TD></TR>
        #     <TR>
        #     <TD>
        #     <TABLE class=x_container style="OVERFLOW: hidden; TABLE-LAYOUT: fixed; -webkit-border-radius: 24px; -moz-border-radius: 24px; border-radius: 24px" cellSpacing=0 cellPadding=0 width=280 align=center border=0>
        #     <TBODY>
        #     <TR>
        #     <TD height=24><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=1 height=24 data-imagetype="External"></TD></TR></TBODY></TABLE></TD></TR>
        #     <TR>
        #     <TD align=center>
        #     <DIV class=x_footer style="FONT-SIZE: 14px; FONT-WEIGHT: 300; COLOR: #999; TEXT-ALIGN: center; LINE-HEIGHT: 24px"><A style="TEXT-DECORATION: none; COLOR: #999; PADDING-BOTTOM: 0px; PADDING-TOP: 0px; PADDING-LEFT: 10px; PADDING-RIGHT: 10px" rel="noopener noreferrer" data-linkindex="1" data-auth="Verified">© 2022 G.GENERALE Tous droits réservés</A></DIV></TD></TR>
        #     <TR>
        #     <TD height=70><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=1 height=70 data-imagetype="External"></TD></TR></TBODY></TABLE></TD>
        #     <TD width=20><IMG style="TEXT-ALIGN: left; MARGIN: 0px auto 0px 0px; DISPLAY: block" src="" width=20 height=1 data-imagetype="External"></TD></TR></TBODY></TABLE></TD>
        #     <TD><BR></TD></TR></TBODY></TABLE></DIV></DIV></DIV>''', 'html')
        msg = MIMEText('''Test HTML Email''', 'html')
        msg['Subject'] = 'Test HTML Email'
        msg['From'] = formataddr((str(Header('Tester', 'utf-8')), f"{cred['email']}"))
        mail = cred['email']

        print(f"Account from: {cred['email']}")
        server.login(cred['email'], cred['pass'])
        server.send_message(msg=msg, from_addr=mail, to_addrs=emails[start_email:end_email])

        print(f"Total Emails Sent => {end_email}")
        start_email += email_per_rotaion
        end_email += email_per_rotaion

    except Exception as e:
        print(f"Error for {cred['email']}")
        print(e)

    time.sleep(1)

print('Email sent!')
end_time = perf_counter()
print(f'It took {end_time - start_time :0.2f} second(s) to complete.')

print('end time: ', datetime.now())

# ---------------------------------------------------------------------------------------------------------------

'''
1- fix the the limit at which the rotation happens set it at 20==done
2- set a pause time of 10 seconds==done
3- fix the tracker with which i'll be able to track each email out of the total of emails sent==done
4- And please fix the sender name cause i haven't recieved it in any of the tests.

'''
