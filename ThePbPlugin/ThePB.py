# ThePB.in PasteBin Plugin by Steve: steve]at[swiftirc[net]
# Version 1.0 ALPHA
# Copyright (C) 2014 Steve C

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# TODO: Add paste-selection vs whole file
import sublime, sublime_plugin
import json,urllib,urllib2
import conf, types

class ThepbCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		body = self.view.substr(sublime.Region(0,self.view.size()))

		# Attempt to get file type
		# This could probably be cleaned up.
		fType = self.getSyntax()
		parameters = [('apikey',conf.API_KEY),('mode',conf.PASTE_MODE),('paste',body),('lang',fType),('desc',conf.PASTE_DESC),('pass',conf.LOCK_PASS),('priv',conf.IS_PRIV)]
		parameters = urllib.urlencode(parameters)
		req = urllib2.Request(conf.PASTE_URL, parameters, headers = conf.URL_HEADERS)
		page = urllib2.urlopen(req)
		content = page.read()
		url = json.loads(content)['url']
		
		sublime.set_clipboard(url)
		sublime.status_message("Get your paste at: " + url)

	def getSyntax(self):
		fSyntax = self.view.settings().get('syntax').replace('.tmLanguage', '').replace(' ', '').rsplit('/',1)[-1]

		# If the file type is in the dictionary we can assign it, if not we'll just send it as text.
		try:
			fType = types.SYNTAX[fSyntax]
		except KeyError:
			fType = 'text'
		return fType




