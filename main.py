from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window


Window.size=(360,640)
class Container(GridLayout):
    numbers = []
    operator = ''
    dotcount = False

    def eqNamber(self):
        try:
            number = float(self.ioLable.text)
        except Exception:
            number = 0.0
        self.numbers.append(number)
        self.ioLable.text = ''
        i = 0
        while i < len(self.numbers):
            if ((i-1) >= 0):
                number = self.numbers[i]
                prev_number = self.numbers[i-1]
                try:
                    if self.operator == '+':
                        res = number + prev_number
                    elif self.operator == '-':
                        res = prev_number - number
                    elif self.operator == '*':
                        res = prev_number * number
                    elif self.operator == '/':
                        res = prev_number / number
                    self.ioLable.text = str(res)
                    self.numbers[i] = res
                    self.numbers.pop(i-1)
                except Exception:
                    self.ioLable.text='На ноль делить нельзя'
            i +=1
        self.dotcount = False
    #clear labale
    def clearLabel(self):
        self.ioLable.text = ''
        self.numbers = [0.0, 0.0]
        self.dotcount = False
    #print numbers in labale
    def printNumber(self, btn_id):
        self.ioLable.text += btn_id.text
    def printDot(self):
        if (self.dotcount != True):
            if self.btn_dot.state == 'normal':
                self.dotcount = True 
            self.ioLable.text += self.btn_dot.text
    
    # function add thwo numbers
    def sumNumber(self):
        self.operator = '+'
        try:
            number = float(self.ioLable.text)
        except Exception:
            number = 0.0
        self.numbers.append(number)
        self.ioLable.text = ''
        self.dotcount = False
    # function sub thwo numbers
    def subNumber(self):
        self.operator = '-'
        try:
            number = float(self.ioLable.text)
        except Exception:
            number = 0.0
        self.numbers.append(number)
        self.ioLable.text = ''
        self.dotcount = False
    # function mull thwo numbers
    def mullNumber(self):
        self.operator = '*'
        try:
            number = float(self.ioLable.text)
        except Exception:
            number = 0.0
        self.numbers.append(number)
        self.ioLable.text = ''
        self.dotcount = False

    # function div thwo numbers
    def divNumber(self):
        self.operator = '/'
        try:
            number = float(self.ioLable.text)
        except Exception:
            number = 0.0
        self.numbers.append(number)
        self.ioLable.text = ''
        self.dotcount = False

class CalcApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    CalcApp().run()
