from main import api, requests
def Function(msg, cmd):
	return requests.get('https://mipsum.herokuapp.com/frases/random').json()['frase']

plugin = {
	'patterns': [
		"^[/!](mipsum)$"
	],
	'function': Function,
	'name': "Mipsum",
	'admin': False,
	'usage': '<code>/mipsum</code>: Random text from mipsum',
	'sudo': False,
	}