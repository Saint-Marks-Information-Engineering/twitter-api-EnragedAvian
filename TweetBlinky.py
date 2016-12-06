import time
import RPi.GPIO as GPIO
from twython import twythonStreamer


TERMS = '#yes'

LED = 22

API_KEY = 'yjOiVYznjU7tEYQznLaUlJV21'
APP_SECRET = 'KKvwoJSCeq4SXYdxuj2RiDHvw5Owk0SWJlvieprz2D62FKyEUK'
OAUTH_TOKEN = '805877579580375040-EDyLVC9p0v0N0TFFyIh9RCsF241LIQV'
OAUTH_TOKEN_SECRET = '0chQEc2xDael6WnC1FAN2LxgGGUXeHHTuBORI0XYVy4pM'

class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        GPIO.output(LED, GPIO.HIGH)
                        time.sleep(0.5)
                        GPIO.output(LED, GPIO.LOW)

# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()
