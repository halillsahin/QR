import kivy
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang.builder import Builder
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.camera import Camera
from kivy.uix.popup import Popup
from kivy.core.clipboard import Clipboard
import webbrowser
from kivy.uix.scrollview import ScrollView
import qrcode
from random import randint
from PIL import Image as PILImage
from kivy.uix.image import Image 
from kivy.factory import Factory
import cv2
from pyzbar.pyzbar import decode
import os, sys
from kivy.resources import resource_add_path, resource_find
from kivy_deps import sdl2, glew

Builder.load_string(
"""


<QROLUŞTUR>
  BoxLayout:
    orientation:"vertical"
    cols:2
    rows:4
    FloatLayout:
      Label:
        font_size:24
        text:"QR Arkaplan rengi seçiniz: "
        size:100,100
        color:0,0,0,1
        pos:-220,300           
      Label:
        font_size:28
        text:"QR kod rengi seçiniz: "
        size:100,100
        color:0,0,0,1
        pos:-228,200                                                                                                                                                                    
      Label:
        font_size:24
        text:"QR kodunuza resim ekleyin: "
        size:100,100
        color:0,0,0,1
        pos:-202,100
                              
      Spinner:
        size_hint_y:0.1
        size_hint_x:0.1 
        pos_hint:{"x":0.48,"y":0.85}
        text: 'Renkler'
        values: "kırmızı","mavi","yeşil","turuncu","mor","beyaz","pembe","siyah","sarı"
        id:arkaplan_spinner
                                        
     
      Spinner:
        size_hint_y:0.1
        size_hint_x:0.1 
        pos_hint:{"x":0.48,"y":0.71}
        text: 'Renkler'
        values: "kırmızı","mavi","yeşil","turuncu","mor","beyaz","pembe","siyah","sarı"                                         
        id:qr_spinner 
      Button:
        text:"Dosyalar"
        size_hint_y:0.1
        size_hint_x:0.1
        pos_hint:{"x":0.48,"y":0.58} 
        on_press:root.dosya_popup().open()
      Label:
        text:"Bir metin giriniz: "
        font_size:24
        size:100,100
        color:0,0,0,1
        pos:-262,-20     

      TextInput:
        font_size:20
        id:qr_metni
        size_hint_x:0.45
        size_hint_y:0.05
        pos:330,335
        multiline:False
      Button:
        text:"Dönüştür"
        size_hint_y:0.065
        size_hint_x:0.1
        pos_hint:{"x":0.78,"y":0.44}
        on_press:root.QRFiltre()
      
      Button:
        text:"QR OLUŞTUR"
        size_hint_y:0.15
        size_hint_x:0.34
        pos_hint:{"x":0,"y":0}
        on_press: root.manager.current = 'QROLUŞTUR'
      Button:
        text:"QR OKUT"
        size_hint_y:0.15
        size_hint_x:0.33
        pos_hint:{"x":0.34,"y":0}
        on_press: root.manager.current = 'QROKUT'
      Button:
        text:"İLETİŞİM"
        size_hint_y:0.15
        size_hint_x:0.33
        pos_hint:{"x":0.67,"y":0}
        on_press: root.manager.current = 'İLETİŞİM'




<QROKUT>
  BoxLayout:
    orientation:"vertical"
    FloatLayout:
      
      Button:
        text:"QR OLUŞTUR"
        size_hint_y:0.15
        size_hint_x:0.34
        pos_hint:{"x":0,"y":0}
        on_press: root.manager.current = 'QROLUŞTUR'
      Button:
        text:"QR OKUT"
        size_hint_y:0.15
        size_hint_x:0.33
        pos_hint:{"x":0.34,"y":0}
        on_press: root.manager.current = 'QROKUT'
      Button:
        text:"İLETİŞİM"
        size_hint_y:0.15
        size_hint_x:0.33
        pos_hint:{"x":0.67,"y":0}
        on_press: root.manager.current = 'İLETİŞİM'
      Camera:
        id: camera
        resolution: (640, 480)
        play: True
        pos:0,100
        size:100,100
      Label:
        id: qr_result
        text: ""
        font_size: 20
        pos_hint: {"x": 0, "y": 0.22}
        size_hint_y: None
        height: 44  


<İLETİŞİM>
  ScrollView:
    do_scroll_x: False
    do_scroll_y: True
  
    mail:mail
    BoxLayout:
      FloatLayout: 
        Button:
          text:"QR OLUŞTUR"
          size_hint_y:0.15
          size_hint_x:0.34
          pos_hint:{"x":0,"y":0}
          on_press: root.manager.current = 'QROLUŞTUR'
        Button:
          text:"QR OKUT"
          size_hint_y:0.15
          size_hint_x:0.33
          pos_hint:{"x":0.34,"y":0}
          on_press: root.manager.current = 'QROKUT'
        Button:
          text:"İLETİŞİM"
          size_hint_y:0.15
          size_hint_x:0.33
          pos_hint:{"x":0.67,"y":0}
          on_press: root.manager.current = 'İLETİŞİM'
        Label:
          text:"Merhaba! Uygulamam reklamsız ve tamamen ücretsizdir."

          font_size:20
          bold:True
          color:0,0,0,1
          pos:0,350
        Label:
          text:"Sizlere daha kaliteli hizmet sunabilmem için bağış yapabilirsiniz."  
          font_size:20
          color:0,0,0,1
          bold:True
          pos:0,325
        Label:
          text:"Soru,öneri ve görüşleriniz için iletişime geçmekten lütfen çekinmeyin!"
          size_hint_x:0.91
          size_hint_y:0.1
          bold:True
          color:0,0,0,1
          pos_hint:{"x":0.04,"y":0.25}
          font_size:30  
        GridLayout:
          cols:4
          rows:1
          size_hint_x:0.91
          size_hint_y:0.07
          pos_hint:{"x":0.05,"y":0.17}
          Image:
            size_hint_x:0.1
            size_hint_y:0.1
            pos_hint:{"x":0.12,"y":0.23}
            source: r"C:/Users/halil/OneDrive/Masaüstü/qruygulaması/etsylogo.png"
            id:etsy
            on_touch_down: if self.collide_point(*args[1].pos): root.open_etsy()
          Image:
            size_hint_x:0.1
            size_hint_y:0.1
            pos_hint:{"x":0.45,"y":0.23}
            source:r"C:/Users/halil/OneDrive/Masaüstü/qruygulaması/logoyoutube.png"
            id:youtube
            on_touch_down: if self.collide_point(*args[1].pos): root.open_youtube()
          Image:
            size_hint_x:0.1
            size_hint_y:0.1
            pos_hint:{"x":0.8,"y":0.23}
            source: r"C:/Users/halil/OneDrive/Masaüstü/qruygulaması/downloader.png"
            id:downloader
            on_touch_down: if self.collide_point(*args[1].pos): root.open_downloader()
          Image:
            size_hint_x:0.1
            size_hint_y:0.1
            pos_hint:{"x":0.8,"y":0.23}
            source: r"C:/Users/halil/OneDrive/Masaüstü/qruygulaması/mail.png" 
            id:mail
            on_touch_down: if self.collide_point(*args[1].pos): root.copy_text("startnowdoing@gmail.com")

        GridLayout:
          cols:3
          rows:3
          size_hint_x:0.91
          size_hint_y:0.24
          pos_hint:{"x":0.05,"y":0.65}
          Image:
            size_hint_x:0.8
            size_hint_y:0.8
            pos_hint:{"x":0.8,"y":0.83}
            source:r"C:/Users/halil/OneDrive/Masaüstü/qruygulaması/garanti.png"

          Image:
            size_hint_x:0.8
            size_hint_y:0.8
            pos_hint:{"x":0.45,"y":0.83}
            source:r"C:/Users/halil/OneDrive/Masaüstü/qruygulaması/yapıkredi.jpg"

          Image:
            size_hint_x:0.8
            size_hint_y:0.8
            pos_hint:{"x":0.12,"y":0.83}
            source:r"C:/Users/halil/OneDrive/Masaüstü/qruygulaması/ziraat.png"  
          Label:
            text:"Garanti Bankası"
            color:0,1,0,1
            bold:True
            font_size:24
          Label:
            text:"Yapı Kredi"
            bold:True
            font_size:24
            color:0,0,1,1
          Label:
            text:"Ziraat Bankası"  
            bold:True
            font_size:24
            color:1,0,0,1
          Button:
            text:"iban Adresini Kopyala"
            size_hint_x:0.25
            size_hint_y:0.3
            font_size:20
            bold:True  
            color:0,1,0,1
            on_press: root.copy_text("TR22 0006 2000 0190 0006 6448 27")
          Button:
            text:"iban Adresini Kopyala"
            size_hint_x:0.25
            size_hint_y:0.3
            font_size:20
            bold:True   
            color:0,0,1,1
            on_press: root.copy_text("TR73 0006 7010 0000 0036 0485 43")
          Button:
            text:"iban Adresini Kopyala"
            size_hint_x:0.25
            size_hint_y:0.3
            font_size:20
            bold:True         
            color:1,0,0,1
            on_press: root.copy_text("TR 2900 0100 0033 6181 2041 5004")
        GridLayout:
          cols:3
          rows:3
          size_hint_x:0.91
          size_hint_y:0.24
          pos_hint:{"x":0.05,"y":0.35}
          Image:
            size_hint_x:0.8
            size_hint_y:0.8
            source:r"C:/Users/halil/OneDrive/Masaüstü/qruygulaması/tether.png"
          Image:
            size_hint_x:0.8
            size_hint_y:0.8
            source:r"C:/Users/halil/OneDrive/Masaüstü/qruygulaması/bitcoin.png"
          Image:
            size_hint_x:0.8
            size_hint_y:0.8
            source:r"C:/Users/halil/OneDrive/Masaüstü/qruygulaması/bnb.png"
          Label:
            text:"USDT-TRC20 "
            font_size:20
            color:0,0,0,1
            bold:True
            size_hint_y:None
          Label:
            text:"BITCOIN-BITCOIN"
            font_size:20
            color:0,0,0,1
            bold:True
            size_hint_y:None
          Label:
            text:"BNB-BEP20"
            font_size:20
            color:0,0,0,1
            bold:True
            size_hint_y:None  
          Button:
            text:"Adresi kopyalayınız"
            size_hint_x:0.25
            size_hint_y:0.35
            font_size:20
            bold:True   
            color:0,0,0,1
            id:dolarbutonu
            on_press: root.copy_text("TAV5aVNYeapfVyriQkk7HEgMj5cXK8e1b5")
          Button:
            text:"Adresi kopyalayınız"
            size_hint_x:0.25
            size_hint_y:0.35
            font_size:20
            bold:True   
            color:0,0,0,1  
            id:bitcoinbutonu
            on_press: root.copy_text("1AhTnPiBKkP1eCeCTh4U5LnDH6FDU3xk7u")
          Button:
            text:"Adresi kopyalayınız"
            size_hint_x:0.25
            size_hint_y:0.35
            font_size:20
            bold:True   
            color:0,0,0,1
            on_press: root.copy_text("0x9097869444245552229b4bee960c90f95864e221")
            id:bnbbutonu
#:import Factory kivy.factory.Factory
<dosya_popup>:
  title:"Lütfen Dosya Seçiniz"
  BoxLayout:
    orientation: "vertical"

    FileChooserListView:
      id: filechooser
      
      path: "/"
      filters: ["*.png", "*.jpg", "*.jpeg", "*.gif"]  # Sadece resim dosyalarını göster
      

    Button:
      text: "Seç"
      font_size: 20
      size_hint_y: 0.1
      bold: True
      color: 0, 1, 0, 1
      on_press: root.on_select(filechooser.selection)
      

    Button:
      text: "Vazgeç"
      font_size: 20
      size_hint_y: 0.1
      bold: True
      color: 1, 0, 0, 1
      on_press: root.dismiss()





         
""")


