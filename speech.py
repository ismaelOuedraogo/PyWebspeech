#!/usr/bin/python
import subprocess
import cgi,cgitb 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

message= (form.getvalue("message"))


subprocess.call(["pico2wave","-l=fr-FR","-w=fichier.wav","%s"% message])
subprocess.call(["aplay","fichier.wav"])

print message



html = """<!DOCTYPE html>
<head>
    <title>Webservice</title>
</head>
<body>
    
</body>
</html>
"""

print(html)
