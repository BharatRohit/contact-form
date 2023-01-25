import streamlit as st
st.header(":mailbox: Get In Touch With Me!")

Contact_form = """
<form action="https://formsubmit.co/rohitbharat810@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Type your message here"></textarea>
    <input type="file" name="attachment" accept="image/png, image/jpeg">
     <button type="submit">Send</button>
</form>
"""

st.markdown(Contact_form,unsafe_allow_html=True)
