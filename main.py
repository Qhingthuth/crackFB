#!/usr/bin/python3
# Mau Recode Yaaaa???
# Silahkan Bree Izin Dulu Tapi Lah
# Feri Pratama
# CyberCarboon2
#--------------------------[ MODULE ]---------------------
import os,sys
import Feri
try:
	import user_agent2
except (ImportError,ModuleNotFoundError):
	os.system('pip install user-agent2 && pip install get-useragents')
def create_dir():
	try:
		os.mkdir('OK')
	except:
		pass
	try:
		os.mkdir('CP')
	except:pass


def __feri__():
	Feri.main()
	
if __name__=="__main__":
	create_dir()
	__feri__()
