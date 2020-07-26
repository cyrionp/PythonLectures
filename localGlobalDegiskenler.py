name='Çınar'
def changeName(new_name):
    name=new_name
    print(name)

changeName('Ada')
print(name)

def karsilama():
    name='Çınar'
    def hello():
        print('hello '+name)

    hello()

karsilama()
