# Google Spell Check
(a Sublime Text 2 Plugin Package)

## Description
Replaces the selected text with Google's spelling correction.  Use Google magic to fix spelling.  Google has a far better spell checker than most tools.  This does _not_ replace the built-in spell checker, offer suggestions, or adds words to the built-in dictionary.  Instead it replaces the selected text with a Google search page result's magically usually right recommended spelling (or does nothing if Google thinks you've got it right).

There are several problems with most typical spell checkers:

1. **Lack of Context**, most only check the word itself, not taking into consideration the context you're using the word or phrase in, gatsby quotes
1. **Lack of Frequency**, most use grammatical syntax 'sounds like' lookup tables, but don't know how frequent a misspelling is, google sees mispellings all the time so they have a much better idea of what you 
1. **No Help w Names**, company names like flikr tumblr or say I'm talking about scifi author jon scalzi most would say Jon and no idea on scalzi because they look one word at a time, google search considers the whole phrase and popular names together to correct to john sculzi
1. **Limited Dictionary**, most use somewhat limited dictionaries, whereas google has the world of words available to it:  
1. **Just Suck**, like Sublime's spell checker has no idea what do to with avalible, scifi

BTW, this uses a standard Google search page results instead of the Google API.  This is nice in that an API key isn't required, but isn't 100% officially supported, so Google changing their URL schema could break the plugin.

## Installation
any of these...
* Get through the awesome Sublime [Package Control](http://wbond.net/sublime_packages/package_control) as Google Spell Check
* Git clone into your sublime packages folder  
```git clone https://github.com/noahcoad/google-spell-check.git```
* (Download)[https://github.com/noahcoad/google-spell-check/archive/master.zip] and unpack into your sublime packages folder

## How to Use
1. Select some text in the editor
1. Run the google_spell_correct command
  1. via ctrl+shift+p (command+shift+p in OSX) > Google Spell Check
  1. via right-click context menu > Google Spell Check
  1. via hotkey, default is ctrl+alt+g
1. be patient, may take a second for google to return a result  
if nothing changes, google probably thinks your spelling is okay, or has no idea what you're talking about