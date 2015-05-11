# Import SOAPpy WSDL Package
from SOAPpy import WSDL

# CrSeed WSDL URL
wsdlurl = "https://palena.sii.cl/DTEWS/CrSeed.jws?wsdl"

# Create a service proxy from the wsdl
_server = WSDL.Proxy(wsdlurl)

# Default option values.
query = 'uniprot:wap_rat'
format = 'fasta'
style = 'raw'

result = _server.fetchData(query, format, style)

print result