import streamlit as st  
import re

st.set_page_config(page_title="PASSWORD STRANGTH CHECKER",page_icon="🔒")
st.title("🔒 Password strangth checker")
st.markdown("""
            ## welcome to the ultimate password strangth checker 👋
use this simple tool to check the stranth of your password and get suggestion on how to make it stronger
            we will give you helpfull tips to create a **strong password 🔒""")

password = st.text_input("Enter your password", type="password")
feedback =[]
score = 0

if password :
    if len(password)>=8:
        score +=1
    else :
        feedback.append("‼ password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score +=1
    
    else :
        feedback.append("‼ password should contaion both upper and lowercase characters.")
    
    if re.search(r'\d', password):
        score +=1
    else :
        feedback.append("‼ password should contain at least one digit.")
    
    if re.search(r'[!@#$%]',password):
        score +=1
    else: feedback.append("‼ password should contain at least one speacial character (!@#$%).")

    if score == 4:
        feedback.append("✅ your Password is strong.")
    elif score ==3:
        feedback.append("☢ your Password is medium strength. it could be strong.")

    else: feedback.append("🔴your password is weak! please make it strong")


    if feedback:
        st.markdown("## improvement suggestion")
        for tip in feedback:
            st.write(tip)
else:
    st.info("please enter your password to get started.")


