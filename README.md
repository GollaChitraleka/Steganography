**Project Description:** Image Steganography

**Overview:**  
This project demonstrates a simple form of image steganography, where a secret text message is hidden within an image. The core idea is to encode the message into the pixel data of an image without making perceptible changes to the image's appearance. A corresponding decryption process allows the hidden message to be extracted, provided the correct passcode is supplied.

**Key Features:**

- **Image-based Encryption:**  
  The project reads a user-selected image and encodes a secret message into its pixel values. Each character of the message is converted into its ASCII value and embedded into specific color channels (red, green, or blue) of sequential pixels. The image, once modified, is saved as the encrypted image.

- **Decryption Process:**  
  For decryption, the user selects the encrypted image and enters the decryption passcode. The program then reads the pixel data from the encrypted image, reconstructing the message by converting the ASCII values back into characters. Only the correct passcode will allow the hidden message to be revealed.

- **Graphical User Interface (GUI):**  
  A user-friendly interface built with Tkinter (using enhanced styling with `ttk`) simplifies the encryption and decryption processes. The GUI provides:
  - Input fields for entering the secret message and passcode.
  - Buttons to select images for encryption and decryption.
  - Visual feedback via dialogs to confirm successful operations or report errors.

- **Security Consideration:**  
  Although the project uses a passcode to control access to the hidden message, the underlying steganography method is quite basic and is meant primarily for educational and demonstrative purposes. For real-world applications, more advanced techniques would be needed.

- **Usage Flow:**  
  1. **Encryption:**  
     - The user selects an image from their file system.
     - They enter a secret message and a passcode.
     - The message is encoded into the image, which is then saved (preferably as a PNG to avoid compression artifacts) and displayed.
  2. **Decryption:**  
     - The user inputs the same passcode used for encryption.
     - They select the encrypted image.
     - The program extracts and displays the hidden message.

**Output:**

![Screenshot (21)](https://github.com/user-attachments/assets/5be1344c-34cd-4f42-9851-05ad3124a4c0)


![Screenshot (22)](https://github.com/user-attachments/assets/bd6eb997-1841-41fe-823f-7ba92b497852)


![Screenshot (23)](https://github.com/user-attachments/assets/661b241f-8e8d-4757-bb99-405f16234e29)


**Conclusion:**  
This project serves as an accessible introduction to the concepts of steganography and basic image processing using Python and OpenCV. It highlights how digital images can be manipulated to hide information and provides a hands-on example of both the encryption and decryption processes through a modern, user-friendly GUI.
