from flask import Flask, render_template_string, request   # Ukljucivanje Flask modula
import RPi.GPIO as GPIO     # Ukljucivanje GPIO biblioteke
from time import sleep      # Ukljucivanje sleep modula
servo_pin = 2 # GPIO pin
GPIO.setmode(GPIO.BCM)      
# Definisanje servo PIN-a kao izlaznog pina
GPIO.setup(servo_pin, GPIO.OUT)     
p = GPIO.PWM(servo_pin, 50)  
p.start(0) # Prvobitni 0 ciklus
app = Flask(__name__)

TPL = '''
<html>
<style>
div {
  background-image: url('istockphoto-967951076-612x612.jpg');
}
</style>
     
<head>
<title>Web aplikacija za upravljanje rasvetom u kaficima</title></head>
    <body>
    <h2> Aplikacija za upravljanje rasvetom u kaficima</h2>
        <form method="POST" action="test">
            <h3> Promeni ugao osvetljenja pomocu potenciometra</h3>
            <p>  <input type="range" min="1" max="12.5" name="slider" /> </p>
            <input type="submit" value="Potvrdi" />
        </form>
    </body>
</html>

'''
@app.route("/")
def home():                                                                                                                                                         
    return render_template_string(TPL)                        
@app.route("/test", methods=["POST"])
def test():
    # Uzmi vrednost sa potenciometra
    slider = request.form["slider"]
    
    p.ChangeDutyCycle(float(slider))
    sleep(1)
    # Pauziraj servo
    p.ChangeDutyCycle(0)
    return render_template_string(TPL)
# Pokreni aplikaciju
if __name__ == "__main__":
    app.run()