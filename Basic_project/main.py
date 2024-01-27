from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.image import Image

class ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.top_app_bar.title = "Decimal to Binary"
            self.input.text = "Enter a Decimal Number"
            self.label.text = ""
            self.converted.text = ""
        else:
            self.state = 0
            self.top_app_bar.title = "Binary to Decimal"
            self.input.text = "Enter Binary Number"
            self.label.text = ""
            self.converted.text = ""







    def convert(self, args):
        if self.state == 0:
            val = int(self.input.text,2)
            self.converted.text = str(val)
            self.label.text = "In DECIMAL IS:"
        else:
            val = bin(int(self.input.text))[2:]
            self.converted.text = str(val)
            self.label.text = "In BINARY IS:"




    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "DeepOrange"
        screen = MDScreen()

        # Ensure that the top app bar is positioned at the top
        self.top_app_bar = MDTopAppBar(
            title="Binary to Decimal",
            right_action_items=[["rotate-3d-variant", lambda x: self.flip() ]],
            pos_hint={'top': 1}  # This should make sure the app bar is at the top
        )
        screen.add_widget(self.top_app_bar)

        #Logo
        screen.add_widget(Image(source = "bite.png",size=(100, 100) ,pos_hint = {"center_x":0.5, "center_y":0.7}))

        #textfield
        self.input = MDTextField(
            text = "Enter a Binary Number", halign = "center", size_hint = ( 0.8, 1), pos_hint = {"center_x":0.5, "center_y":0.45}, font_size = 22,
        )
        screen.add_widget(self.input)

        #Primary + Secondary Label
        self.label = MDLabel(
            font_size = 18,
            halign = "center",
            pos_hint = {"center_x":0.5, "center_y":0.35},
            theme_text_color = "Secondary"
        )

        self.converted = MDLabel(
            halign = "center",
            pos_hint = {"center_x":0.5, "center_y":0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)


        #CONVERT BUTTON
        screen.add_widget(MDFillRoundFlatButton(
            text = "CONVERT",
            font_size = 17,
            pos_hint = {"center_x":0.5, "center_y":0.15},
            on_press = self.convert
            ))









        return screen
if __name__ == '__main__':
    ConverterApp().run()
