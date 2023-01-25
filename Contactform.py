import streamlit as st
<link rel="stylesheet" type="text/css" href="https://github.com/BharatRohit/contact-form/blob/main/style.css">

st.header(":mailbox: Get In Touch With Me!")

Contact_form = """
<form action="https://formsubmit.co/rohitbharat810@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Type your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(Contact_form,unsafe_allow_html=True)

# # Use Local Css File
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}<style>",unsafe_allow_html=True)
# local_css("contactform/style.css")
# https://github.com/BharatRohit/contact-form/blob/main/style.css
# <input type="file" name="attachment" accept="image/png, image/jpeg">
     
