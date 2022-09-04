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
# checkout server branch
git checkout server

# Go to server folder
cd server

# Run server
python3 server.py

# Run server - in background mode
nohup python3 server.py & > /dev/null
```
---

⚠️ **NOTE:** The API Structure can change at any point as i'm still polishing things on my end
