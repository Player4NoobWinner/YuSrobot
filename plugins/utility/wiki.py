from main import api, wikipedia
def Function(msg, cmd):
	wikipedia.set_lang("add your language ex: en")
	summary = '{} <a href="{}">more</a>'
	try:
		resp = summary.format(wikipedia.summary(cmd[1], sentences=3), wikipedia.page(cmd[1]).url)
	except Exception as error:
		resp = 'Not Found'
	return resp

plugin = {
	'patterns': [
		"^[/!](wiki) (.+)$"
	],
	'function': Function,
	'name': "Wiki",
	'usage': '<code>/wiki [term]</code>: Searches wiki and send results from wikipedia',
	'sudo': False,
	}