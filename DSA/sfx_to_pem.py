# from OpenSSL import crypto

# pfx_path = r'D:\RBL SSL\6244444837847db164d6c25c098ab6d7.pfx'
# pem_path = r'D:\RBL SSL\cert_and_key.pem'
# pfx_password = 'sR%!vuoj2(Mvy4Rd6#ch]vtek'  # Replace with your actual .pfx password

# # Load .pfx file
# with open(pfx_path, 'rb') as pfx_file:
#     pfx_data = pfx_file.read()

# # Convert .pfx to .pem
# p12 = crypto.load_pkcs12(pfx_data, pfx_password)

# # Extract private key and certificate
# private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())
# certificate = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())

# # Write to .pem file
# with open(pem_path, 'wb') as pem_file:
#     pem_file.write(private_key)
#     pem_file.write(certificate)

# print(f"Converted .pfx to .pem and saved at {pem_path}", 'ddddddddddddddddddddddddddddddddddddddddddddd')



# ----------------------------- 


from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.hazmat.primitives.serialization import pkcs12, BestAvailableEncryption
import os

pfx_path = r'D:\RBL SSL\6244444837847db164d6c25c098ab6d7.pfx'
pem_path = r'D:\RBL SSL\cert_and_key.pem'
pfx_password = b'sR%!vuoj2(Mvy4Rd6#ch]vtek'  # Replace with your actual .pfx password

# Load .pfx file
with open(pfx_path, 'rb') as pfx_file:
    pfx_data = pfx_file.read()

# Convert .pfx to .pem
private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(pfx_data, pfx_password)

# Write private key and certificate to .pem file
with open(pem_path, 'wb') as pem_file:
    pem_file.write(private_key.private_bytes(
        encoding=Encoding.PEM,
        format=PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=NoEncryption()
    ))
    pem_file.write(certificate.public_bytes(Encoding.PEM))
    for cert in additional_certificates:
        pem_file.write(cert.public_bytes(Encoding.PEM))

print(f"Converted .pfx to .pem and saved at {pem_path}")



