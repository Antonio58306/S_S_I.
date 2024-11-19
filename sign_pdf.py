from app.models.signer import Signer
from app.utils.cli import import_file,export_file,import_cert,import_key
    
key = import_key('app/static/john-key.pem')
cert = import_cert('app/static/john-cert.pem')
signer = Signer(name="John Doe", email="johndoe@mail.com", private_key=key,cert_pem=cert)
file = import_file('app/static/pdf.pdf')
signed = file.sign(signer=signer, reason="reason",location= "location")
export_file(signed, f'{signed.name}')