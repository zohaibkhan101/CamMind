# CamMind - AI CCTV Surveillance System

CamMind is an AI-powered CCTV surveillance system built in Python. It uses your device's camera (webcam or IP camera) and a pretrained vision-language model (BLIP) to generate real-time scene descriptions. Ideal for smart surveillance use cases, it helps you monitor, log, and even raise alerts for suspicious activity directly on your local system.

---

## 📸 Features

- 🔹 Real-time video feed processing from webcam
- 🔹 Scene understanding using a vision-language model (BLIP from Hugging Face)
- 🔹 Text overlay of live scene captions
- 🔹 Custom "judgement" logic for suspicious activity
- 🔹 Keyboard interrupt to quit easily (`q` key)
- 🔹 Runs locally — no need for browser or internet after setup

---

## 🔧 Installation and Setup

Follow the steps below to set up and run the project on your local machine.

### 1. Clone the Repository


git clone https://github.com/zohaibkhan101/CamMind.git
cd CamMind
2. Create a Virtual Environment
On Windows:



python -m venv venv
venv\Scripts\activate
On macOS/Linux:



python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
If you have a requirements.txt file:


pip install -r requirements.txt
Otherwise, manually install the required packages:


pip install torch torchvision transformers opencv-python
🔍 You can verify Torch installation instructions for your system at: https://pytorch.org/get-started/locally/

🚀 How to Run the System
To run the AI CCTV surveillance system:

t
python aicctv.py
This will:

Open your default webcam

Continuously capture frames

Use the BLIP model to generate scene captions

Display the frame with the caption overlaid

🔴 Stop the Surveillance
Press the q key while the camera window is active to stop the program.

🧠 Judgement Logic (Optional)
You can customize logic in aicctv.py to raise alerts when a specific condition is met. Example:


if "person" not in caption:
    print("⚠️ Alert: No person detected!")
elif "sleeping" in caption:
    print("⚠️ Alert: Inactive person detected!")
📁 Project Structure

CamMind/
│
├── aicctv.py               # Main surveillance script
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── snapshots/              # (Optional) Saved images from alerts
├── logs/                   # (Optional) Event logs with timestamps
✅ Prerequisites
Python 3.7+

Webcam or IP CCTV feed (for future expansion)

Internet connection (for first-time model download)

💡 Future Features (Planned)
📈 Dashboard with live feed and analytics

🌐 IP camera integration

📲 Telegram/Discord bot alerts

🧠 Suspicious behavior detection using rule-based or ML models

🧾 SQLite or CSV-based log history

🖼️ Snapshot saving with captions

🙋‍♂️ Author
Zohaib Khan
GitHub: @zohaibkhan101

📝 License
This project is licensed under the MIT License. See the LICENSE file for more information.
