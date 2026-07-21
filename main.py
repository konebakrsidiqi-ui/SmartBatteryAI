from kivy.app import App
from kivy.uix.label import Label

class SmartBatteryAI(App):
    def build(self):
        return Label(text="SmartBatteryAI\nVersion 1.0")

SmartBatteryAI().run()
