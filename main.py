from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import time
import uuid
import random
# from google.cloud import firestore

app = Flask(__name__)

userLanguage = 'en'
ts = time.time()
	
# db = firestore.Client()

@app.route('/', methods=['GET'])
def hello():
# 	doNotTrack = request.headers.get('DNT')
# 	
# 	if doNotTrack != '1':
# 		language = request.headers.get('Accept-Language')
# 		user = request.headers.get('User-Agent')
# 		referer = request.headers.get('Referer')
# 		with open('log.txt', 'a') as fo:
# 			fo.write('TS:'+str(ts)+'  AL:'+str(language)+'  UA:'+str(user)+'  R:'+str(referer)+' \n')
# 	else:
# 		print('user has asked not to be tracked')
		
	if userLanguage == 'it':
		return render_template('it.html')
	elif userLanguage == 'de':
		return render_template('de.html')
	elif userLanguage == 'zh':
		return render_template('zh.html')
	else:
		return render_template('index.html')
		
@app.route('/it', methods=['GET'])
def italiana():
	userLanguage = 'it'
	return render_template('it.html') 
	
@app.route('/de', methods=['GET'])
def deutsch():
	userLanguage = 'de'
	return render_template('de.html')
	
@app.route('/zh', methods=['GET'])
def chinese():
	userLanguage = 'zh'
	return render_template('zh.html')
	
@app.route('/zandypokal', methods=['GET'])
def zanpok():
	return redirect('https://www.icloud.com/numbers/0f8PvUMhsQlLPV7_93CgqO7Fw#Zandy_Pokal')
	
@app.route('/partenope', methods=['GET'])
def partenope():
# 	TODO: fix form
	return render_template('partenope.html')
	
@app.route('/astros', methods=['GET'])
def astros():
	return render_template('astros.html')

@app.route('/sscnapoli', methods=['GET'])
def sscnapoli():
	return render_template('sscnapoli.html')

@app.route('/ratings', methods=['GET'])
def ratings():
	# TODO: fix
	return 'Under Construction'

@app.route('/projects', methods=['GET'])
def projects():
	return """Fish Camp - Released <br>
			GG - Beta <br>
			Palette - Beta <br>
			Animal Countdown - Released <br>
			People in Action - Beta <br>
			Stocks - Alpha <br>
			Ratings - NiD<br>
			Water Club - Released<br>
			Music Story - NiD <br>"""
	
# 	return render_template('projects.html')
	
@app.route('/translationhelp', methods=['GET', 'POST'])
def tHelp():
	if request.method == 'GET':
		return render_template('translationhelp.html')
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		project = request.form.get('project')
		lang = request.form.get('lang')
		original = request.form.get('original')
		correct = request.form.get('correct')
		com = request.form.get('com')
		
# 		doc_ref = db.collection(u'translations').document(str(uuid.uuid4()))
# 		doc_ref.set({
#     		u'name': name,
#     		u'email': email,
#     		u'project': project,
#     		u'land': lang,
#     		u'original': original,
#     		u'correct': correct,
#     		u'com': com,
# 		})
		
# 		return 'Submitted. Thank you. Danke. Grazie.'
		return 'Coming Soon'
		
@app.route('/randomcity', methods=['GET'])
def randomCity():
	lat = random.uniform(-85.0, 85.0)
	lon = random.uniform(-180.0, 180.0)
	return '<a href="http://maps.apple.com/?ll= '+str(lat)+','+str(lon)+'&q=Pin">Open in Apple Maps</a>'
# 	return str(lat) + ' ' + str(lon)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
