from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import time

app = Flask(__name__)

userLanguage = 'en'
ts = time.time()

@app.route('/', methods=['GET'])
def hello():
	doNotTrack = request.headers.get('DNT')
	
	if doNotTrack != '1':
		language = request.headers.get('Accept-Language')
		user = request.headers.get('User-Agent')
		referer = request.headers.get('Referer')
		with open('log.txt', 'a') as fo:
			fo.write('TS:'+str(ts)+'  AL:'+str(language)+'  UA:'+str(user)+'  R:'+str(referer)+' \n')
	else:
		print('user has asked not to be tracked')
		
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

@app.route('/stocks', methods=['GET'])
def stocks():
	return render_template('stocks.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
