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

# Configuration Values for ThePB.in Plugin
# Edit the values below to suit your needs

# API Key
# Note: You -MUST- obtain an API key and edit this value first.
# You can get yours at http://thepb.in/p/auth
API_KEY = 'change-me'

###################################################
# Optional Settings
# These settings control how your paste is handled.
###################################################
# Lock Pass
# Edit this to lock your pastes with a password
# This is sent as PLAINTEXT
LOCK_PASS = ''

# Private or Public
# Set this value to 1 and your pastes will be submitted
# privately.

IS_PRIV = '0'

# Description
# Edit this if you would like to change the description
PASTE_DESC = 'ThePB PasteBin Plugin http://thepb.in/tools/'

# TODO: Add support for private/public pastes

###################################################
# Other Settings
# Editing these could cause weird things to happen!
###################################################
PASTE_MODE = 'paste'
PASTE_URL = 'http://thepb.in/api/'

# Headers to Send
# TODO: Shrink this down a ton!
URL_HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded'}





