from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

userLanguage = 'en'

@app.route('/', methods=['GET'])
def hello():
	print(request.accept_languages)
	if userLanguage == 'it':
		return render_template('it.html')
	elif userLanguage == 'de':
		return render_template('de.html')
	elif userLanguage == 'zh':
		return render_template('zh.html')
	else:
		return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
