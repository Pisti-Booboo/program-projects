#!/usr/bin/env python3
#coding: utf-8
### la 1er ligne permet d'executer ce script en tapen seulment son nom dans un terminal UNIX, avec ca plus besoin de le faire précéder par la commande python
### la 2eme ligne autorise les charactere unicode avec accent et autre specificité de language dans le code source

from __future__ import division# pour avoir un nombre a virgul qan la division ne tombe pas just
from __future__ import print_function#
from __future__ import unicode_literals# utilise unicode au lieu de ASCII pour les chaine de charactere

__doc__ = "information decrivant l'usage & la fonction de ce modul/prog,changelog: modification faite par rapport a la version precedente"
__author__ = "N-zo syslog@laposte.net"#aka the creator, the boss, the one who decide
__credits__ = ["Rob xxx", "Peter xxx", "Gavin xxxx",	"Matthew xxxx"]#people who reported bug fixes, made suggestions, etc. but did not actually write the code.
__date__ = "2016-02-25"#started date / creation date
__version__ = "x.x.x"# auto modif par Vrzion
#__maintainer__ = "Nzo"#person who fixed bugs and made improvements, who replace the author
#__contact__ = "syslog@laposte.net"#mailing list du projet, forum ou email de l'auteur ou du mainteneur
#__license__ = "X"#do what you can do with it, je ne crois pas au system de license
#__status__ = "Release"#should typically be one of 'Prototype', 'Development', or 'Production' 'Deprecated' 'Release'.


### LOGS , presque toujours utile
from libs import debugger

### TRADUCTION multilingual , internationalization,localization
#import locale # permet de representer un nombre ou un text dans le langage de l'utilisateur. par exemple un float sera ecrit avec un point si l'utilisateur est anglo ou avec une virgule si il est franco et le format des dates sera fonction du langage de l'utilisateur ,etc...
###initially, when a program is started, the locale is the C locale, no matter what the user’s preferred locale is. The program must explicitly say that it wants the user’s preferred locale settings by calling setlocale(LC_ALL, '').
#import intl
#intl.setlocale(intl.LC_ALL,"")
import gettext # provides internationalization (I18N) and localization (L10N), (permet d'acceder aux traductions po/mo)
#print( gettext.bindtextdomain('domain',localedir=None) ) #should print '/usr/share/locale'
#print( gettext.find('domain', all=False) ) # print le pathname du fichier .mo qui sera utiliser
#print( gettext.bind_textdomain_codeset('domain',codeset=None) ) #If codeset is omitted, then the current binding is returned.
#print( gettext.find(domain, localedir=None, languages=None, all=False) )# cherche les fichier mo pouvant etre utiliser(This function implements the standard .mo file search algorithm.)
translator = gettext.translation('domainX',fallback=True)# if no .mo file is found, this function raises OSError if fallback is false (which is the default), and returns a NullTranslations instance if fallback is true.
# translators: insert notes for poedit users
#print( translator.gettext("STARTER_MSG1") )
#print( translator.ngettext("STARTER_MSG2singular","STARTER_MSG2plural",qantum) )
### jai la preference de specifier clairement le "domain de traduction" pour chaque fichier/module python et l'utilisation mixer du racourci _ et de ngettext me derange
#_ = translator.gettext
#print(_("STARTER_MSG3"))



###
### Modules specifiq importer pour ce program
###

### OpenGL
#from OpenGL.GL import *
#from OpenGL.GLUT import *
#from OpenGL.GLU import *
#rom OpenGL.GLE import *
#from OpenGL.GL.ARB.multitexture import *

#import colorsys		#Conversion functions between RGB and other color systems.
#import random
#import hashlib	# Secure hash and message digest algorithms.
#import string #manipulation des chaine de caractere
#import struct # Interpret strings as packed binary data, par exemple pour convertir un nombre ecrit sur 16bits en une chaine de caractere de plusieur octect et inversement
#import binascii # Convertir du binaire en ASCII et vice versa

