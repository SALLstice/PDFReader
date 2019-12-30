import subprocess

pythonPath = r"C:Python38\python.exe"
minerPath = r'C:Python38\scripts\pdf2txt.py'
outputPath = r'C:\Users\sallma\Documents\invoice.txt'
inputFile =  r'C:\Users\sallma\Documents\invoice.pdf'
buildString = f"{pythonPath} {minerPath} -S {inputFile}"

output = subprocess.check_output(buildString, shell=True)
outStr = str(output)
outList = outStr.split('\\n')

filterOutList = [o for o in outList if o != "\\r"]
filterOutList = [k[:-2] for k in filterOutList]
filterOutList = [j for j in filterOutList if j != ""]

invIdx = outStr.find("INVOICE")
invNum = outStr[invIdx+16:invIdx+22]