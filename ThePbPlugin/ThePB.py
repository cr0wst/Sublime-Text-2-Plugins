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
class ThepbCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings('ThePB.sublime-settings')
		body = self.view.substr(sublime.Region(0,self.view.size()))

		# Attempt to get file type
		# This could probably be cleaned up.
		fType = self.getSyntax()
		parameters = [('apikey',settings.get('API_KEY')),('mode',settings.get('PASTE_MODE')),('paste',body),('lang',fType),('desc',settings.get('PASTE_DESC')),('pass',settings.get('LOCK_PASS')),('priv',settings.get('IS_PRIV'))]
		parameters = urllib.urlencode(parameters)
		URL_HEADERS = {'User-Agent': 'Sublime Text/2.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded'}
		req = urllib2.Request(settings.get('PASTE_URL'), parameters, headers = URL_HEADERS)
		page = urllib2.urlopen(req)
		content = page.read()
		try:
			url = json.loads(content)['url']
			sublime.set_clipboard(url)
			sublime.status_message("Get your paste at: " + url)
		except KeyError:
			sublime.status_message("An error has occured: %s " % json.loads(content)['error'])

	def getSyntax(self):
		fSyntax = self.view.settings().get('syntax').replace('.tmLanguage', '').replace(' ', '').rsplit('/',1)[-1]
		# Type dictionary
		types = '{"4cs":"GADV 4CS","6502acme":"MOS 6502 (6510) ACME Cross Assembler format","6502kickass":"MOS 6502 (6510) Kick Assembler format","6502tasm":"MOS 6502 (6510) TASM\/64TASS 1.46 Assembler format","68000devpac":"Motorola 68000 - HiSoft Devpac ST 2 Assembler format","abap":"ABAP","actionscript":"ActionScript","actionscript3":"ActionScript 3","ada":"Ada","algol68":"ALGOL 68","apache":"Apache configuration","applescript":"AppleScript","apt_sources":"Apt sources","arm":"ARM ASSEMBLER","asm":"ASM","asp":"ASP","asymptote":"asymptote","autoconf":"Autoconf","autohotkey":"Autohotkey","autoit":"AutoIt","avisynth":"AviSynth","awk":"awk","bascomavr":"BASCOM AVR","bash":"Bash","basic4gl":"Basic4GL","bf":"Brainfuck","bibtex":"BibTeX","blitzbasic":"BlitzBasic","bnf":"bnf","boo":"Boo","c":"C","c_loadrunner":"C (LoadRunner)","c_mac":"C (Mac)","caddcl":"CAD DCL","cadlisp":"CAD Lisp","cfdg":"CFDG","cfm":"ColdFusion","chaiscript":"ChaiScript","cil":"CIL","clojure":"Clojure","cmake":"CMake","cobol":"COBOL","coffeescript":"CoffeeScript","cpp":"C++","cpp-qt":"C++ (Qt)","csharp":"C#","css":"CSS","cuesheet":"Cuesheet","d":"D","dcl":"DCL","dcpu16":"DCPU-16 Assembly","dcs":"DCS","delphi":"Delphi","diff":"Diff","div":"DIV","dos":"DOS","dot":"dot","e":"E","ecmascript":"ECMAScript","eiffel":"Eiffel","email":"eMail (mbox)","epc":"EPC","erlang":"Erlang","euphoria":"Euphoria","f1":"Formula One","falcon":"Falcon","fo":"FO (abas-ERP)","fortran":"Fortran","freebasic":"FreeBasic","freeswitch":"FreeSWITCH","fsharp":"F#","gambas":"GAMBAS","gdb":"GDB","genero":"genero","genie":"Genie","gettext":"GNU Gettext","glsl":"glSlang","gml":"GML","gnuplot":"Gnuplot","go":"Go","groovy":"Groovy","gwbasic":"GwBasic","haskell":"Haskell","haxe":"Haxe","hicest":"HicEst","hq9plus":"HQ9+","html4strict":"HTML","html5":"HTML5","icon":"Icon","idl":"Uno Idl","ini":"INI","inno":"Inno","intercal":"INTERCAL","io":"Io","j":"J","java":"Java","java5":"Java(TM) 2 Platform Standard Edition 5.0","javascript":"JavaScript","jquery":"jQuery","kixtart":"KiXtart","klonec":"KLone C","klonecpp":"KLone C++","latex":"LaTeX","lb":"Liberty BASIC","ldif":"LDIF","lisp":"Lisp","llvm":"LLVM Intermediate Representation","locobasic":"Locomotive Basic","logtalk":"Logtalk","lolcode":"LOLcode","lotusformulas":"Lotus Notes @Formulas","lotusscript":"LotusScript","lscript":"LScript","lsl2":"LSL2","lua":"Lua","m68k":"Motorola 68000 Assembler","magiksf":"MagikSF","make":"GNU make","mapbasic":"MapBasic","matlab":"Matlab M","mirc":"mIRC Scripting","mmix":"MMIX","modula2":"Modula-2","modula3":"Modula-3","mpasm":"Microchip Assembler","mxml":"MXML","mysql":"MySQL","nagios":"Nagios","netrexx":"NetRexx","newlisp":"newlisp","nsis":"NSIS","oberon2":"Oberon-2","objc":"Objective-C","objeck":"Objeck Programming Language","ocaml":"OCaml","ocaml-brief":"OCaml (brief)","octave":"GNU Octave","oobas":"OpenOffice.org Basic","oorexx":"ooRexx","oracle11":"Oracle 11 SQL","oracle8":"Oracle 8 SQL","oxygene":"Oxygene (Delphi Prism)","oz":"OZ","parigp":"PARI\/GP","pascal":"Pascal","pcre":"PCRE","per":"per","perl":"Perl","perl6":"Perl 6","pf":"OpenBSD Packet Filter","php":"PHP","php-brief":"PHP (brief)","pic16":"PIC16","pike":"Pike","pixelbender":"Pixel Bender 1.0","pli":"PL\/I","plsql":"PL\/SQL","postgresql":"PostgreSQL","povray":"POVRAY","powerbuilder":"PowerBuilder","powershell":"PowerShell","proftpd":"ProFTPd configuration","progress":"Progress","prolog":"Prolog","properties":"PROPERTIES","providex":"ProvideX","purebasic":"PureBasic","pycon":"Python (console mode)","pys60":"Python for S60","python":"Python","q":"q\/kdb+","qbasic":"QBasic\/QuickBASIC","rails":"Rails","rebol":"REBOL","reg":"Microsoft Registry","rexx":"rexx","robots":"robots.txt","rpmspec":"RPM Specification File","rsplus":"R \/ S+","ruby":"Ruby","sas":"SAS","scala":"Scala","scheme":"Scheme","scilab":"SciLab","sdlbasic":"sdlBasic","smalltalk":"Smalltalk","smarty":"Smarty","spark":"SPARK","sparql":"SPARQL","sql":"SQL","stonescript":"StoneScript","systemverilog":"SystemVerilog","tcl":"TCL","teraterm":"Tera Term Macro","text":"Text","thinbasic":"thinBasic","tsql":"T-SQL","typoscript":"TypoScript","unicon":"Unicon (Unified Extended Dialect of Icon)","upc":"UPC","urbi":"Urbi","uscript":"Unreal Script","vala":"Vala","vb":"Visual Basic","vbnet":"vb.net","vedit":"Vedit macro language","verilog":"Verilog","vhdl":"VHDL","vim":"Vim Script","visualfoxpro":"Visual Fox Pro","visualprolog":"Visual Prolog","whitespace":"Whitespace","whois":"Whois (RPSL format)","winbatch":"Winbatch","xbasic":"XBasic","xml":"XML","xorg_conf":"Xorg configuration","xpp":"X++","yaml":"YAML","z80":"ZiLOG Z80 Assembler","zxbasic":"ZXBasic"}'
		j = json.loads(types)
		# Dictionary is backwards, it's much more useful to us like this!
		SYNTAX = dict (zip(j.values(),j.keys())) 
		# If the file type is in the dictionary we can assign it, if not we'll just send it as text.
		try:
			fType = SYNTAX[fSyntax]
		except KeyError:
			fType = 'text'
		return fType




