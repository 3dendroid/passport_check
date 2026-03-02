# 🛂 Passport Status Checker Bot

Automated Python script designed to monitor the status of a passport application and send real-time notifications via Telegram. Perfect for deployment on cloud platforms like Railway.

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.10+-green.svg)
![Railway](https://img.shields.io/badge/deployed%20on-Railway-black.svg)

## 🚀 Features
- **Automated Monitoring:** Regularly checks the official passport tracking portal.
- **Telegram Notifications:** Sends instant updates (success/status changes) to your Telegram bot.
- **Anti-Bot Detection:** Configured with stealth arguments to bypass basic automation detection.
- **Cloud Ready:** Fully optimized for **Railway** using Nixpacks (Chromium & Chromedriver auto-setup).
- **Headless Mode:** Runs efficiently on servers without a graphical interface.

## 📂 Project Structure
```text
├── pages/                  # Page Object Model (POM)
│   └── main_page.py        # Selectors and logic for the status page
├── tests/                  # Test cases
│   └── test_check_pass.py  # Main script for checking status
├── utilities/              # Helpers
│   ├── telegram_notifier.py # Telegram API integration
│   └── data.py             # Data handling
├── .env                    # Environment variables (Token, IDs)
├── requirements.txt        # Python dependencies
├── nixpacks.toml           # Railway configuration (Chrome setup)
└── README.md
```

## 🛠️ Tech Stack
- **Language:** Python 3.11+
- **Automation:** Selenium WebDriver
- **Orchestration:** Pytest (optional)
- **Notification:** Telegram Bot API
- **Deployment:** Railway (via Nixpacks/Docker)

## ⚙️ Configuration

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/passport-status-checker.git
   cd passport-status-checker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   TELEGRAM_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   PASSPORT_APP_ID=123456789
   # Add any other specific data required by the portal
   ```

## 🚀 Deployment on Railway

This project is optimized for [Railway](https://railway.app/).

### 1. Nixpacks Configuration
The project includes a `nixpacks.toml` file to ensure Google Chrome and Chromedriver are installed in the cloud environment:
```toml
[phases.setup]
nixPkgs = ["python311", "chromium", "chromedriver"]
```

### 2. Railway Settings
- **Start Command:** `python tests/test_check_pass.py` (or your main entry point).
- **Variables:** Add your `.env` content to the **Variables** tab in the Railway dashboard.
- **Health Checks:** Since this is a script/cron job, you might want to disable HTTP health checks.

## 🖥️ Local Usage
To run the script locally (make sure you have Chrome installed):
```bash
python tests/test_check_pass.py
```
*Note: The script is configured to run in `--headless=new` mode by default for server compatibility.*

## 🤝 Contributing
Feel free to fork this repository, open issues, and submit pull requests. Any improvements (like adding more tracking sites) are welcome!

## ⚠️ Disclaimer
This tool is for personal use only. Ensure that your automated checks comply with the Terms of Service of the website you are monitoring.

---
*Created by SUPERDEN*

---
