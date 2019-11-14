import psycopg2
conn = psycopg2.connect(database="Movoto", user="postgres", password="1234", host="127.0.0.1", port="5555")
sourcePath = '/Users/george/Downloads/movoto_estimates.csv'

class AirbnbRow:
    def __init__(self, zip, bed, bath):
        self.zip = zip.strip('"')
        self.bed = bed.strip('"')
        self.bath = bath.strip('"')
        self.entire = 0
        self.private = 0
    
    def save(self):
        sql = ('insert into airbnb_est_value(zip, bed, bath, entire, single)'
        ' values (\'{}\', {}, {}, {}, {})').format(self.zip.rjust(5, '0'), self.bed, self.bath, self.entire, self.private)

        # print (sql)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()


lineNumber = 0
airbnbRow = None;
for line in open(sourcePath):
    lineNumber += 1
    if(lineNumber == 1):
        continue
    print('Processing line number is : {}'.format(lineNumber));
    lnValues = line.split(',');
    if(lineNumber %2 == 0):
        airbnbRow = AirbnbRow(lnValues[0], lnValues[1], lnValues[2])
        airbnbRow.entire = lnValues[4].strip().strip('"')
    else:
        airbnbRow.private = lnValues[4].strip().strip('"')
        airbnbRow.save();
        airbnbRow = None

conn.close()




    