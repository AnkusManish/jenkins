class test:
    def __init__(self,subject):
        self.subject = 'Maths'


my_test = test('exam')

def final_exams (maths,english):
    maths.subject = 'Hard'
    english.subject = 'Easy'

final_exams(test('maths'), my_test)