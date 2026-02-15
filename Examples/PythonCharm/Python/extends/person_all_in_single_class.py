class Person:


    def SayHello(self):
        print(f'{self.Name} says Hello!')


class Worker(Person):
    def __init__(self):
        Person.__init__(self)
        self.Title = ''
        self.Salary = 0

    def SayHello(self):
        if self.Title == 'Manager':
            print(f'{self.Title} {self.Name} says Hello!')
        else:
            Person.SayHello(self)

    def Work(self):
        print(f'Work work work...')


worker = Worker()
worker.Title = 'Manager'
worker.Name = 'Bob'

worker.SayHello()
worker.Work()

