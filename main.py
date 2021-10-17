from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.core.window import Window
import Encrypt

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label


class MyApp(App):
    count = False
    string = ''

    def press_encrypt(self, instance):
        print("Зашифровано")
        self.message.text = "Зашифровано сообщение >>> \n "
        self.string = Encrypt.encrypt(self.user_text.text, self.user_key.text)
        self.count = True
        self.message.text += self.string
        self.key.text = "Ключ шифрования >>> \n "
        self.key.text += self.user_key.text

    def press_decrypt(self, instance):
        print("Расшифровано")
        self.message.text = "Расшифрованое сообщение >>> \n "
        if not self.count:
            self.string = self.user_text.text
        self.message.text += Encrypt.decrypt(self.string, self.user_key.text)
        self.key.text = "Ключ шифрования >>>\n "
        self.key.text += self.user_key.text
        self.count = False

    def press_close(self, instance):
        #App.get_running_app().stop()
        Window.close()

    def build(self):
        a = AnchorLayout()
        b = BoxLayout(orientation='vertical', spacing=10, size_hint=[.85, .9])
        self.u_in = Label(text="Введите сообщение", halign="left", valign="middle", font_size='20sp',
                          size_hint=(.5, .25))
        self.u_in.bind(size=self.u_in.setter('text_size'))
        b.add_widget(self.u_in)
        self.user_text = TextInput(multiline=False, size_hint=(1, .3), font_size='20sp')
        b.add_widget(self.user_text)
        self.us_in = Label(text="Введите ключ", halign="left", valign="middle", font_size='20sp', size_hint=(.5, .25))
        self.us_in.bind(size=self.us_in.setter('text_size'))
        b.add_widget(self.us_in)
        self.user_key = TextInput(multiline=False, size_hint=(1, .3), font_size='20sp')
        b.add_widget(self.user_key)
        b_button = BoxLayout(spacing=10, size_hint=[1, .25])
        b_button.add_widget(Button(text="Encrypt",
                                   font_size=20,
                                   on_press=self.press_encrypt,
                                   size_hint=[.5, 1],
                                   background_color=[1, 0, 0, 1],
                                   background_normal=""
                                   ))
        b_button.add_widget(Button(text="Decrypt",
                                   font_size=20,
                                   size_hint=[.5, 1],
                                   on_press=self.press_decrypt,
                                   background_color=[1, 0, 25, 1],
                                   background_normal=""
                                   ))
        b.add_widget(b_button)
        self.message = Label(text="", halign="left", valign="top", font_size='20sp', size_hint=(.5, .5) , text_language = 'en')
        self.message.bind(size=self.message.setter('text_size'))
        b.add_widget(self.message)
        self.key = Label(text="", halign="left", valign="top", font_size='20sp', size_hint=(.5, .5))
        self.key.bind(size=self.key.setter('text_size'))
        b.add_widget(self.key)
        a1 = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=[1, .3])
        btn = Button(text="Close",
                     font_size=20,
                     size_hint=[.8, 1],
                     background_color=[1, 0, 25, 1],
                     background_normal="",
                     padding=[20, 20]
                     )
        btn.bind(on_press=self.press_close)
        a1.add_widget(btn)
        b.add_widget(a1)
        a.add_widget(b)

        return a


if __name__ == "__main__":
    MyApp().run()
