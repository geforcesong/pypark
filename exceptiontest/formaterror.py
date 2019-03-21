class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        print('>> log file', self.line, self.file)

def parser():
    raise FormatError(20, 'spam.txt')

try:
    parser()
except FormatError as exc:
    exc.logerror()