# 🎙️ Jarvis – Python Voice Assistant with AI

Jarvis is a Python-based voice assistant that listens to your commands, opens websites, plays music, fetches live news, and answers questions using an AI model via Ollama. It works with a wake word system (“Jarvis”) and performs actions hands-free using speech recognition and text-to-speech.

## 🚀 Features
- Wake word detection (“Jarvis”)
- Open websites (Google, YouTube, Facebook, LinkedIn)
- Play songs using voice commands
- Fetch and read live news headlines
- AI-powered conversational replies
- Text-to-Speech voice output
- Local LLM support using Ollama (Gemma)

## 🛠️ Technologies Used
- Python
- SpeechRecognition
- Pyttsx3
- Requests
- BeautifulSoup
- Ollama (Gemma LLM)

📂 Project Structure
jarvis.py  - Main voice assistant  
brain.py   - AI communication module  
musiclib.py - Song library  

⚙️ Installation
pip install speechrecognition pyttsx3 requests beautifulsoup4 ollama

Install and run Ollama model:
ollama pull gemma3:4b

▶️ Run
python jarvis.py

Say "Jarvis" and give commands like:
- Open Google
- Play Tum Hi Ho
- Tell me the news
- What is AI
- Stop

🔮 Future Improvements
- System control (volume, brightness, open applications)
- WhatsApp and Email automation
- GUI interface (desktop or web app)
- Custom wake word training
- Multi-language support
- Smart home integration
