import vobject

s = """
BEGIN:VCARD
VERSION:3.0
EMAIL;TYPE=INTERNET:jeffrey@osafoundation.org
FN:Jeffrey Harris
N:Harris;Jeffrey;;;
TEL;TYPE=WORK,VOICE:(111) 555-1212
TEL;TYPE=HOME,VOICE:(404) 555-1212
END:VCARD
"""
v = vobject.readOne( s )

for tel in v.tel_list:
    print(tel.value)
