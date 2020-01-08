from .excel.sf_excel import Excel
from .textgrid.sf_textgrid import SFTextGrid
from .metadata.sf_metadata import SFMetadata
from .wav.sf_wav import SFWav
from .utils.sf_utils import SFUtils
from .filesystem.sf_filesystem import SFFS


def help(ftype=""):
	ftype = ftype.lower()
	if "excel" in ftype:
		Excel.help()
	elif "textgrid" in ftype:
		SFTextGrid.help()
	elif "metadata" in ftype:
		SFMetadata.help()
	elif "wav" in ftype:
		SFWav.help()
	elif "fs" in ftype or "filesystem" in ftype:
		SFFS.help()
	elif "util" in ftype:
		SFUtils.help()
	else:
		print("Excel:","myexcel = Excel()"," 读写EXCEL类")
		print("SFTextGrid:","mytg = SFTextGrid()"," 操作TextGrid")
		print("SFMetadata:","mymd = SFMetadata()"," 操作Metadata")
		print("SFWav:","mywav = SFWav()"," 操作wav")
		print("SFFS:","myfs = SFFS()"," 文件系统")
		print("SFUtils:","SFUtils.xxxx()"," 一些通用的方法")
		print("以上可通过调用各类的静态的help()方法查看详细说明")
		print("或调用kog_lib.help(type)查看，type为功能的类型('excel','textgrid','metadata','wav','fs','utils')")
