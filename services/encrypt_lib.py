# from cryptography.fernet import Fernet
#
# key = b'4Q4ZknSsErJfsnLCoQDVnYqauRWm8-NS59OEAvcYj5g='
#
#
# def encrypt_text(text):
#     fernet = Fernet(key)
#     byt = bytes(text, 'utf-8')
#     enc_message = fernet.encrypt(byt)
#     print(len(enc_message))
#     return enc_message
#
#
# def decrypt_text(enc_message):
#     fernet = Fernet(key)
#     dec_message = fernet.decrypt(enc_message)
#     return dec_message
