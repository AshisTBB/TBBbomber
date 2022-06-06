import requests
from requests.structures import CaseInsensitiveDict
print("\033[H\033[J")
print("""


feglat("asb")
                    T_B_B
         TÊÃM BLÅÇK BËRRY
         Created by: ÅSB ÃSHÏS BÎSWÅS
                    TBB C_O

  
  
  Creator: Asb Ashis Biswas
  Facebook : https://www.facebook.com/profile.php?id=100074238783251
 

  """)                                                        
number=str(input("Enter Terget Number:+88 "))
amount=int(input("Enter Terget Amount: "))
txt = "we facked you"


data = "phone="+number


for i in range(amount):
    resp = requests.post(txt, data=data)
    print(str(i+1)+"SMS SENT")
