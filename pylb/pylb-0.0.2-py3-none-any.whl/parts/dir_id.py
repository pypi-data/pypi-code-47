
# dir_idの管理 [dir_id.py]

import os
import sys
import random
# 絶対パスに変換 [path_utils.py]
from .path_utils import rel_to_abs
# dir_idの衝突エラー [error_message.py]
from .error_message import dir_id_collision_error

# 新しいdir_idを生成 [dir_id.py]
def gen_new_dir_id(digits = 64):
	# 現状を退避
	rand_state = random.getstate()
	# 状態の攪拌
	random.seed()
	ls = [random.choice("0123456789abcdef") for _ in range(digits)]
	# 現状を退避
	random.setstate(rand_state)
	return "".join(ls)

# dir_idの設置(ない場合) [dir_id.py]
def gen_dir_id(dirname):
	# __pylb__の場所
	pylb_path = "%s/__pylb__/"%dirname
	# __pylb__の作成
	if os.path.exists(pylb_path) is False: os.mkdir(pylb_path)
	# dir_idファイルの存在確認
	dir_id_file = "%s/dir_id.txt"%pylb_path
	if os.path.exists(dir_id_file) is False:
		with open(dir_id_file, "w", encoding = "utf-8") as f:
			f.write(gen_new_dir_id())	# 新しいdir_idを生成

# dir_idの重複チェック [dir_id.py]
def dir_id_check(lib_dirname, pylb):
	# 絶対パスに変換
	lib_dirname = rel_to_abs(lib_dirname)
	# dir_idの取得
	with open("%s/__pylb__/dir_id.txt"%lib_dirname, "r", encoding = "utf-8") as f:
		dir_id = f.read()
	# 干渉チェック (物理パスが異なるがdir_idが同じものがあるかをチェック)
	if dir_id not in pylb._dir_id_check_memo:
		pylb._dir_id_check_memo[dir_id] = lib_dirname
		return True
	temp_dic = pylb._dir_id_check_memo[dir_id]
	if temp_dic == lib_dirname: return True
	# dir_idの衝突エラー [error_message.py]
	dir_id_collision_error(temp_dic, lib_dirname)
