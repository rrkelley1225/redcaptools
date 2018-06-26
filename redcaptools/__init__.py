import pycurl, io
from urllib.parse import urlencode
import json
import pandas as pd

def getReport(reportID):
    buf = io.BytesIO()
    data = {
    'token': 'DF0536E309676D419C6E49BAE0CCA7FD',
    'content': 'report',
    'format': 'json',
    'report_id': reportID,
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'returnFormat': 'json'
    }
    ch = pycurl.Curl()
    ch.setopt(ch.URL, 'https://id.research.louisville.edu/redcap/api/')
    ch.setopt(ch.POSTFIELDS, urlencode(data))
    ch.setopt(ch.WRITEFUNCTION, buf.write)
    ch.perform()
    ch.close()
    d = json.loads(buf.getvalue().decode())
    buf.close()
    
    return pd.DataFrame(d)