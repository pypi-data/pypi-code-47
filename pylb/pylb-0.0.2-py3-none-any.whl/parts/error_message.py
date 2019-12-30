
# エラーメッセージ [error_message.py]

import sys

# dir_idの衝突エラー [error_message.py]
def dir_id_collision_error(dir_1, dir_2):
	raise Exception(f"""\n\n\n
	*** [pylb error] dir_id collision ***

	## Collision Directories
		{dir_1}
		{dir_2}

	## 対応策 (Japanese)
		1. 上記が同一機能の場合
			片方のみ読み込むようにコードを変更してください
		2. 別機能としたい場合
			新しく作った方(複製した方)の__pylb__ディレクトリを削除してください

	## HOW TO FIX (English)
		1. When both modules have the same function
			Change the source code to load only one module out of two modules.
		2. When both modules have different functions
			Delete the __pylb__ directory in the newly created (or copied) module.

	(press [Enter] key ...)

	""")

# library拡張子違いエラー [error_message.py]
def py_lib_ext_error():
	raise Exception("\n\n[pylb error] only .py format files are supported.")

# library非存在エラー [error_message.py]
def py_lib_existence_error(lib_path):
	raise Exception("\n\n[pylb error] library below was not found.\n\t%s"%lib_path)
