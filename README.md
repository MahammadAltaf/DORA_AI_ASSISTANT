  # 🎙️ Dora - Voice Assistant (Advanced Python Practice Project)

**Dora** is a smart, voice-controlled assistant developed as a hands-on practice project using advanced Python modules. It simulates a real AI assistant's behavior, such as recognizing voice commands, speaking responses, and opening websites or music—helping explore real-time audio interaction programming.

---

## 📁 Project Structure

```
├── main.py               # Main logic for voice command processing
├── musicLibrary.py       # Dictionary storing music name & YouTube links
├── requirements.txt      # Python dependencies
```

---

## 🚀 Features

- **Wake Word Activation**: Responds to the wake word `"Dora"` to begin listening.
- **Speech Recognition**: Uses Google’s online speech recognition for accuracy.
- **Voice Feedback**: Speaks back using `pyttsx3`.
- **Command Execution**:
  - Open sites like Google, Facebook, LinkedIn, YouTube
  - Play predefined songs via YouTube
- **Natural Exit Commands**: Say "bye", "goodbye", "exit", etc., to end the session.

---

## 🎵 Supported Music Commands

| Command         | Song Title | YouTube Link |
|-----------------|------------|--------------|
| `play jab`      | Jab        | [Watch](https://youtu.be/K-Ts-NFR62o?si=dyUFjX7qPHxudt3I) |
| `play lose`     | Lose       | [Watch](https://youtu.be/VJxppgsHjF8?si=khsinnZu5oBafYw5) |
| `play munjane`  | Munjane    | [Watch](https://youtu.be/xNR4FAEGxV4?si=0hGOtnE7rd_RXFvs) |

---

## 💻 Setup Instructions

### 1. Clone or Download
Clone the repo or download the `.zip` and extract it.

### 2. Install Dependencies
Make sure you are in the project directory. Then run:

```bash
pip install -r requirements.txt
```

### 3. Run the Assistant

```bash
python main.py
```

---

## 🧠 Modules & Technologies Used

- `speech_recognition` – for capturing and recognizing voice
- `pyttsx3` – for converting text to speech
- `pocketsphinx` – offline speech recognition backend
- `webbrowser` – to open URLs in the default browser
- `requests` – pre-integrated for future enhancements
- `PyAudio` – for microphone support

---

## ✅ Use Case

This project is designed as an **advanced Python practice tool**, not a full AI assistant. It serves as a real-world playground to work with:

- Voice interface development
- Speech-to-text & text-to-speech integration
- Real-time audio input handling
- Error handling & timeouts

---

## 🙋‍♂️ Developer

**Mahammad Altaf**  
Python | AI | IoT | Voice Systems  
[LinkedIn Profile](https://www.linkedin.com/in/mahammad-altaf-842326289)

---

## 📌 Note

While this is not a production-grade AI assistant, it mimics one well for learning purposes. Future enhancements can include:
- Dynamic music search
- Weather updates
- GUI with PyQt or Tkinter
- Offline fallback with Sphinx

---
