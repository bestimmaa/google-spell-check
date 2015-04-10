# Replaces the word under the cursor or selection with Google Search's recommended spelling
# Hosted at http://github.com/noahcoad/google-spell-check

import sublime, sublime_plugin, urllib2, re, HTMLParser

PLUGIN_NAME = "google-spell-check"
SETTINGS_FILE = PLUGIN_NAME + ".sublime-settings"
SETTINGS_PREFIX = PLUGIN_NAME.lower() + '_'
settings = sublime.load_settings(SETTINGS_FILE)
google_local = "com"

if settings is not None:
	google_local = settings.get('google-local-version')

class GoogleSpellCheckCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if len(self.view.sel()) == 1 and self.view.sel()[0].a == self.view.sel()[0].b:
			self.view.run_command("expand_selection", {"to": "word"})

		for sel in self.view.sel():
			if sel.empty():
				continue

			fix = self.correct(self.view.substr(sel))
			edit = self.view.begin_edit()
			self.view.replace(edit, sel, fix)
			self.view.end_edit(edit)

	def correct(self, text):
		# grab html
		html = self.get_page('http://www.google.'+google_local+'/search?q=' + urllib2.quote(text))
		html_parser = HTMLParser.HTMLParser()

		# save html for debugging
		open('page.html', 'w').write(html)
		# pull pieces out
		#match = re.search(r'(?:Showing results for|Did you mean|Including results for)[^\0]*?<a.*?>(.*?)</a>', html)
		match = re.match("(.*?)<a class=\"spell\" href=\"(.*)\"><b><i>(.*)</i></b></a>(.*?)",html,re.S)
		#match = re.match("(.*) class(.*)",html,re.S)
		if match is None:
			print("google-spell-check: no correction found for "+text)
			fix = text
		else:
			print("google-spell-check: found correction!")
			fix = (match.group(3))

		# return result
		return fix

	def get_page(self, url):
		# the type of header affects the type of response google returns
		# for example, using the commented out header below google does not 
		# include "Including results for" results and gives back a different set of results
		# than using the updated user_agent yanked from chrome's headers
		# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
		headers = {'User-Agent':user_agent,}
		req = urllib2.Request(url, None, headers)
		page = urllib2.urlopen(req)
		html = str(page.read())
		page.close()
		return html

# p.s. Yes, I'm using hard tabs for indentation.  bite me
# set tabs to whatever level of indentation you like in your editor 
# for crying out loud, at least they're consistent here, and use 
# the ST2 command "Indentation: Convert to Spaces", which will convert
# to spaces if you really need to be part of the 'soft tabs only' crowd =)