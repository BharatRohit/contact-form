import streamlit as st
st.header(":mailbox: Get In Touch With Me!")

Contact_form = """
<form action="https://formsubmit.co/rohitbharat810@gmail.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""
st.markdown(Contact_form,unsafe_allow_html=True)
