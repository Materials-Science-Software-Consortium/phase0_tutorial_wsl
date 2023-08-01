# phase0_tutorial_wsl

講習会などで用いている例題とその説明です．WSLで実行することを想定していますが，一般的なLinuxやmacOSにおいても問題なく実行することができます．
[こちらから](https://phase0-tutorial-wsl.readthedocs.io/ja/latest/) HTML版のドキュメントをみることができます

# 必要なソフトウェア

説明の文章はSphinx を用いているので，Sphinxをインストールする必要があります．
```
pip install sphinx
```

また，Read the Docsが提供しているテーマを利用しているのでこれもインストールします．
```
pip install sphinx_rtd_theme
```

# 含まれるファイルについて

トップディレクトリーにあるファイル/ディレクトリーは下記の通り。
- Makefile : Sphinx用のMakefileです．Sphinxのインストールができていれば`make html` とすることによってHTMLのドキュメントを得ることができます．
- make.bat : Sphinx用のMakefileです．Windowsで用います．`make.bat html` とすることによってHTMLのドキュメントを得ることができます．
- source : Sphinx のソースコードが格納されたディレクトリーです．
- wsl : 例題の入力ファイルが格納されています．

