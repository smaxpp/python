class Student(object):
    def __init__(self, name, score, age):
        self.name=name
        self.score=score
        self.__age=age

    def getAge(self):
        return self.__age

def main():
    print('start')
    bart = Student('Bart', 34,12)
    print (bart.name)
    print (bart.score)
    print (bart.getAge())
    print (type(bart))

if(__name__ == '__main__'):
    main()