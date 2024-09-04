# Домашнее задание по теме "Режимы открытия файлов"

# module_7_1_old.py
from pprint import pprint

name_file = 'poem.txt'
file = open(name_file, 'w')
file.write('''My soul is dark - Oh! quickly string
The harp I yet can brook to hear;
And let thy gentle fingers fling
Its melting murmurs o'er mine ear.
If in this heart a hope be dear,
That sound shall charm it forth again:
If in these eyes there lurk a tear,
'Twill flow, and cease to burn my brain.
But bid the strain be wild and deep,
Nor let thy notes of joy be first:
I tell thee, minstrel, I must weep,
Or else this heavy heart will burst;
For it hath been by sorrow nursed,
And ached in sleepless silence, long;
And now 'tis doomed to know the worst,
And break at once - or yield to song.''')
file.close()
file = open(name_file, 'r')
print(file.read())
file.close()
