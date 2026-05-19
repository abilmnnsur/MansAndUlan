A Telegram bot that generates QR codes from different types of data (text, URL, Wi-Fi credentials, and contact information) and stores user generation history.

📱 Features
🔗 URL → QR code generation
📝 Plain text → QR code
📶 Wi-Fi credentials → QR code (WPA/WEP format support)
👤 Contact cards → vCard QR codes
📊 User history tracking (last 5 requests)
🔄 Interactive step-by-step input via FSM
🧠 Input validation (empty input, format checks)
💾 Local JSON storage system
⚡ Async API requests (non-blocking bot execution)
🗂️ Project Structure
uniqr-bot/
├── bot.py                 # Main entry point
├── config.py              # Configuration and environment variables
├── requirements.txt       # Dependencies
├── .env                   # Secret token (not committed)
├── .gitignore            # Ignored files

├── data/
│   └── history.json      # User request history storage

├── handlers/
│   ├── start.py          # /start, /help handlers
│   ├── qr.py             # QR generation FSM logic
│   └── history.py        # History display handler

├── services/
│   ├── qr_service.py     # QR code API integration
│   └── file_manager.py   # JSON read/write operations

├── models/
│   ├── base_qr.py        # Abstract QR class
│   ├── text_qr.py        # Text QR implementation
│   ├── url_qr.py         # URL QR implementation
│   ├── wifi_qr.py        # Wi-Fi QR format
│   └── contact_qr.py     # vCard QR format

├── keyboards/
│   └── menu.py           # Telegram UI keyboards

└── utils/
    └── validators.py     # Input validation helpers
⚙️ Installation
1. Clone repository
git clone <your-repo-url>
cd uniqr-bot
2. Create virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Create .env file
BOT_TOKEN=your_telegram_bot_token_here

Get token from @BotFather on Telegram.

🚀 Running the Bot
python bot.py

Expected output:

Bot started successfully
Polling started...
🤖 Bot Commands
Command	Description
/start	Start main menu
/help	Show help message
/history	Show last QR requests
🧠 Architecture

The project follows a modular structure:

Handlers — Telegram event logic and user interaction
Services — API requests and file operations
Models — QR data types with OOP inheritance
Keyboards — Telegram UI buttons
Utils — input validation helpers
OOP Design

All QR types inherit from a base abstract class:

BaseQR defines common interface
Each subclass implements its own formatting logic
Bot works with all QR types through polymorphism
⚡ Key Implementation Details
Async API handling

Synchronous requests are executed safely using:

asyncio.to_thread(requests.post, ...)
FSM (Finite State Machine)

Used for step-by-step QR data collection.

JSON storage

User history is stored locally in:

data/history.json

Each user has independent tracking.

🔐 Security
Bot token stored in .env
.env excluded via .gitignore
No sensitive data hardcoded
📄 License

MIT — free to use and modify.

💡 Summary

UniQR Bot is a lightweight Telegram tool demonstrating:

asynchronous programming in Python
modular architecture design
OOP principles (inheritance & polymorphism)
API integration and FSM-based interaction
