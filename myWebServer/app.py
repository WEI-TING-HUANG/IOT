from flask import Flask, render_template, Response, session
from camera import VideoCamera
import RPi.GPIO as GPIO

app = Flask(__name__)
app.secret_key='sjehfjeefrjewth43u' 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)         #LED output pin


@app.route('/')
def index():
    return render_template('index.html' , sound_flag=session.get('soundFlag'))

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sound_feed')
def sound_feed():
    if session.get('soundFlag') == 0:
        session['soundFlag'] = 1
    else:
        session['soundFlag'] = 0
    
    GPIO.output(37, session.get('soundFlag'))
    return render_template('index.html' , sound_flag=session.get('soundFlag'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
    session['soundFlag'] = 0
