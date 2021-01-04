# filetomaton

Kinda bored so I decided to organize my Downloads folder. Actually is a pretty bad code that needs to be improved, and only works with a set of filetypes. 

Thinking about how to classify files based on content or something like that.

Create a virtual enviroment using Python 3.8+
```
virtualenv venv
```

Install requirements (actually there are only 2 lol)
```
pip install -r requirements.txt
```

Create a `.env` file containing the folder to track

```
FOLDER_TO_TRACK=/home/cameneses/Downloads
```

Run a daemon on startup or use crontab to run it as `@reboot`

```
source venv/bin/activate && python main.py
```