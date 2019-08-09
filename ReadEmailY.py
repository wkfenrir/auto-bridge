import email ​
import imapclient 
from imapclient import IMAPClient
​
HOST = 'imap.gmail.com'
USERNAME = 'UR EMAIL'
PASSWORD = 'UR PASSWORD'
​
with IMAPClient(HOST) as server:
    server.login(USERNAME, PASSWORD)
    server.select_folder('INBOX', readonly=True)
​
    messages = server.search()
    for uid, message_data in server.fetch(messages, 'RFC822').items():
        email_message = email.message_from_bytes(message_data[b'RFC822'])
        print(uid, email_message.get_payload())