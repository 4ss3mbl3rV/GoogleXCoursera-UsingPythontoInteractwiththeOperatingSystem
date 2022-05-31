import os, sys, datetime

if os.path.isfile('novel.txt'):
    print(str(os.path.getsize('novel.txt')) + ' bytes')

    timestamp = os.path.getmtime('novel.txt')
    convertTime = datetime.datetime.fromtimestamp(timestamp)
    print('timestamp: {}'.format(timestamp))
    print('time: {}'.format(convertTime))
    absPath = os.path.abspath('novel.txt')
    print('-'*10, 'absolute path', '-'*10)
    print(absPath)
else:
    sys.exit('File not Found')
