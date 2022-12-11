import argparse
import requests
from bs4 import BeautifulSoup

# Use the argparse library to parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("page_url", help="URL of the web page")
parser.add_argument("--id", help="ID of the HTML element containing the main content of the page")
parser.add_argument("--classname", help="class of the HTML element containing the main content of the page")
args = parser.parse_args()

# Use the requests library to fetch the contents of the web page
page_url = args.page_url
page_content = requests.get(page_url)

# Use the BeautifulSoup library to parse the page content
soup = BeautifulSoup(page_content.text, 'html.parser')

# Extract the text from the page using the specified id or class name (if provided),
# or extract the text from the entire page if no id or class name is specified
page_text = ""
if (args.id is not None) or (args.classname is not None):
    element = soup.find(id=args.id, class_=args.classname)
    if element is not None:
        page_text = element.get_text()
else:
    page_text = soup.get_text()
print(page_text)

# Use a text-to-speech library to read the text out loud
from gtts import gTTS
tts = gTTS(text=page_text, lang='en')
tts.save("page_contents.mp3")

# Play the audio file using the pygame library
import pygame
pygame.init()
pygame.mixer.music.load("page_contents.mp3")
pygame.mixer.music.play()

# Keep the script running until the audio has finished playing
while pygame.mixer.music.get_busy():
    continue
