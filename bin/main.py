import os
import sys
import errno
import json

class application_module_config:
	config_ini = None
	config_file = 'config.ini'

	def __init__(self, file=''):
		import configparser
		self.config_ini = configparser.ConfigParser()
		self.config_ini.sections()
		if os.path.isfile(file):
			print('Config file: {0}'.format(file))

	def load(self):
		return None
		if os.path.isfile(self.config_file):
			config = self.config_ini.read(self.config_file, encoding='utf-8')
			self.config_ini.sections()
			return config
		else:
			raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.config_file)

	def default(self):
		config = {}
		config['global'] = {}
		config['global']['length-begin'] = 1
		config['global']['length-until'] = 6
		config['global']['character-lower'] = True
		config['global']['character-upper'] = True
		config['global']['character-number'] = True
		config['global']['character-special'] = True
		return config

class application_module_chars:
	def __init__(self):
		pass

	def chrs_number(self):
		l = list(range(48,57+1))
		for i,n in enumerate(l):
			l[i] = chr(l[i])
		return l

	def chrs_lower(self):
		l = list(range(97,122+1))
		for i,n in enumerate(l):
			l[i] = chr(l[i])
		return l

	def chrs_upper(self):
		l = list(range(65,90+1))
		for i,n in enumerate(l):
			l[i] = chr(l[i])
		return l

	def chrs_spechar(self):
		l = list(range(33,47+1))
		l += list(range(58,64+1))
		l += list(range(91,96+1))
		l += list(range(123,126+1))
		for i,n in enumerate(l):
			l[i] = chr(l[i])
		return l

if __name__ == '__main__':
	argv = ''
	if len(sys.argv)>1:
		argv = sys.argv
		del argv[0]
		argv = ' '.join(argv).strip()
		print('Command Line Args: {0}'.format(argv))

	if '--help' in argv or len(argv)==0:
		print('Usage: ')
		print('{0} {1}'.format(' '*2,'--help'))
		print('{0} {1}'.format(' '*10,'Print the help.'))
		print('{0} {1}'.format(' '*2,'--no-config'))
		print('{0} {1}'.format(' '*10,'No Load the Config, Use the Default Setting.'))
		print('{0} {1}'.format(' '*2,'--character-number=on|off'))
		print('{0} {1}'.format(' '*10,'Override Setting, Use or Unuse'))
		print('{0} {1}'.format(' '*2,'--character-lower=on|off'))
		print('{0} {1}'.format(' '*10,'Override Setting, Use or Unuse'))
		print('{0} {1}'.format(' '*2,'--character-upper=on|off'))
		print('{0} {1}'.format(' '*10,'Override Setting, Use or Unuse'))
		print('{0} {1}'.format(' '*2,'--character-special=on|off'))
		print('{0} {1}'.format(' '*10,'Override Setting, Use or Unuse'))
		print('{0} {1}'.format(' '*2,'--length-begin=n'))
		print('{0} {1}'.format(' '*10,'Override Setting,'))
		print('{0} {1}'.format(' '*2,'--length-until=n'))
		print('{0} {1}'.format(' '*10,'Override Setting,'))
		sys.exit()

	config = application_module_config(file='config.ini')
	if '--no-config' not in argv:
		config = config.load()
	else:
		config = config.default()
	if config is None:
		print('Unable the Open the config. Try Use Option `--no-config`')
		sys.exit(1)
	# print(json.dumps(config,indent=4))

	if '--character-number' in argv:
		print('--character-number')
	if '--character-lower' in argv:
		print('--character-lower')
	if '--character-upper' in argv:
		print('--character-upper')
	if '--character-special' in argv:
		print('--character-special')
	if '--length-begin' in argv:
		print('--length-begin')
	if '--length-until' in argv:
		print('--length-until')

	chrslist = []
	if config['global']['character-number']: 
		chrslist += application_module_chars().chrs_number()
	if config['global']['character-lower']: 
		chrslist += application_module_chars().chrs_lower()
	if config['global']['character-upper']: 
		chrslist += application_module_chars().chrs_upper()
	if config['global']['character-special']: 
		chrslist += application_module_chars().chrs_spechar()

	print(' '.join(chrslist).strip())

	for i in range(config['global']['length-begin'], config['global']['length-until']+1):
		print(i)

	text = ''
	while len(text)<=config['global']['length-until']+1:
		text += '+'
	for i0 in list(chrslist):
		print(i0)
	print(len(chrslist))

