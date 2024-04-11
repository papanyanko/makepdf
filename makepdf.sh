# !/usr/bin/bash
if [ "$#" -lt 1 ]; then
	echo "画像ファイルのあるディレクトリへのパスを指定してください"
	exit 1
else
	. .venv/bin/activate
	python3 ./src/makepdf.py "$1"
	deactivate
fi