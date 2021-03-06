from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_PSS
import Crypto
import base64
KEY_SIZE = 2048

def gen_keys(path='../../private/keys'):
    key = RSA.generate(KEY_SIZE)
    private_key = key.export_key("PEM")
    file_out = open(f"{path}/private.pem", "wb")
    file_out.write(private_key)
    file_out.close()
    
    public_key = key.publickey().export_key("PEM")
    file_out = open(f"{path}/public.pem", "wb")
    file_out.write(public_key)
    file_out.close()
    print(f"Keys have been written to {path}")

def encrypt(message, path='keys/public.pem'):
    key = RSA.importKey(open(path).read())
    cipher = PKCS1_OAEP.new(key, Crypto.Hash.SHA256, lambda x,y: Crypto.Signature.PKCS1_PSS.MGF1(x,y, Crypto.Hash.SHA1))
    ciphertext = cipher.encrypt(message)
    return ciphertext


def decrypt(ciphertext_base64, path='keys/private.pem'):
    key = open(path).read()
    key = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key=key, hashAlgo=Crypto.Hash.SHA256, mgfunc=lambda x,y: Crypto.Signature.PKCS1_PSS.pss.MGF1(x,y, Crypto.Hash.SHA1))
    ciphertext = base64.b64decode(ciphertext_base64)
    message = cipher.decrypt(ciphertext)
    return message

if __name__ == '__main__':
    gen_keys()