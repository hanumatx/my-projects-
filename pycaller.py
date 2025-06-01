import tkinter as tk
from PIL import Image, ImageTk
import phonenumbers as ph 
from phonenumbers import carrier, geocoder, timezone, PhoneNumberType, NumberParseException 

def get_phone_number_details(phone_number):
    try:

        number = ph.parse(phone_number)

        if not ph.is_valid_number(number):
           return "Invalid Phone Number"

        timezones = timezone.time_zones_for_number(number)
        carrier_name = carrier.name_for_number(number, "en")
        location = geocoder.description_for_number(number, "en")
        country_code = number.country_code
        national_number = number.national_number

        number_type = ph.number_type(number)
        number_type_str = {
            PhoneNumberType.FIXED_LINE: "Fixed line",
            PhoneNumberType.MOBILE: "Mobile",
            PhoneNumberType.PREMIUM_RATE: "Premium rate",
            PhoneNumberType.SHARED_COST: "Shared cost",
            PhoneNumberType.VOIP: "VoIP",
            PhoneNumberType.PAGER: "Pager",
            PhoneNumberType.UAN: "UAN",
            PhoneNumberType.PERSONAL_NUMBER: "personal number",
            PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed line or mobile",
            PhoneNumberType.VOICEMAIL:  "Voicemail",
            PhoneNumberType.UNKNOWN: "unknown",
    }.get(number_type, "Unknown")
        
        details = {
 
        "Country Code": country_code,
        "National Number": national_number,
        "Number Type": number_type_str,
        "Timezone": timezones,
        "Carrier": carrier_name,
        "Location": location
    
    }

        return details
    except NumberParseException as e:
     return str(e)
    
def fetch_details():
    phone_number = input("Enter the phone number:")

    details = get_phone_number_details (phone_number)



    if isinstance(details, dict):

       result = "\n".join([f"{key}: {value}" for key, value in details.items()])

    else:

        result = details

    result_label.config(text=result)

root = tk.Tk()
root.title("Phone Number Details")

root.mainloop()

window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth
screen_height = root.winfo_screenheight
position_top =   int(screen_height/ 2 - window_height/ 2)
position_right = int(screen_width/ 2 - window_width/ 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

logo = Image.open(r"C:\Users\32han\Downloads\pngegg.png")
logo = logo.resize((100,100),Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)
Image_label = tk.Label(root,image=logo)
logo.label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady = 20)

tk.Label(frame, text="Enter phone number:").grid(row=0, column=0, padx=10, pady=10)

entry = tk.entry(frame,width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(frame, text="Get Details", command=fetch_details)
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.label( root, texts="", justify="left")
result_label.pack(pady=10)

root.mainloop()
