from flask import Flask
from flask import render_template

app = Flask(__name__)

userLanguage = 'en'

@app.route('/', methods=['GET'])
def hello():
	if userLanguage == 'it':
		return render_template('index2_IT.html')
	elif userLanguage == 'de':
		return render_template('index2_DE.html')
	elif userLanguage == 'zh':
		return render_template('index2_zhHans.html')
	else:
		return render_template('index2.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