### Math
#import operator #For example, operator.add(x, y) is equivalent to the expression x+y.
#import math #pour faire des truc de math
#from Numeric import*
#import numpy
#import statistics	#mathematical statistics functions
#from fractions import Fraction # int(Fraction(3, 2) + Fraction(1, 2)) = 2
#from decimal import Decimal # parceque: 0.1 + 0.1 + 0.1 - 0.3 = 5.551115123125783e-17

#import threading # constructs higher-level threading interfaces
#import queue  #when information must be exchanged safely between multiple threads.

#import selectors

#import re #Regular expression operations
#import fnmatch # support for Unix shell-style wildcards, which are not the same as regular expressions
#import collections	# provide alternatives specialized datatypes (dict, list, set, and tupl) ex: deque>list-like container with fast appends and pops on either end
#from collections import deque # storage de queue de données
#import reprlib  		#  provides python object representations by limited strings size.
#import traceback		#exactly mimics the behavior of the Python interpreter when it prints a stack trace.

#import signal #defining custom handlers to be executed when a signal is received.
#import os #pour faire un peu de tout se que le system d'exploitation peut faire
#import sys
#sys.maxint # la limite de transformation d'un int en long
#import platform
#import sysconfig #provides access to Python’s configuration information like the list of installation paths and the configuration variables relevant for the current platform.#python3
#os.environ.keys()
#print(sys.platform)
#print(os.uname())
#print(os.getcwd())
#print(os.times())
#print(os.cpu_count()) #python3
#print(os.curdir)
#print(os.pardir)
#print(os.sep)
#print(os.extsep)
#print(os.linesep)
#print(os.devnull)
#print(os.urandom(10))
#print(sys.getsizeof(object[, default]

### les modules suivant permettent de connaitre la conso et fonctionnement d'un prog python,
### ce genre de tache est utile au moment de la conception, et devraient normalment etre des options d'un bon IDE, permettant aussi d'afficher le resultat en collonne triable, ou en grapgiques de statistic
#import cProfile,profile # cProfile and profile provide profiling of Python programs. A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
#import trace # repertori les modules importer et les fonction du prog
#import tracemalloc #python3
#import resource # This module provides basic mechanisms for measuring and controlling system resources utilized by a program.

### open read and write files
### ces moduls devraient etre integrer dans le "corps" du programe, non pas dans son starter
### car le programe decide quel mode utiliser pour l'ouverture ou ecriture ,ou la taille du tampon memoire, la prioriter d'acces , etc...
#import dbm #Interfaces to various Unix "database" formats.
#from xml.dom import minidom #XML
#import csv #CSV/TSV File Reading and Writing
#import yaml # YAML parser and emitter for Python, PyYAML.org
#import xml.parsers.expat  #Fast XML parsing using Expat
#import shelve # data persistence, permet d'enregistrer dans un fichier des datas python pour une reutilisation ulterieur
#import sqlite3	#A DB-API 2.0 implementation using SQLite 3.x.
#import mimetypes	#Mapping of filename extensions to MIME types.
#import shutil #High-level file operations, including copying.
#import tempfile #pour la creation et manipulation de ficher et dossier temporaire
#import tarfile  # manipulation d'archive tar
#import pathlib # manipulation,modification,convertion(Posix:Windows) et check des pathnames en tout genre #python3
#import fileinput # alternative a open() utile pour ouvrir plusieurs fichiers en une fois ou utiliser un pipe shell |
#print(fileinput.input('-'))#blok si rien est fourni par le pipe
#import pipes
#print( sys.__stdin__.read() ),print( sys.stdin.read() ) #blok si rien est fourni par le pipe
#import glob # finds all the pathnames matching a specified pattern according to the rules used by the Unix shell # le shell s'occupe deja de convertir les  paterns avant den donner le resultat au program
#import os.path #pour la manipulation des fichier repertoire et de leur chemin d'acces

### ces moduls permetant d'ouvrir ne connection devraient etre integrer dans le "corps" du programe, non pas dans son starter
### car le programe decide quel mode utiliser pour l'ouverture et l'envoie des donnés ,et la taille du tampon memoire,  etc...
#import urllib # permet douvrir une URL de la meme facon qu'on ouvre un fichier local
#import ipaddress# convert check ip adress #python3
#import socket #Low-level networking interface.
#import asyncore #provides the basic infrastructure for writing asynchronous socket service clients and servers.
#import socketserver # simplifies the task of writing network servers.

