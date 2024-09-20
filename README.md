# 🔒 Text Encryption and Decryption Tool

This project provides a simple and interactive **Text Encryption and Decryption Tool** built with Python and **Streamlit**. The tool allows you to shift characters of a message by a specified value, which can be used to encrypt or decrypt the message using a Caesar Cipher-like approach.

## Features

- **Text Encryption**: Shifts the characters of the input message by a user-specified value to produce an encrypted output.
- **Text Decryption**: Reverses the encryption process by shifting characters in the opposite direction using the same shift value.
- **User-Friendly Interface**: The tool features an easy-to-use interface with separate sections for encryption and decryption.
- **Real-Time Encryption/Decryption**: As you input text and specify the shift value, the tool processes and displays the encrypted or decrypted result in real-time.

## How It Works

1. **Encryption**: 
   - Each character in the input message is shifted forward by a specified number of positions in the alphabet.
   - The tool supports both uppercase and lowercase letters.
   - Example: With a shift value of 3, "A" becomes "D", "B" becomes "E", and so on.
   
2. **Decryption**:
   - Reverses the process by shifting each character backward by the same shift value used during encryption.
   - Example: With a shift value of 3, "D" becomes "A", "E" becomes "B", etc.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-encryption-decryption-tool.git
   ```

2. Navigate to the project directory:
   ```bash
   cd text-encryption-decryption-tool
   ```

3. Install the required dependencies:
   ```bash
   pip install streamlit
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run text_encryption.py
   ```

2. Open your browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

3. Enter a message in the "Encryption" section, choose a shift value, and click the **Encrypt** button to see the encrypted text.

4. Similarly, in the "Decryption" section, enter the encrypted message, select the same shift value, and click the **Decrypt** button to recover the original message.

## Example

- **Encryption Example**:
  - Input Message: `hello`
  - Shift Value: `3`
  - Encrypted Message: `khoor`
  
- **Decryption Example**:
  - Input Message: `khoor`
  - Shift Value: `3`
  - Decrypted Message: `hello`


## Screenshots
![image](https://github.com/user-attachments/assets/0ec79801-1c3d-4f1e-a004-1600b2ef39f4)

## Contributing

Feel free to fork this repository and contribute enhancements or new features! Pull requests are welcome.

