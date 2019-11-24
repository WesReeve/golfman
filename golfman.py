""" golfman.py """

from getpass import *
c,g,w = 0,[],getpass('word:')
while c<5:
    l=input('Guess: ')
    f=l in w
    g = (g,g+[l])[f]
    c += (1,0)[f]
    s=' '.join([('_',x)[l==x or x in g] for x in w])
    y='_' not in s
    print( '\n'*30+f"""{('Incorrect','Correct!')[l in w]}
 |--|
{('    |',' O  |')[c>=1]}
{(' ','-')[c>=3]}{(' ','|')[c>=2]}{('  |','- |')[c>=4]}
{('  ',' ^')[c>=5]}  |\n    |
\n\n{s}""" )
    if y:
        break
print( ('Loser!','Winner!')[y] )