# 🤝 Personal Assistant — AI-Powered n8n + Streamlit App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![n8n](https://img.shields.io/badge/Powered%20by-n8n-orange?logo=n8n)](https://n8n.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Your AI-powered personal assistant connected to n8n — manage your calendar, emails, tasks, notes, and expenses via a beautiful conversational UI.**
>
> ---
>
> ## ✨ Features
>
> | Capability | Description |
> |---|---|
> | 🧠 **Q&A** | Get accurate answers on virtually any topic instantly |
> | 📅 **Calendar & Meetings** | Arrange, reschedule, and manage your calendar events |
> | 📧 **Email Management** | Read, reply, and summarize your emails effortlessly |
> | ✅ **Task Management** | Create and manage your to-do lists and reminders |
> | 📝 **Quick Notes** | Capture ideas and notes on the fly with ease |
> | 💰 **Expense Tracking** | Log and monitor your expenses and budget smartly |
>
> ---
>
> ## 🏗️ Tech Stack
>
> - **Frontend UI**: [Streamlit](https://streamlit.io) — fast, interactive Python web app
> - - **Workflow Automation**: [n8n](https://n8n.io) — self-hosted AI workflow engine
>   - - **AI Backend**: Connected via n8n webhook to LLM agents
>     - - **Language**: Python 3.9+
>      
>       - ---
>
> ## 🚀 Getting Started
>
> ### Prerequisites
>
> - Python 3.9+
> - - n8n instance running (local or cloud)
>   - - Streamlit
>    
>     - ### Installation
>    
>     - ```bash
>       # 1. Clone the repository
>       git clone https://github.com/Sameer051022/personal-assistant-n8n.git
>       cd personal-assistant-n8n
>
>       # 2. Create and activate a virtual environment
>       python -m venv venv
>       source venv/bin/activate  # On Windows: venv\Scripts\activate
>
>       # 3. Install dependencies
>       pip install -r requirements.txt
>       ```
>
> ### Configuration
>
> Create a `.env` file (or set Streamlit secrets) with your n8n webhook URL:
>
> ```env
> N8N_WEBHOOK_URL=https://your-n8n-instance.com/webhook/your-webhook-id
> ```
>
> Or configure via `streamlit/secrets.toml`:
>
> ```toml
> N8N_WEBHOOK_URL = "https://your-n8n-instance.com/webhook/your-webhook-id"
> ```
>
> ### Run Locally
>
> ```bash
> streamlit run app.py
> ```
>
> Open your browser at `http://localhost:8501`
>
>
> ## 📁 Project Structure
>
> ```
> personal-assistant-n8n/
> ├── app.py                  # Main Streamlit application
> ├── requirements.txt        # Python dependencies
> ├── .env.example            # Example environment variables
> ├── .gitignore              # Python gitignore
> └── README.md               # This file
> ```
>
> ---
>
> ## 🔧 n8n Workflow Setup
>
> This app communicates with an n8n workflow via a **webhook trigger**. The workflow handles:
>
> 1. **Message Routing** — Routes user messages to the correct AI agent
> 2. **Calendar Integration** — Connects to Google Calendar / Outlook
> 3. **Email Integration** — Reads and sends emails via Gmail / Outlook
> 4. **Task Management** — Syncs with your task management tool
> 5. **Notes & Finance** — Stores notes and tracks expenses
>
> To import the workflow, export your n8n workflow as JSON and add it to a `/workflow` directory.
>
> ---
>
> ## 🤝 Contributing
>
> Contributions are welcome! Please feel free to submit a Pull Request.
>
> 1. Fork the project
> 2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
> 3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
> 4. Push to the branch (`git push origin feature/AmazingFeature`)
> 5. Open a Pull Request
>
> ---
>
> ## 📄 License
>
> This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
>
> ---
>
> ## 👤 Author
>
> **Sameer Faisal**
>
> - GitHub: [@Sameer051022](https://github.com/Sameer051022)
>
> ---
>
> <p align="center">Powered by n8n · Built with ❤️ using Streamlit</p>
