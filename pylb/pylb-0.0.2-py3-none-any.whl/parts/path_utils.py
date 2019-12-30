
# path関係の処理 [path_utils.py]

import os
import sys
import inspect
import pathlib
# library拡張子違いエラー [error_message.py]
from .error_message import py_lib_ext_error
# library非存在エラー [error_message.py]
from .error_message import py_lib_existence_error

# 絶対パスに変換 [path_utils.py]
def rel_to_abs(rel_path):
	p = pathlib.Path(rel_path)
	return str(p.resolve())

# current_dirの絶対パスを取得 [path_utils.py]
def get_abs_cur():
	rel_cur = os.getcwd()	# カレントパスの取得 (相対)
	return rel_to_abs(rel_cur)	# 絶対パスに変換

# pylb.loadが記載された場所を取得 (絶対パス) [path_utils.py]
def get_abs_load_path(pylb):
	# 呼び出しスタックの取得
	stack = inspect.stack()
	# 2個前の場所を調べる (この関数自体の呼び出しもカウントされることに注意)
	rel_file_path = stack[3].filename
	# 呼び出し元がシェルの場合はcwdを返す
	if rel_file_path == "<stdin>": return pylb._lib_save_path
	# ファイルの存在する場所(絶対パス)を調べる
	abs_file_path = rel_to_abs(rel_file_path)	# 絶対パスに変換
	abs_load_path, _ = os.path.split(abs_file_path)
	return abs_load_path

# ライブラリの場所を絶対パスに変換 [path_utils.py]
def lib_path_to_abs(raw_lib_path, abs_load_path):
	# もともと絶対パスの場合はそのまま
	p = pathlib.Path(raw_lib_path)
	if p.is_absolute() is True: return raw_lib_path
	# 絶対パスに変換
	raw_abs_lib_path = "%s/%s"%(abs_load_path, raw_lib_path)
	abs_lib_path = rel_to_abs(raw_abs_lib_path)	# 絶対パスに変換 [path_utils.py]
	return abs_lib_path

# パス分解オブジェクト [path_utils.py]
class Div_Path:
	# 初期化処理
	def __init__(self, abs_path):
		# フルパス
		self.fullpath = abs_path
		# パスの分解
		self.dirname, raw_name = os.path.split(self.fullpath)
		self.filename, self.ext = os.path.splitext(raw_name)

# libraryのパスを扱いやすい形に格納 [path_utils.py]
def pack_lib_path(raw_lib_path, pylb):
	# pylb.loadが記載された場所を取得 (絶対パス)
	abs_load_path = get_abs_load_path(pylb)
	# ライブラリの場所を絶対パスに変換
	abs_lib_path = lib_path_to_abs(raw_lib_path, abs_load_path)
	# パス分解オブジェクトの生成
	lib_dp = Div_Path(abs_lib_path)
	# 拡張子の確認
	if lib_dp.ext != ".py": py_lib_ext_error()	# library拡張子違いエラー [error_message.py]
	# libraryの存在確認
	if os.path.exists(lib_dp.fullpath) is False:
		py_lib_existence_error(lib_dp.fullpath)	# library非存在エラー [error_message.py]
	return lib_dp
