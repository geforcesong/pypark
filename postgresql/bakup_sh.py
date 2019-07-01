import gzip
from sh import pg_dump
with gzip.open('./postgresql/baks/backup.gz', 'wb') as f:
  pg_dump('-h', 'localhost', '-U', 'george', 'Student', _out=f)
