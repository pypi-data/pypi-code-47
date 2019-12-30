
# 読み込み (import) [import_core.py]

import os
import sys
import shutil

# 読み込み (import) [import_core.py]
def import_core(lib_dp):
	# dir_idの取得
	with open("%s/__pylb__/dir_id.txt"%lib_dp.dirname, "r", encoding = "utf-8") as f:
		dir_id = f.read()
	# 一時ファイル名
	temp_filename = "__pylb_load_temp_%s_%s"%(lib_dp.filename, dir_id[:10])	# 新しいdir_idを生成
	temp_full = "%s/%s.py"%(lib_dp.dirname, temp_filename)
	# 一時ファイルを生成 (別ディレクトリに存在する同名のファイルと確実に区別するため)
	shutil.copyfile(lib_dp.fullpath, temp_full)
	# 読み込み
	sys.path.append(lib_dp.dirname)
	exec("import %s as pylb_temp_lib"%temp_filename)
	# 魔界(exec,eval)から外のスコープにモジュールを連れ出す
	ret_pylb_temp_lib = eval("pylb_temp_lib")
	# 一時ファイルを削除
	if os.path.exists(temp_full): os.remove(temp_full)
	return ret_pylb_temp_lib
