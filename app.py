from flask import Flask
import subprocess
from datetime import datetime
import pytz
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Name and Username
    name = "Chandan Neralgi"  # Replace with your full name
    username = os.getlogin()
    
    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f %Z')
    
    # Top Output
    top_output = subprocess.getoutput('top -bn1')

    # Format and return the response
    result = f"<h1>Name: {name}</h1>"
    result += f"<h2>Username: {username}</h2>"
    result += f"<h2>Server Time (IST): {server_time}</h2>"
    result += f"<pre>{top_output}</pre>"

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
