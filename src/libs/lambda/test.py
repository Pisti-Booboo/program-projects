# mylib.py


import os
### variable d'environnement
env= os.environ.keys()
#print(os.environ["LANGUAGE"],os.environ["LC_ALL"],os.environ["LC_MESSAGES"],os.environ["LANG"])



import gettext
#print( gettext.bindtextdomain('domain',localedir=None) ) #should print '/usr/share/locale'
#print( gettext.find('domain', all=False) ) # print le pathname du fichier .mo qui sera utiliser
translator = gettext.translation('domainZ',fallback=True)
#print( translator.gettext("MSG1") )
#_ = translator.gettext
#print(_("MSG1"))




import logging
### create logger
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())#In addition to any handlers directly associated with a logger, all handlers associated with all ancestors of the logger are called to dispatch log messages.




OKIDOX='ok'

class Auxiliary:
	def __init__(self):
		#logger = logging.getLogger('appli.modul.Aux')
		logger.info('creating an instance of Auxiliary')

	def do_something(self):
		logger.info('Auxiliary doing something')
		a = 1 + 1
		logger.info('Auxiliary done doing something')
		print( "lib: "+translator.gettext("CDM1") )
		#print(_("CDM1"))



def log_test():
	logger.debug('debug log lib')
	logger.info('info log lib')
	logger.warning('warning log lib')
	logger.error('error log lib')
	logger.critical('critical log lib')
	print( "lib: "+translator.gettext("CFG1") )
	#print(_("CFG1"))
	"""
	print(_("MSG1"))
	print(_("OPT1"))
	print(_("ZZZ1"))
	"""
