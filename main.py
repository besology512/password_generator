from tkinter import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.factory import Factory
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty
import math
from kivy.uix.popup import Popup
#############################
import user_input as u
import random
import operations as O
import passwordlist as P
import modify_and_rate as MR
import clipboard  # must install it using < pip install clipboard >
import time  # delete it later


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    value1 = StringProperty("")
    value2 = StringProperty("")
    value3 = StringProperty("")
    value4 = StringProperty("")
    value5 = StringProperty("")
    value6 = StringProperty("")
    value7 = StringProperty("")

    def rate(self):
        u.input_password = self.ids.writePass.text
        if len(u.input_password) == 0:
            badinput2().open()
        else:
            output = MR.password_suggestion(u.input_password)
            self.value1 = str(output[0])
            self.value2 = str(output[1])
            self.value3 = str(output[2][0])
            self.value4 = str(output[2][1])
            self.value5 = str(output[2][2])
            self.value6 = str(output[2][3])
            self.value7 = str(output[2][4])


class WindowManager(ScreenManager):
    pass


class MainBox(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class MainGrid(GridLayout):  # work here
    def multiple_passwords(self, checkBox):
        u.multiple_passwords = checkBox.active


class badinput(Popup):
    pass


class badinput2(Popup):
    pass


class badinput3(Popup):
    pass


class CharNumGrid(GridLayout):
    my_value = StringProperty("15")

    def on_slider_value(self, slider):
        self.my_value = str(math.floor(slider.value))
        u.Plength = math.floor(slider.value)
        return u.Plength


class CreateButtonBox(BoxLayout):
    num_password = u.n_passwords
    final_password = StringProperty("Password")
    leng = u.Plength
    multiple_passwords = u.multiple_passwords

    def user_choice(self):
        if u.upper == True:
            O.upper_case()
        if u.lower == True:
            O.lower_case()
        if u.Numbers == True:
            O.numbers()
        if u.exclude_ambsymbols == True and u.symbols == True:
            O.not_ambsymbols()
        if u.exclude_ambsymbols == False and u.symbols == True:
            O.all_symbols()

    def get_password(self, length, n_passwords):
        # This function take the length of the password and the number of generated password as an input and give a randomized password as a output
        start_time = time.time()
        if u.Numbers == False and u.lower == False and u.upper == False and u.symbols == False and u.wspace == False:
            badinput().open()
            return StringProperty(self.final_password)
        elif u.Numbers == False and u.lower == False and u.upper == False and u.symbols == False and u.wspace == True:
            badinput3().open()
        else:
            if n_passwords == 1:
                if len(P.password) != 0:
                    P.password = []
                    P.pass_options = []
                self.user_choice()
                for i in range(int(length)):
                    x = random.randrange(0, len(P.pass_options))
                    P.password.append(P.pass_options[x])
                MR.check_pass()
                self.final_password = ''.join(P.password)
                return StringProperty(self.final_password)
            else:
                f = open("passwords.txt", "a")
                for i in range(0, n_passwords):
                    if len(P.password) != 0:
                        P.password = []
                        P.pass_options = []
                    self.user_choice()
                    for i in range(int(length)):
                        x = random.randrange(0, len(P.pass_options))
                        P.password.append(P.pass_options[x])
                    MR.check_pass()
                    generated_password = ''.join(P.password)
                    f.write(f"{generated_password} \n")
                f.close()
        end_time = time.time()
        print(end_time-start_time)

    def call_get_password(self):
        if u.multiple_passwords == True:
            multiple_passwords().open()
        else:
            self.get_password(u.Plength, self.num_password)

    def Copy(self):
        clipboard.copy(self.final_password)


class multiple_passwords(Popup):
    my_value = StringProperty("2")

    def on_slider_value(self, slider):
        self.my_value = str(math.floor(slider.value))
        u.n_passwords = math.floor(slider.value)
        return u.n_passwords

    def save(self):
        Factory.CreateButtonBox().get_password(u.n_passwords, u.Plength)

    def close(self):
        self.dismiss()


class Upper(GridLayout):
    def work_button(self, checkbox):
        u.upper = checkbox.active


class Lower(GridLayout):
    def work_button(self, checkbox):
        u.lower = checkbox.active


class Digits(GridLayout):
    def work_button(self, checkbox):
        u.Numbers = checkbox.active


class Symbols(GridLayout):
    def work_button(self, checkbox):
        u.symbols = checkbox.active


class Ambigous(GridLayout):
    def work_button(self, checkbox):
        u.exclude_ambsymbols = checkbox.active


class Space(GridLayout):
    def work_button(self, checkbox):
        u.wspace = checkbox.active


class PassField(TextInput):
    pass


class RateButton(Button):
    pass


class PasswordGeneratorApp(App):
    def build(self):
        self.load_kv("styling.kv")


if __name__ == "__main__":
    PasswordGeneratorApp().run()
