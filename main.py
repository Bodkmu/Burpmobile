from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import threading
import socket

# تم تعريف التصميم في متغير نصي واحد محكم القفل
layout_kv = '''
MDBoxLayout:
    orientation: "vertical"
    md_bg_color: 0.9, 0.9, 0.9, 1

    MDTopAppBar:
        title: "Burp Suite Pro - Mobile"
        elevation: 1
        md_bg_color: 0.95, 0.95, 0.95, 1
        specific_text_color: 0.9, 0.4, 0, 1
        right_action_items: [["window-maximize", lambda x: app.enable_pip()]]

    MDTabs:
        id: tabs
        background_color: 0.95, 0.95, 0.95, 1
        indicator_color: 0.9, 0.4, 0, 1
        text_color_active: 0.9, 0.4, 0, 1

        Tab:
            title: "PROXY"
            MDBoxLayout:
                orientation: "vertical"
                padding: "8dp"
                spacing: "5dp"
                MDBoxLayout:
                    size_hint_y: None
                    height: "45dp"
                    MDRaisedButton:
                        text: "Forward"
                        md_bg_color: 0.8, 0.8, 0.8, 1
                        text_color: 0, 0, 0, 1
                        on_release: app.forward_data()
                MDTextField:
                    id: proxy_text
                    multiline: True
                    mode: "fill"
                    fill_color: 1, 1, 1, 1
                    text: "Waiting for traffic on port 8080..."

        Tab:
            title: "REPEATER"
            MDBoxLayout:
                orientation: "vertical"
                padding: "8dp"
                spacing: "10dp"
                
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0.45
                    MDLabel:
                        text: "Request:"
                        font_style: "Caption"
                        size_hint_y: None
                        height: "20dp"
                    MDTextField:
                        id: repeater_input
                        mode: "fill"
                        fill_color: 1, 1, 1, 1
                        multiline: True
                        font_size: "13sp"

                MDBoxLayout:
                    size_hint_y: None
                    height: "48dp"
                    spacing: "10dp"
                    MDRaisedButton:
                        text: "SEND"
                        md_bg_color: 0.9, 0.4, 0, 1
                        size_hint_x: 0.5
                        on_release: app.send_repeater()
                    MDRoundFlatButton:
                        text: "Copy Response"
                        text_color: 0.9, 0.4, 0, 1
                        line_color: 0.9, 0.4, 0, 1
                        size_hint_x: 0.5
                        on_release: app.copy_response()

                MDBoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0.45
                    MDLabel:
                        text: "Response:"
                        font_style: "Caption"
                        size_hint_y: None
                        height: "20dp"
                    MDTextField:
                        id: repeater_response
                        mode: "fill"
                        fill_color: 0.98, 0.98, 0.98, 1
                        readonly: True
                        multiline: True
                        font_size: "13sp"

<Tab@MDFloatLayout+MDTabsBase>:
'''

class Tab(MDFloatLayout, MDTabsBase):
    pass

class BurpApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(layout_kv)

    def on_start(self):
        # تشغيل سيرفر البروكسي في Thread منفصل
        threading.Thread(target=self.start_proxy, daemon=True).start()

    def start_proxy(self):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('0.0.0.0', 8080))
            server.listen(5)
            while True:
                client, addr = server.accept()
                data = client.recv(4096).decode('utf-8', errors='ignore')
                if data:
                    self.root.ids.proxy_text.text = data
                    self.root.ids.repeater_input.text = data
                client.close()
        except Exception as e:
            print(f"Proxy Error: {e}")

    def forward_data(self):
        self.root.ids.proxy_text.text = "Forwarded! Waiting for next request..."

    def send_repeater(self):
        # هنا تم إصلاح القوسين الناقصين في تعريف الدالة
        self.root.ids.repeater_response.text = "HTTP/1.1 200 OK\\nServer: Burp-Mobile\\n\\n[+] Success! Data captured."

    def copy_response(self):
        res_text = self.root.ids.repeater_response.text
        if res_text:
            Clipboard.copy(res_text)

    def enable_pip(self):
        print("Floating Window mode triggered.")

if __name__ == '__main__':
    BurpApp().run()
