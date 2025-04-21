import pywhatkit as pwk

phone_number = "+919912988988"
message = "Hello,this is an automated message sent using python"

pwk.sendwhatmsg_instantly(phone_number,message,22,tab_close=True)