import imaplib
import email
from email.header import decode_header, make_header

socket = imaplib.IMAP4_SSL("imap.gmail.com", port=993)

socket.login("dr.truefood@gmail.com", "zndWkr9630@")

socket.select('INBOX')

socket.literal = u"주문내역".encode('utf-8')

resp, lst = socket.uid('search', 'CHARSET', 'UTF-8', 'ALL', 'SUBJECT') # 미확인 메일 : "ALL" -> "UNSEEN"

for i in lst[0].split():
    result, data = socket.uid('fetch', i, '(RFC822)')
    raw_email = data[0][1]

    print("-"*80)
    message = email.message_from_bytes(raw_email)
    date = make_header(decode_header(message.get('Date')))
    print(date)
    frm = make_header(decode_header(message.get('From')))
    print(frm)
    subject = make_header(decode_header(message.get('Subject')))
    print(subject)

socket.close()
socket.logout()