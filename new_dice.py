'''
    new_dice.py

    new dice functions / classes
'''
import random

class Die(object):
    faces = (None,'   \n| * |\n   \none','   *\n|   |\n *  \ntwo','  *\n| * |\n  *\nthree','* *\n|   |\n * *\nfour','* *\n| * |\n * *\nfive','***\n|   |\n ***\nsix')

    def __init__(self, faces=None):
        if faces is not None:
            self.faces = faces
        self.value = 1

    def print_faces(self):
        count = 1
        tmp = [][:]
        for itm in self.faces:
            tmp.append('face {}'.format(count) + '\n' + itm)
            count += 1
        print ' '.join(map(str,tmp))

    def __str__(self):
        return self.faces[self.value]

    def roll(self):
        self.value = random.randrange(1,len(self.faces))




def test():
    myRoll = (Die(),Die(),Die(),Die(),Die(),Die())
    dieFormat = '''{} {} {} 
    {} {} {}
    '''
    
    for d in range(len(myRoll)):
        myRoll[d].roll()
    #print ' '.join(map(str,myRoll))
    print dieFormat.format(*myRoll)    
    #d = Die()
    #d.print_faces()
    #print d
    #d.roll()
    #print d


if __name__ == "__main__":
    test()