class QROLUŞTUR(Screen):
      selected_file=""
    
      class dosya_popup(Popup):
            Factory.register("dosya_popup", module="dosya_popup")    
            
            def is_image_file(self, filename):
              image_extensions = [".png", ".jpg", ".jpeg", ".gif"]
              return any(filename.lower().endswith(ext) for ext in image_extensions)
            def on_select(self,selected_files):
              
              
              if selected_files:
                  QROLUŞTUR.selected_file = selected_files[0]
              self.dismiss()

      def QRFiltre(self):
          if QROLUŞTUR.selected_file=="":
                        
              qr = qrcode.QRCode(
              version=1,  # QR kodunun versiyonu
              error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
              box_size=16,  # Kutu boyutu
              border=4,  # Kenar boşluğu
              )

              # QR kodu içerecek metni belirtin
              metin =self.ids.qr_metni.text 

              # QR kodunu oluşturmak için add_data() yöntemini kullanın
              qr.add_data(metin)
              qr.make(fit=True)
              arkaplan_rengi=self.ids.arkaplan_spinner.text
              qr_rengi=self.ids.qr_spinner.text
              

              if qr_rengi=="Renkler":
                  qr_rengi="black"
              elif qr_rengi=="sarı":
                  qr_rengi="yellow"
              elif qr_rengi=="mavi":
                  qr_rengi="blue"
              elif qr_rengi=="yeşil":
                  qr_rengi="green"
              elif qr_rengi=="turuncu":
                  qr_rengi="orange"
              elif qr_rengi=="mor":
                  qr_rengi="purple"
              elif qr_rengi=="beyaz":
                  qr_rengi="white"
              elif qr_rengi=="pembe":
                  qr_rengi="pink"
              elif qr_rengi=="siyah":
                  qr_rengi="black"
              elif qr_rengi=="kırmızı":
                  qr_rengi="red" 
                        

              if  arkaplan_rengi=="Renkler":
                  arkaplan_rengi="white"
              
              elif arkaplan_rengi=="mavi":
                  arkaplan_rengi="blue"
              elif arkaplan_rengi=="sarı":
                  arkaplan_rengi="yellow"
              elif arkaplan_rengi=="kırmızı":
                  arkaplan_rengi="red"
              elif arkaplan_rengi=="yeşil":
                  arkaplan_rengi="green"
              elif arkaplan_rengi=="turuncu":
                  arkaplan_rengi="orange"
              elif arkaplan_rengi=="mor":
                  arkaplan_rengi="purple"
              elif arkaplan_rengi=="beyaz":
                  arkaplan_rengi="white"
              elif arkaplan_rengi=="pembe":
                  arkaplan_rengi="pink"
              elif arkaplan_rengi=="siyah":
                  arkaplan_rengi="black"                                               
              
              

              

              # QR kodunu oluşturmak için make_image() yöntemini kullanın
              img = qr.make_image(fill_color=f"{qr_rengi}" , back_color=f"{arkaplan_rengi}")
              rastsal=randint(1,100000000)
      # Oluşturulan QR kodunu bir dosyaya kaydedin (örneğin, "qrcode.png")
              img.save(f"'QR dönüştürücü'{rastsal}.png")

              # Kullanıcıya QR kodunu gösterin
          
              img.show()
              
          else:
              
            
      
              
              
            
      
         # qrcode kütüphanesini yükleyin

    
        # QR kodu oluşturmak için bir QRCode nesnesi oluşturun
              qr = qrcode.QRCode(
                  version=1,  # QR kodunun versiyonu
                  error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
                  box_size=16,  # Kutu boyutu
                  border=4,  # Kenar boşluğu
              )

              # QR kodu içerecek metni belirtin
              metin =self.ids.qr_metni.text 

              # QR kodunu oluşturmak için add_data() yöntemini kullanın
              qr.add_data(metin)
              qr.make(fit=True)
              arkaplan_rengi=self.ids.arkaplan_spinner.text
              qr_rengi=self.ids.qr_spinner.text
              

              if qr_rengi=="Renkler":
                  qr_rengi="black"
              elif qr_rengi=="sarı":
                  qr_rengi="yellow"
              elif qr_rengi=="mavi":
                  qr_rengi="blue"
              elif qr_rengi=="yeşil":
                  qr_rengi="green"
              elif qr_rengi=="turuncu":
                  qr_rengi="orange"
              elif qr_rengi=="mor":
                  qr_rengi="purple"
              elif qr_rengi=="beyaz":
                  qr_rengi="white"
              elif qr_rengi=="pembe":
                  qr_rengi="pink"
              elif qr_rengi=="siyah":
                  qr_rengi="black"
              elif qr_rengi=="kırmızı":
                  qr_rengi="red" 
                        

              if  arkaplan_rengi=="Renkler":
                  arkaplan_rengi="white"
              
              elif arkaplan_rengi=="mavi":
                  arkaplan_rengi="blue"
              elif arkaplan_rengi=="sarı":
                  arkaplan_rengi="yellow"
              elif arkaplan_rengi=="kırmızı":
                  arkaplan_rengi="red"
              elif arkaplan_rengi=="yeşil":
                  arkaplan_rengi="green"
              elif arkaplan_rengi=="turuncu":
                  arkaplan_rengi="orange"
              elif arkaplan_rengi=="mor":
                  arkaplan_rengi="purple"
              elif arkaplan_rengi=="beyaz":
                  arkaplan_rengi="white"
              elif arkaplan_rengi=="pembe":
                  arkaplan_rengi="pink"
              elif arkaplan_rengi=="siyah":
                  arkaplan_rengi="black"                                               
              
              

              

              # QR kodunu oluşturmak için make_image() yöntemini kullanın
              img = qr.make_image(fill_color=f"{qr_rengi}" , back_color=f"{arkaplan_rengi}")
              
              
              
                  
                  # Resmi aç
              logo_path =QROLUŞTUR.selected_file # Kullanmak istediğiniz logo dosya yolu
              logo = PILImage.open(logo_path)
              
              # Logo boyutunu QR koduyla aynı hale getir
              logo = logo.resize((img.size[0] // 8, img.size[1] // 8))

              # Logo'yu QR kodunun ortasına yerleştir
              x = (img.size[0] - logo.size[0]) // 2
              y = (img.size[1] - logo.size[1]) // 2
              img.paste(logo, (x, y), None)
              
              rastsal=randint(1,100000000)
              # Oluşturulan QR kodunu bir dosyaya kaydedin (örneğin, "qrcode.png")
              img.save(f"'QR dönüştürücü'{rastsal}.png")

              # Kullanıcıya QR kodunu gösterin
          
              img.show()
      
      

          
    
class QROKUT(Screen):
   def qr_code_reader():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        # Farklı iyileştirmeleri uygula
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, threshold = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY)

        decoded_objects = decode(threshold)

        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(points)
                points = hull
            num_of_points = len(points)
            for j in range(num_of_points):
                cv2.line(frame, tuple(points[j]), tuple(points[(j+1)%num_of_points]), (0, 0, 255), 2)

            cv2.putText(frame, data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("QR Code Reader", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
class İLETİŞİM(Screen):


    def copy_text(self, text):
        Clipboard.copy(text)

    def open_etsy(self):
            webbrowser.open("https://www.etsy.com/shop/CreativeByHalil")

    def open_youtube(self):
            webbrowser.open("https://www.youtube.com/@startnowdoing")

    def open_downloader(self):
            webbrowser.open("https://videoandmp3download.com/")




    
class MyApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(QROLUŞTUR(name="QROLUŞTUR"))
        sm.add_widget(QROKUT(name="QROKUT"))
        sm.add_widget(İLETİŞİM(name="İLETİŞİM"))
        return sm

if __name__ == "__main__":
    Window.clearcolor=0,1,0.9,1
    MyApp().run()