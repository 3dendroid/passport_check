## 🪪 Check status passport status
Automated script for checking the passport creating status

## 📂 Project Structure
```
├── pages/                  # Selenium Page Objects
│   └── main_page.py
├── tests/                  # Test cases
│   └── test_claim_reward.py
├── utilities/              # Helpers
│   ├── telegram_notifier.py
│   └── data.py
├── .env                    # Local environment config
├── requirements.txt
├── Dockerfile              # Optional: for Railway deployment
└── README.md
```

## 🚀 Features
- 🔐 Automation check the status of the passport
- 📲 Sends notification to Telegram
- 🌐 Supports local and Railway environments

## 🛠️ Tech Stack
- Python 3.11+
- Selenium WebDriver
- Pytest
- Telegram Bot API
- Railway (Docker)
- dotenv (`.env` support)