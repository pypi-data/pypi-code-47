
# コード変更差分管理 [code_diff_check.py]

import os
import sys
import shutil
import difflib

# ファイル間の比較 [code_diff_check.py]
def file_diff(file_1, file_2):
	f1 = open(file_1, 'r', encoding = "utf-8")
	f2 = open(file_2, 'r', encoding = "utf-8")
	ls1 = f1.readlines()
	ls2 = f2.readlines()
	if ls1 == ls2: return None
	d = difflib.Differ()
	result = d.compare(ls1, ls2)
	return '\n'.join(result)

# 前回読み込み時からの差分をチェック [code_diff_check.py]
def check_diff(backup_filename, lib_filename):
	message_header = "\n\n*** [pylb] pylb.load() confirm ***\n\n\tsource file: %s\n\n"%lib_filename
	# backupがない場合
	if os.path.exists(backup_filename) is False:
		print(message_header)
		print("前のバージョンが見つかりません。ソースコードを確認する場合は一旦プログラムを終了してください。\n問題ない場合は[Enter]で続行してください。")
		print("\nPrevious version of module not found. If necessary, exit the program and check the source code.\nIf there is no problem to continue, press the [Enter] key.")
		input(">")
		return "no backup"
	# ファイル間の比較
	diff_result = file_diff(backup_filename, lib_filename)
	if diff_result is None: return "no change"
	print(message_header)
	print(diff_result)
	print("\n前回実行時から上記の変更があります。ソースコードを確認する場合は一旦プログラムを終了してください。\n問題ない場合は[Enter]で続行してください。")
	print("\nAs shown above, some parts have been changed since the last run. \nIf necessary, exit the program and check the source code.\nIf there is no problem to continue, press the [Enter] key.")
	input(">")
	# 変更を検知
	return "change"

# 差分確認と最新版保存 [code_diff_check.py]
def check_and_save(lib_dp, lib_save_path):
	# dir_idの取得
	with open("%s/__pylb__/dir_id.txt"%lib_dp.dirname, "r", encoding = "utf-8") as f:
		dir_id = f.read()
	# saveする場所
	if os.path.exists("%s/__pylb__/"%lib_save_path) is False: os.mkdir("%s/__pylb__/"%lib_save_path)
	# 前回呼び出し時のファイル
	backup_filename = "%s/__pylb__/%s_%s%s"%(
		lib_save_path,	# lib保存場所
		lib_dp.filename,	# lib名
		dir_id,	# libのdir_id
		lib_dp.ext	# libの拡張子
	)
	# 前回読み込み時からの差分をチェック
	check_diff(backup_filename, lib_dp.fullpath)
	# コピーして保存
	shutil.copyfile(lib_dp.fullpath, backup_filename)
