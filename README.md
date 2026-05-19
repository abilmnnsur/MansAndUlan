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
├── bot.py                 

├── config.py              

├── requirements.txt       

├── .gitignore             

├── data/

│   └── history.json       


├── handlers/              

│   ├── start.py           

│   ├── qr.py              

│   └── history.py         


├── services/              

│   ├── qr_service.py      

│   └── file_manager.py    


├── models/               

│   ├── base_qr.py         

│   ├── text_qr.py         

│   ├── url_qr.py        

│   ├── wifi_qr.py         

│   └── contact_qr.py      


├── keyboards/            

│   └── menu.py            


└── utils/                 

└── validators.py      

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

screens 
start and menu <img width="1182" height="985" alt="image" src="https://github.com/user-attachments/assets/f791eda3-875d-41d9-a053-a6d80a6f1311" />

types of QR 
<img width="399" height="201" alt="image" src="https://github.com/user-attachments/assets/bce52d08-4a32-4324-b13f-d713313ddb66" />
<img width="632" height="677" alt="image" src="https://github.com/user-attachments/assets/6208fec6-7707-43ff-97b9-c86405621b92" />
<img width="619" height="689" alt="image" src="https://github.com/user-attachments/assets/75279a8b-537d-43c3-aa1e-71f70715079c" />
<img width="653" height="805" alt="image" src="https://github.com/user-attachments/assets/247b159e-e5e9-4a4f-b5fa-03071151c4ef" />
<img width="624" height="755" alt="image" src="https://github.com/user-attachments/assets/1e842920-2adb-4e87-a05d-4513ed10fe55" />

history <img width="389" height="446" alt="image" src="https://github.com/user-attachments/assets/9e5ae130-5dc6-4d41-9664-b64dda21e33b" />

help <img width="620" height="134" alt="image" src="https://github.com/user-attachments/assets/9af44173-31b7-4110-bb43-5d59bfbed8e7" />

about <img width="432" height="137" alt="image" src="https://github.com/user-attachments/assets/2891b3ac-1677-40cb-b87b-38c3abc83c4e" />