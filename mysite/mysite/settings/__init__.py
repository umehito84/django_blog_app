# setting ファイルの入れ替えを初期化コードで行う
# 開発環境では localモジュールが呼び出され、本番環境では productionモジュールが呼ばれる

from .production import *

try:
	from .local import *
except:
	pass