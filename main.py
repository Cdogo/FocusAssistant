file = open(input('enter filename: '))
file = file.readlines()

outFile = open('run.py', 'w')

def makeLine(programName):
    return '\n        if process.name.lower() == \"{}\":\n            process.Terminate()\n'.format(programName.lower())
    
outFile.write('import wmi\nimport time\nf = wmi.WMI()\n')
outFile.write('while True:\n    time.sleep({})\n    for process in f.Win32_Process():'.format(file[0][:-1]))

for line in file[1:]:
    if line[:-1] + '\n' == line:
        outFile.write(makeLine(line[:-1]))
    else:
        outFile.write(makeLine(line))
outFile.close()
    
