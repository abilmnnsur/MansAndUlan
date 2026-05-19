Project Overview

ловиQrbratishka Bot is a Telegram bot was developed by Abilmansur and Ulan

The bot allows users to generate QR codes from different types of data:

URLs
Plain text
Wi-Fi credentials
Contact information (vCard)

QR codes are generated using the QRCode Monkey API, and user request history is stored locally in JSON format.

Technology Stack
Programming Language: Python 3.14+
Framework: aiogram 3.x
API Integration: requests (wrapped with asyncio.to_thread for non-blocking execution)
Configuration: python-dotenv
Storage: JSON files
Architecture Style: modular structure with OOP principles

project/

│── main.py
├── bot.py
├── config.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── history.json
│
├── handlers/
│   ├── start.py
│   ├── qr.py
│   └── history.py
│
├── services/
│   ├── qr_service.py
│   └── file_manager.py
│
├── models/
│   ├── base_qr.py
│   ├── text_qr.py
│   ├── url_qr.py
│   ├── wifi_qr.py
│   └── contact_qr.py
│
├── keyboards/
│   └── menu.py
│
└── utils/
    └── validators.py
Architecture Overview

The project is divided into logical modules:

handlers/ – Telegram command and message handling
services/ – API requests and file operations
models/ – QR data formats using OOP (inheritance and polymorphism)
keyboards/ – Telegram UI buttons
utils/ – input validation helpers

The BaseQR abstract class defines a common interface for all QR types.
Each subclass implements its own formatting logic (e.g., Wi-Fi string format or vCard format).


Key Implementation Notes
Async API handling

The QRCode Monkey API is synchronous, so blocking requests are executed using:

asyncio.to_thread(requests.post, ...)
FSM usage

The bot uses Finite State Machine (FSM) to collect user input step-by-step during QR generation.

History storage

User requests are saved in data/history.json, limited to the last 5 entries per user.


Team Contribution

Ulan:

Project structure setup
Telegram handlers (start, history)
UI keyboards
QR API integration service

Abilmansur:

OOP model system (QR classes)
FSM logic for QR creation
Input validation system
JSON storage management

Installation
1. Clone repository
git clone <repo-url>
cd project
2. Create virtual environment
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
3. Create .env file
BOT_TOKEN=your_token_here
4. Run bot
python bot.py


Conclusion
This was one of the hardest project we had.We think that we have very well project,good structure and we believe that you will like our project.The hardest part was with handlers, but we fixed it and our project is done.We wish all of best to you and happy to be a student of you
