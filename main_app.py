# напиши здесь свое приложение
# импорт необходимого
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import *
# класс для приложения
class FirstWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        h1 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        h2 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        v1 = BoxLayout(orientation = 'vertical')
        txt = Label(text = txt_instruction)
        txt_name = Label(text = 'Введите имя')
        txt_age = Label(text = 'Введите возраст')
        name = TextInput(text = '', multiline = False)
        age = TextInput(text = '', multiline = False)
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        h1.add_widget(txt_name)
        h1.add_widget(name)
        h2.add_widget(txt_age)
        h2.add_widget(age)
        v1.add_widget(txt)
        v1.add_widget(h1)
        v1.add_widget(h2)
        v1.add_widget(self.btn)
        self.add_widget(v1)
    def next(self):
        self.manager.transition.direction = 'left' #направление анимации
        self.manager.current = 'second' # на какое окно мы будем ссылаться
class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        h = BoxLayout(size_hint = (0.8, None), height = '30sp')
        v = BoxLayout(orientation = 'vertical')
        txt = Label(text = txt_test1)
        txt_result = Label(text = 'Введите результат')
        result = TextInput(text = '', multiline = False)
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        h.add_widget(txt_result)
        h.add_widget(result)
        v.add_widget(txt)
        v.add_widget(h)
        v.add_widget(self.btn)
        self.add_widget(v)
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'third'
class ThirdWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v = BoxLayout(orientation = 'vertical')
        txt = Label(text = txt_sits)
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        v.add_widget(txt)
        v.add_widget(self.btn)
        self.add_widget(v)
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'fourth'
class FourthWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        h1 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        h2 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        v1 = BoxLayout(orientation = 'vertical')
        txt = Label(text = txt_test3)
        txt_result = Label(text = 'Результат')
        txt_result_2 = Label(text = 'Результат после отдыха')
        result = TextInput(text = '', multiline = False)
        result2 = TextInput(text = '', multiline = False)
        self.btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        h1.add_widget(txt_result)
        h1.add_widget(result)
        h2.add_widget(txt_result_2)
        h2.add_widget(result2)
        v1.add_widget(txt)
        v1.add_widget(h1)
        v1.add_widget(h2)
        v1.add_widget(self.btn)
        self.add_widget(v1)
    def next():
        self.manager.transition.direction = 'left'
        self.manager.current = 'fifth'
class FifthWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instr = Label(text='Расчет...', halign='center')
        P1 = self.manager.P1
        P2 = self.manager.P2
        P3 = self.manager.P3
        age = self.manager.age
        result_text = test(P1, P2, P3, age)
        self.instr.text = result_text

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.age = 0
        sm.P1 = 0
        sm.P2 = 0
        sm.P3 = 0
        sm.add_widget(FirstWindow(name = 'first'))
        sm.add_widget(SecondWindow(name = 'second'))
        sm.add_widget(ThirdWindow(name = 'third'))
        sm.add_widget(FourthWindow(name = 'fourth'))
        sm.add_widget(FifthWindow(name = 'fifth'))
        return sm
app = MyApp()
app.run()