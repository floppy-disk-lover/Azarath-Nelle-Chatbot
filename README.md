To use either Nelle or Lumina, you need to run the following commands for Windows:
PS> python -m venv venv
PS> venv\Scripts\activate
(venv) PS> python -m pip install chatterbot==1.0.4 pytz
For Linux/Mac:
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install chatterbot==1.0.4 pytz
This project uses some code from RealPython.com Here is the original URL: https://realpython.com/build-a-chatbot-python-chatterbot/
After you have ran the first steps, to run the files, use the following commands:
venv/bin/activate -This will switch to the virtual enviroment then run the following:
python filename.py
IMPORTANT: THIS WILL ONLY WORK IF YOU USE BELOW PYTHON 3.8
