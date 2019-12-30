
# pyLibraryBinder [pylb]

import os
import sys
# current_dirの絶対パスを取得 [path_utils.py]
from .parts.path_utils import get_abs_cur
# libraryのパスを扱いやすい形に格納 [path_utils.py]
from .parts.path_utils import pack_lib_path
# dir_idの設置(ない場合) [dir_id.py]
from .parts.dir_id import gen_dir_id
# dir_idの重複チェック [dir_id.py]
from .parts.dir_id import dir_id_check
# 差分確認と最新版保存 [code_diff_check.py]
from .parts.code_diff_check import check_and_save
# 読み込み (import) [import_core.py]
from .parts.import_core import import_core

# 自身の読み込み
_here_dir, _ = os.path.split(__file__)
sys.path.append(_here_dir)
import pylb

# 前回呼び出しlib保存場所
_lib_save_path = None
# dir_idの重複をチェックする辞書
_dir_id_check_memo = {}

# load library [pylb]
def load(raw_lib_path):
	# 前回呼び出しlib保存場所の取得 (最初にpylbが呼ばれた際のcurrent_dirの絶対パス)
	if pylb._lib_save_path is None:
		pylb._lib_save_path = get_abs_cur()	# current_dirの絶対パスを取得
	# libraryのパスを扱いやすい形に格納 [path_utils.py]
	lib_dp = pack_lib_path(raw_lib_path, pylb)
	# dir_idの設置(ない場合)
	gen_dir_id(lib_dp.dirname)
	# dir_idの重複チェック
	dir_id_check(lib_dp.dirname, pylb)
	# 差分確認と最新版保存
	check_and_save(lib_dp, pylb._lib_save_path)
	# 読み込み (import)
	ret_pylb_temp_lib = import_core(lib_dp)
	return ret_pylb_temp_lib
