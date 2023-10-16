from pybo.models import Structure
from pybo import db

# with open(r"structuredata-1.dat") as datFile:
#     print([data.split(',')[0] for data in datFile])

with open(r"structuredata-1.dat") as datFile:
    next(datFile)
    for data in datFile:
        s = Structure(date=data.split(',')[0],\
                      batt=float(data.split(',')[1]),\
                      temp=float(data.split(',')[2]),\
                      ch1_a=float(data.split(',')[3]),\
                      ch1_b=float(data.split(',')[4]),\
                      ch1_c=float(data.split(',')[5]),\
                      ch1_d=float(data.split(',')[6]),\
                      ch2_a=float(data.split(',')[7]),\
                      ch2_b=float(data.split(',')[8]),\
                      ch2_c=float(data.split(',')[9]),\
                      ch2_d=float(data.split(',')[10]),\
                      ch3_a=float(data.split(',')[11]),\
                      ch3_b=float(data.split(',')[12]),\
                      ch3_c=float(data.split(',')[13]),\
                      ch3_d=float(data.split(',')[14]),\
                      ch4_a=float(data.split(',')[15]),\
                      ch4_b=float(data.split(',')[16]),\
                      ch4_c=float(data.split(',')[17]),\
                      ch4_d=float(data.split(',')[18]), \
                      ch5_a=float(data.split(',')[19]), \
                      ch5_b=float(data.split(',')[20]), \
                      ch5_c=float(data.split(',')[21]), \
                      ch5_d=float(data.split(',')[22]), \
                      ch6_a=float(data.split(',')[23]), \
                      ch6_b=float(data.split(',')[24]), \
                      ch6_c=float(data.split(',')[25]), \
                      ch6_d=float(data.split(',')[26]), \
                      ch7_a=float(data.split(',')[27]), \
                      ch7_b=float(data.split(',')[28]), \
                      ch7_c=float(data.split(',')[29]), \
                      ch7_d=float(data.split(',')[30]), \
                      ch8_a=float(data.split(',')[31]), \
                      ch8_b=float(data.split(',')[32]), \
                      ch8_c=float(data.split(',')[33]), \
                      ch8_d=float(data.split(',')[34]), \
                      ch9_a=float(data.split(',')[35]), \
                      ch9_b=float(data.split(',')[36]), \
                      ch9_c=float(data.split(',')[37]), \
                      ch9_d=float(data.split(',')[38]), \
                      ch10_a=float(data.split(',')[39]), \
                      ch10_b=float(data.split(',')[40]), \
                      ch10_c=float(data.split(',')[41]), \
                      ch10_d=float(data.split(',')[42]), \
                      ch11_a=float(data.split(',')[43]), \
                      ch11_b=float(data.split(',')[44]), \
                      ch11_c=float(data.split(',')[45]), \
                      ch11_d=float(data.split(',')[46]), \
                      ch12_a=float(data.split(',')[47]), \
                      ch12_b=float(data.split(',')[48]), \
                      ch12_c=float(data.split(',')[49]), \
                      ch12_d=float(data.split(',')[50]), \
                      ch13_a=float(data.split(',')[51]), \
                      ch13_b=float(data.split(',')[52]), \
                      ch13_c=float(data.split(',')[53]), \
                      ch13_d=float(data.split(',')[54]), \
                      ch14_a=float(data.split(',')[55]), \
                      ch14_b=float(data.split(',')[56]), \
                      ch14_c=float(data.split(',')[57]), \
                      ch14_d=float(data.split(',')[58]), \
                      ch15_a=float(data.split(',')[59]), \
                      ch15_b=float(data.split(',')[60]), \
                      ch15_c=float(data.split(',')[61]), \
                      ch15_d=float(data.split(',')[62]), \
                      ch16_a=float(data.split(',')[63]), \
                      ch16_b=float(data.split(',')[64]), \
                      ch16_c=float(data.split(',')[65]), \
                      ch16_d=float(data.split(',')[66]))

from pybo.models import Structur_tiltmeter
from pybo import db

with open(r"structure_tiltmeter-1.dat") as datFile:
    next(datFile)
    for data in datFile:
        s = Structur_tiltmeter(opdatetime=data.split(',')[0],\
                            tilt_01_x=float(data.split(',')[1]), \
                            tilt_01_y = float(data.split(',')[2]), \
                            tilt_02_x = float(data.split(',')[3]), \
                            tilt_02_y = float(data.split(',')[4]), \
                            tilt_03_x = float(data.split(',')[5]), \
                            tilt_03_y = float(data.split(',')[6]), \
                            tilt_04_x = float(data.split(',')[7]), \
                            tilt_04_y = float(data.split(',')[8]), \
                            tilt_05_x = float(data.split(',')[9]), \
                            tilt_05_y = float(data.split(',')[10]), \
                            tilt_06_x = float(data.split(',')[11]), \
                            tilt_06_y = float(data.split(',')[12]), \
                            tilt_07_x = float(data.split(',')[13]), \
                            tilt_07_y = float(data.split(',')[14]))
        db.session.add(s)
        db.session.commit()