# UV Streamlit App

An interactive web app built with [Streamlit](https://streamlit.io/) and managed using [uv](https://github.com/astral-sh/uv), a fast Python package manager and virtual environment tool.

## 🚀 Features

- Simple Streamlit interface
- uv-powered virtual environment (no manual activation needed)
- Clean `.gitignore` setup
- Ready for deployment or extension

## 📦 Tech Stack

- Python 3
- Streamlit
- uv (for dependency and environment management)

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/uv-streamlit-app.git
   cd uv-streamlit-app
   ```

2. Install dependencies using uv:
   ```bash
   uv venv
   uv pip install streamlit
   ```

3. Run the app:
   ```bash
   uv run streamlit run app.py
   ```

## 📁 Project Structure

```
uv-streamlit-app/
├── app.py
├── .gitignore
├── uv.lock
└── README.md
```

## 🧠 Notes

- No need to activate `.venv` manually — uv handles it for you.
- Press `Ctrl + C` to stop the app in terminal.
- You can use `Ctrl + F5` in VS Code if you’ve set up a task.

## 📄 License

This project is licensed under the MIT License.