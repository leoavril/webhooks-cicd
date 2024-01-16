git pull origin main
pip3 install -r requirements.txt
python app.py &
APP_PID=$!
kill $APP_PID