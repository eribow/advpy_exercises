class Birds:
    def __init__(self):
        '''Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']

    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)

class Mammals:
    def __init__(self):
        '''Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild cat']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)

