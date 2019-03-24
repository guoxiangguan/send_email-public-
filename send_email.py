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
    def send_email(self,from_addr='51170601007@stu.ecnu.edu.cn',password='Guan123456',to_addr='1587753354@qq.com',smtp_server='smtp.exmail.qq.com',mimetext=None,msg_from='Guanxiang Guan',msg_to='Guanxiang Guan',msg_subject=None):
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

