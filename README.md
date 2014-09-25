# Devhelp for Sublime Text 2/3

Devhelp package for Sublime Text using [Devhelp](http://devhelpdocs.org/) documentation browser which is similar with [Dash](http://kapeli.com/dash/).

*Tested in Windows/Linux.*  

##Screen-shots

Multiple results for PHP mapping.

![Multiple results for PHP mapping](http://www.vaanwebdesign.ro/includes/images/devhelp_1.png)
<br/>
<br/>
Custom search in Devhelp docsets.

![Custom search in Devhelp docsets](http://www.vaanwebdesign.ro/includes/images/devhelp_2.png)

## Installation

Easiest way to install the plugin is to use [Package Control](http://wbond.net/sublime_packages/package_control).

Alternatively you can clone with git directly into `Packages` directory in the Sublime Text 2 application settings area. The directory name must be `Devhelp`.

### Using Git

Go to your Sublime Text 2 `Packages` directory and clone the repository using the command below:

    git clone https://github.com/vaanwd/Devhelp "Devhelp"

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `Devhelp`
* Copy the folder to your Sublime Text 2 `Packages` directory

## Usage

`F1` - Open Devhelp documentation for current/selected word.

`Shift` + `F1` - Open Devhelp search bar.

## Mapping example
To mapping other language for Devhelp docset you need to edit `User\Devhelp.sublime-settings`:

	{
	  /**
	   *  Devhelp executable path.
	   *  For Linux: /usr/bin/devhelp
	   *  For Windows: c:\\Program Files\\Devhelp\\devhelp.exe
	   */
	  "devhelp_command": "/usr/bin/devhelp",

	  /**
	   * Language mapping examples.
	   */
	  "language_mapping": {
	    "HTML": {"lang": "html", "devhelp_lang": "html"},
	    "JavaScript": {"lang": "javascript", "devhelp_lang": "javascript"},
	    "CSS": {"lang": "css", "devhelp_lang": "css"},
	    "CSS MSN": {"lang": "css", "devhelp_lang": "msdn"},
	    "PHP": {"lang": "php", "devhelp_lang": "php"},
	    "Drupal": {"lang": "php", "devhelp_lang": "drupal"},
	    "Python": {"lang": "python", "devhelp_lang" : "python"},
	    "Django": {"lang": "python", "devhelp_lang" : "django"}
	  }
	}


[&copy; 2014 Vaan Web Design](http://www.vaanwebdesign.ro)

