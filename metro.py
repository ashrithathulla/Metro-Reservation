import streamlit as st
import qrcode
from io import BytesIO
import uuid
from PIL import Image
from gtts import gTTS
import base64


def generate_qr(data):
    qr=qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    return img

st.title("Metro Ticketbooking Systemwith QRCode+Auto voice")

stations=["LB Nagar","Nagole","Uppal","Tarnaka","Habsiguda","Metuguda","Secundrabad"]
name=st.text_input("passanger name")
source=st.selectbox("Source station",stations)
destination=st.selectbox("Destination Station",stations)
no_ticket=st.number_input("Number of Ticket",min_value=1,value=1)
price_per_ticket=30
total_amount=no_ticket*price_per_ticket
st.info(f"Total Amount: (total_amount)")
if st.button("Book Ticket"):
    if name.strip()=="":
        st.error("Please Enter passenger name")
    elif source==destination:
        st.error("Source and Destination cannot be the same.Please select different stations")
    else:
        booking_id=str(uuid.uuid4())[1:8]
        qr_data=(
                f"BookingID:[bookingId\n"
                f"name:{name}\nFrom:(source)\nTo:{destination}\n Ticket:{no_ticket}"
                )
        qr_img=generate_qr(qr_data)
        buf=BytesIO()
        qr_img.save(buf,format="PNG")
        qr_bytes=buf.getvalue()

        st.success("Ticket Booking Successfully")
        st.write("###Ticket Details")
        st.write(f"**Booking ID*** {booking_id}")
        st.write(f"**Passengers:** {name}")
        st.write(f"**From** {source}")
        st.write(f"**To:** {destination}")
        st.write(f"**Tickets:** {no_ticket}")
        st.write(f"**Amount paid:** {total_amount}")
        st.image(qr_bytes, width=250)         
            
    

