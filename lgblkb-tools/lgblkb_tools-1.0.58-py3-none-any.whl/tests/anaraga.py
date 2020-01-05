from lgblkb_tools import logger,Folder
import pandas as pd

def main():
	filepath=r'/home/lgblkb/Desktop/База население.xlsx'
	filepath=r'/home/lgblkb/Desktop/База предприниматели.xlsx'
	df=pd.read_excel(filepath)
	logger.debug('df:\n%s',df)
	
	pass

if __name__=='__main__':
	main()
