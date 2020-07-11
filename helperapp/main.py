import speech_recognition as sr
import random
import datetime
import shutil
from googletrans import Translator
from .extract_key import extract
from fuzzywuzzy import process
from .text_to_speech import say

translator = Translator()
    
def listen_input():
	r = sr.Recognizer()
	r.energy_threshold = 500
	# r.pause_threshold = t
	mic = sr.Microphone()
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	text = r.recognize_google(audio, language='hi-IN')
	result = translator.translate(text)
	text = result.text
	return text

def get_match_score(query_keywords, keyword_list):
	score = 0
	for keyword in query_keywords:
		result = process.extractOne(keyword, keyword_list)
		if result[1] > 70:
			score = 1
	return score

def execute():
	keywords_dict = {"Health":["insurance", "health", "hospital", "medical" , "medicine"], "Education":["school", "empowerment" , "college", "girl", "boy", "education"], "Farming":["job", "insurance", "money", "farmer", "employment", "crop", "grain", "wheat", "rice", "agriculture"]}
	say("aap kya jaanana chaahate ho")
	query = listen_input()
	say("aapke liye uttar dhoondhaa ja raha hai")
	print(query)
	query_keywords = extract(query)
	score = 0
	category = ""
	health_score = get_match_score(query_keywords, keywords_dict["Health"])
	score = health_score
	category = "Health"
	farming_score = get_match_score(query_keywords, keywords_dict["Farming"])
	if farming_score > score:
		score = farming_score
		category = "Farming"
	edu_score = get_match_score(query_keywords, keywords_dict["Education"])
	if edu_score > score:
		score = edu_score
		category = "Education"
	schemes = find_right_info(category)
	return schemes

def find_right_info(category):
	filename = 'E:/Projects/setu/setu/helperapp/'+category+'.txt'
	fobj = open(filename)
	schemes = fobj.readlines()
	fobj.close()
	return schemes