### temps et dates
#from time import clock
#import time	#Time access and conversions.
#import datetime	#Basic date and time types.
#import calendar	#Functions for working with calendars, including some emulation of the Unix cal program.
#import dateutils #un datetime boosté aux hormones qui permet notamment de donnée des durées floues comme “+ 1 mois” et gérer des événements qui se répètent. Il est dans tous mes projets par défaut.
#import babel #n’est pas spécialisé dans les dates mais dans la localisation. Le module possède des outils pour formater des dates selon le format de chaque pays, et aussi avec des formats naturels comme “il y a une minute”.
#import pytz #implémentation saine de gestion des fuseaux horaires en Python. On y reviendra.



### le meme message de log peut etre utiliser a plusieur endroit avec des variables differente dans le module
LOG_MSG1="starting"
LOG_MSG2="this program was designed for Linux operating system. {} detected"
LOG_MSG3="loading"
LOG_MSG4="endding"
LOG_MSG5='stp1'
LOG_MSG6='stp2'
LOG_MSG7='stp3'
LOG_MSG8='stp4'
LOG_MSG9='fonction principal du program'
LOG_MSG10='qantum : {}'
LOG_MSG11='arg : {}'

TEMPLATE_CONSTANTE=1#template_comment



def template_fonction():
	"""information decrivant l'usage de cette fonction"""
	return True



class Template_Class_Parent :
	"""information decrivant l'usage de cette class"""
	def __init__(self,template_argument_parent=True):
		"""information decrivant l'usage de cette metode"""
		self.template_attribut_parent=template_argument_parent

		#template_comment

	def template_methode_parent(self,qantum):
		"""information decrivant l'usage de cette metode"""
		while qantum :
			print("quantum="+qantum)
			quantum-=1
		debugger.log_info( LOG_MSG10.format(qantum) )


class Template_Class_Enfant(Template_Class_Parent) :
	"""information decrivant l'usage de cette class"""
	def __init__(self,template_argument_enfant,template_argument_parent):
		"""information decrivant l'usage de cette metode"""
		Template_Class_Parent.__init__(self,template_argument_parent)

		debugger.log_info( LOG_MSG10.format(template_argument_enfant) )
		self.template_attribut_enfant=template_argument_enfant*"w"
		#template_comment
		self.valu_list=range(len(self.template_attribut_enfant))

	def template_methode_enfant(self,qantum):
		"""information decrivant l'usage de cette metode"""
		for index in xrange(qantum) :
			#template_comment
			debugger.log_info(LOG_MSG10.format(index) )
			valu=self.valu_list[index]
			if valu==0 :
				print("valu egale a zero")
			elif vaku>=-6 :
				print("valu plus grans que -6")
			elif vaku!=1 :
				print("valu different de 1")
			else :
				pass


def start(progname,config,env):
	debugger.log_debug(LOG_MSG9)
	ui=Template_Class_Enfant(template_argument_enfant=12,template_argument_parent=1)
	#input("Press Enter to continue")
	from moduls.libs import mylib#
	debugger.log_info(LOG_MSG5)#
	mylib.log_test()#
	debugger.log_info(LOG_MSG6)#
	a = mylib.Auxiliary()#
	debugger.log_info(LOG_MSG7)#
	a.do_something()#
	debugger.log_info(LOG_MSG8)#
	#handler.emit("record")
	#print( "My name is {0[name]}".format(dict(name='Fred')) ) # My name is Fred
	#print( format(10.0, "7.3g") )
	#print( format(dict(name='Fred'),"My name is {0[name]}") )
	qantum=3
	print( translator.ngettext("STARTER_MSG4singular","STARTER_MSG4plural",qantum) )
	print( translator.gettext("STARTER_MSG5") )
	#print(_("STARTER_MSG6))
	x=input("Press Enter to continue")
	#import time
	#time.sleep(600)
	#open("logs.txt",mode='a')
	#wait(1000)

