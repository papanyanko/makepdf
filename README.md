PNG形式の画像からしおりつきPDFを作る

使い方
トップレベルにresourceとdistディレクトリを作る
resource内に作成したいpdfの名前でディレクトリを作る
pdf名のディレクトリの中に画像としおり用tsvを用意する
`sh makepdf.sh`
distにpdfが出力される

しおりtsvの形式
タブ区切り
タブインデントでしおりの入れ子構造を表現する
目次	4
第1章 タイトル	10
	第1節	10