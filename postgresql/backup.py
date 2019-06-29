import subprocess
command = 'pg_dump -h {0} -d {1} -U {2} -f ./postgresql/baks/table3.dmp'.format(
    'localhost', 'Student', 'george')
popen = subprocess.Popen(
    command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)

popen.wait()
