import tkinter

# window = tkinter.Tk()
# window.title('Miles (mi) to Kilometers (km) Converter')
# window.minsize(width=500, height=300)
# window.maxsize(width=1000, height=600)
# my_label = tkinter.Label(text='Test', font = ('Helvetica', 24, 'normal'))
# my_label.pack(side='left')





# window.mainloop()

def add(n, **kwargs):
    for k, a in kwargs.items():
        n += a
    print(n)
    print(kwargs)

add(0, first=1, second=2, third=3, fourth=4, fifth=5)

class Car():

    def __init__(self, **kw):
        self.make = kw['make']
        self.mdoel = kw.get('model')
    
my_car = Car(make='test')