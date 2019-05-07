"""
crypto.py 
Take a plaintext message and encrypt it using a Caesar cipher(d->a)
JIa.Q, May 2019
"""
#import section
import string

#static variables
CHAR_SET = string.printable[:-5]
#string.printable:'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#\\ -> \; \t -> tab; \n; \r
SUBSTITUTION_CHARS = CHAR_SET[-3:] + CHAR_SET[:-3]#move to left for 3 units
TEST_MESSAGE = 'I like Monty Python. They are very funny.'

encrypt_dict = {}
decrypt_dict = {}
for i, k in enumerate(CHAR_SET):
    c = SUBSTITUTION_CHARS[i]
    encrypt_dict[k] = c
    decrypt_dict[c] = k

#function section
def encrypt_msg(plaintext, en_dict):
    """
    Take a plaintext message and encrypt it using a Caesar cipher(d->a)
    """
    cipher_ans = []
    for k in plaintext:
        c = en_dict[k]
        cipher_ans.append(c)
    return ''.join(cipher_ans)

def decrypt_msg(ciphertext, de_dict):
    plain_ans = []
    for k in ciphertext:
        c = de_dict[k]
        plain_ans.append(c)
    return ''.join(plain_ans)

#test section
if __name__ == '__main__':
    ENCRYPT = False  #True
    input_file_path = './crypt_input.txt'
    output_file_path = './crypt_output.txt'
    if ENCRYPT: #encrypt
        with open(input_file_path, 'r') as r_f:
            plaintext = r_f.read()
        ciphertext = encrypt_msg(plaintext, encrypt_dict)
        with open(output_file_path, 'w') as w_f:
            w_f.write(ciphertext)
    else: #decrypt
        with open(output_file_path, 'r') as r_f:
            ciphertext = r_f.read()
        plaintext = decrypt_msg(ciphertext, decrypt_dict)
        with open(input_file_path, 'w') as w_f:
            w_f.write(plaintext)