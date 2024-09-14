import streamlit as st

alpha="abcdefghijklmnopqrstuvwxyz"
# Define encryption function
def encryption(txt, val):
    newtxt = ""
    
    for i in txt:
        if(i.isupper()):
            newtxt+=chr((ord(i) + val-65) % 26 + 65)
        else:
            newtxt+=chr((ord(i) + val-97) % 26 + 97)

    return newtxt

# Define decryption function
def decryption(txt, val):
    newtxt = ""
    for i in txt:
        if(i.isupper()):
            newtxt+=chr((ord(i) - val-65) % 26 + 65)
        else:
            newtxt+=chr((ord(i) - val-97) % 26 + 97)
            
    return newtxt

# Streamlit UI setup
st.title("🔒 Text Encryption and Decryption Tool")

# Instructions
st.write("""
This tool allows you to encrypt and decrypt a message by shifting each character by a specified value.
Simply enter your message, choose a shift value, and hit the respective button!
""")

# Creating two columns for better layout
col1, col2 = st.columns(2)

# Input for encryption
with col1:
    st.subheader("Encryption")
    text_to_encrypt = st.text_area("Enter message to encrypt", "")
    shift_value_enc = st.number_input("Select shift value for encryption", min_value=1, max_value=100, step=1, value=3)
    
    if st.button("🔐 Encrypt"):
        if text_to_encrypt:
            encrypted_text = encryption(text_to_encrypt, shift_value_enc)
            st.success(f"Encrypted text: {encrypted_text}")
        else:
            st.error("Please enter text to encrypt.")

# Input for decryption
with col2:
    st.subheader("Decryption")
    text_to_decrypt = st.text_area("Enter message to decrypt", "")
    shift_value_dec = st.number_input("Select shift value for decryption", min_value=1, max_value=100, step=1, value=3)
    
    if st.button("🔓 Decrypt"):
        if text_to_decrypt:
            decrypted_text = decryption(text_to_decrypt, shift_value_dec)
            st.success(f"Decrypted text: {decrypted_text}")
        else:
            st.error("Please enter text to decrypt.")

# Footer section
st.write("---")

