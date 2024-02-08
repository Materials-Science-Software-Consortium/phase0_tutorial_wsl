はじめに
================================

概要
------------------

本稿は第一原理バンド計算ソフトウェアPHASE/0のチュートリアルです。「高性能計算・データ分析基盤システム SQUID」において実施します。

本チュートリアルの構成
-----------------------

\ :ref:`si2_chapter` では簡単に計算できる例として2原子からなるシリコン結晶の例を扱います。基本となるself-consistent field (SCF) 計算を実行し，それをもとに電子状態密度やバンド構造，誘電関数の計算などを実行します。また，振動解析や :math:`EV` 曲線の計算を行う方法も紹介します。\ :ref:`mag_chapter` では磁性の扱い方を紹介します。磁性を有効にする方法や磁性を考慮している場合の結果の解析方法などを説明します。\ :ref:`surf_chapter` では表面の計算の方法を紹介します。PHASE/0は平面波基底に基づいて計算を行うため，扱えるのは厳密にいうと周期系のみです。しかし表面に垂直な方向に十分な厚さの"真空層"を設けることによって事実上表面と変わらない系を扱うことはできます。ここではその方法について説明します。また，単純な結晶では必要ない「構造最適化」の方法を説明し，さらに原子ごとの電子状態を解析する方法についても説明します。\ :ref:`defect_chapter` では点欠陥のエネルギー計算を扱います。ここでは，第一原理計算において「生成エネルギー」はどのように計算するかを説明します。最後に，\ :ref:`sup_chapter` においてはPHASE/0を活用するためのちょっとしたコツなどを紹介していきます。


準備
----------------------

必要な実行バイナリーやサンプルデータをかためたアーカイブははSQUIDの ``/tmp/20240213/20240213.tar.gz`` に配置されています。ご自身のホームディレクトリーにコピーして展開してください。

.. code-block:: text

  cd ~
  cp /tmp/20240213/20240213.tar.gz .
  tar -zxvf 20240213.tar.gz

原子配置の可視化には `VESTA <https://jp-minerals.org/vesta/jp/>`_ を用いるので，こちらはローカルPCにインストールしておくことが推奨されます。

PHASE/0の引用情報など
-----------------------

- ホームページ
  https://azuma.nims.go.jp/

- GitHub
  https://github.com/Materials-Science-Software-Consortium

- 論文
  Takahiro Yamasaki, Akiyoshi Kuroda, Toshihiro Kato, Jun Nara, Junichiro Koga, Tsuyoshi Uda, Kazuo Minami, and Takahisa Ohno,
  "Multi-axis Decomposition of Density Functional Program for Strong Scaling up to 82,944 Nodes on the K Computer: Compactly Folded 3D-FFT Communicators in the 6D Torus Network"
  Computer Physics Communications 244, 264-276 (2019).
  https://doi.org/10.1016/j.cpc.2019.04.008

