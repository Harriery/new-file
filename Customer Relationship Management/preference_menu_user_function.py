from PyQt6.QtWidgets import *
import sys
from preference_menu_user import Ui_Preference_menu_user 
from application import Ui_Applications
from mentor_interview import Ui_MentorInterview
from interviews import Ui_Interviews
from mentor_interviews_function import MentorInterviewsWindow
from application_function import Application_Window
from interviews_function import Interview_Window


class UserPreferenceMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Preference_menu_user()
        self.ui.setupUi(self)

    
        # Butonlara tıklanınca ilgili fonksiyonu çağır
        self.ui.pushButton_applications.clicked.connect(self.open_applications)
        print("pushButton_applications bağlandı.")
        
        self.ui.pushButton_mentorMeeting.clicked.connect(self.open_mentor_interview)
        print("pushButton_mentorMeeting bağlandı.")
        
        self.ui.pushButton_interviews.clicked.connect(self.open_interviews)
        print("pushButton_interviews bağlandı.")
        
        self.ui.pushButton_Exit_2.clicked.connect(self.exit)

        # Yeni pencereleri saklamak için değişkenler
        self.applications_window = None
        self.mentor_interview_window = None
        self.interviews_window = None
        

    def exit(self):
       """Pencereyi kapatır ve uygulamadan çıkar."""
       try:
           self.close()  # Mevcut pencereyi kapat
           print("Pencere başarıyla kapatıldı.")
       except Exception as e:
           print(f"Pencere kapatılırken hata oluştu: {e}")

    def open_applications(self):
        
        print("Application butonuna basıldı (User olarak açılıyor).")
        self.application_window = Application_Window(user_type="user")  # Doğru şekilde çağır
        self.application_window.show()
        self.close()


    def open_mentor_interview(self):
        print("Mentor Interview butonuna basıldı (User olarak açılıyor).")
        self.mentor_interview_window = MentorInterviewsWindow(user_type="user")  # User olduğunu belirtiyoruz
        self.mentor_interview_window.show()
        self.close()




    def open_interviews(self):
        print("Interviews butonuna basıldı.")
        self.interviews_window =Interview_Window(user_type="user")
        self.interviews_window.show()
        self.close()