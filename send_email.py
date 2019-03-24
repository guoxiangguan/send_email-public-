from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib
class Email():
    def __init__(self):
        print('send_email(from_addr,password,to_addr,smtp_server,mimetext,msg_from,msg_to,msg_subject)')
    def format_addr(self,s):
        name,addr = parseaddr(s)
        return formataddr((Header(name,'utf-8').encode(),addr))
    def send_email(self,from_addr='你的发件箱账户',password='你的发件箱密码',to_addr='收件箱账户',smtp_server='邮箱服务器',mimetext=None,msg_from='发件人称呼',msg_to='收件人称呼',msg_subject=None):
        msg = MIMEText(mimetext,'plain','utf-8')
        msg['From'] = self.format_addr(msg_from+' '+'<%s>'%from_addr)
        msg['To'] = self.format_addr(msg_to+' '+'<%s>'%to_addr)
        msg['Subject'] = Header(msg_subject,'utf-8').encode()
        server = smtplib.SMTP(smtp_server,25)
        server.login(from_addr,password)
        server.sendmail(from_addr,[to_addr],msg.as_string())
        server.quit()


if __name__ == '__main__':

    from_addr = input('From: ')
    password = input('Password: ')
    to_addr = input('To: ')
    smtp_server = input('SMTP server: ')
    mimetext = input('text: ')
    msg_from = input('发件人: ')
    msg_to = input('收件人: ')
    msg_subject = input('subject: ')
    e = Email()
    e.send_email(from_addr,password,to_addr,smtp_server,mimetext,msg_from,msg_to,msg_subject)

