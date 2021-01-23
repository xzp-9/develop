class Animals:
    name='name'
    color='black'
    age=11
    gender='man'
    def __init__(self,name,color,age,gender,hair):
        self.name=name
        self.age=age
        self.gender=gender
        self.color=color
        self.hair=hair
    def Calling(self):
        print('hahahhh')
    def run(self):
        print('running')
class Cat(Animals):
    def CatchaMouse(self):
        print('the {} can  catcha mouse'.format(Cat.name))
    def Calling(self):
        print('wuowuowuowueowuwoeo')




if __name__ == '__main__':
    t = Animals('ouyangpeng','black',28,'man','long')
    print(t.color)
    print(t.Calling())
    print(t.run())
    t1=Cat('ouyangpeng','black',28,'man','long')
    print(t1.CatchaMouse())
    print(t1.Calling())