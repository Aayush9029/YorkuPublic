# 🌍 YorkuPublic - Public api server for YorkU iOS App.


### 📁 Directory Structure

```bash
# server-branch
├── README.md
└── server
    ├── get_api
    │   ├── google_news.py
    │   ├── __init__.py
    │   ├── reddit_post.py
    │   ├── twitter_post.py
    │   └── utils.py
    ├── server.py
    ├── logs
    │   ├── log.log
    │   └── old_logs/
    ├── Pipfile
    ├── Pipfile.lock
    └── requirements.txt

2 directories, 13 files
```

### 🐍 Usage

```bash
# clone repo
git clone https://github.com/Aayush9029/YorkuPublic

# checkout server branch
git checkout server

# go to server folder
cd server

# activate pipenv (optional)
pipenv shell

# install dependencies
pip install -r requirements.txt

# run server
python3 server.py

# run server - background mode
nohup python3 server.py & > /dev/null
```
---

⚠️ **NOTE:** The API Structure can change at any point as i'm still polishing things on my end
