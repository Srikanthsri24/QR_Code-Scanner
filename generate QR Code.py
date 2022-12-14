from MyQR import myqr
import os

f = open('Students.txt','r')
lines = f.read().split("\n")
print(lines)

for _ in range (0,len(lines)):
    data = lines[_]
    version,level,qr = myqr.run(
        str(data),
        level='H',
        version=1,
        picture="Bg.jpg",
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name = str(lines[_]+'.jpg'),
        save_dir=os.getcwd()
    )
