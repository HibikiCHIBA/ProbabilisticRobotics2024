# ProbabilisticRobotics2024

千葉工業大学 上田隆一先生の講義 確率ロボティクス 2024年度版の内容に沿って作成した課題の提出用リポジトリ

# Install
インストールは, 下記コマンドのようにインストールしたいGithubページのURLを挿入することで開始される. インストールが終了したら, ProbabilisticRobotics2024ディレクトリへ移動し, 内部ファイルが正しくインストールされているかを確認すること. 
```
$ git clone https://github.com/HibikiCHIBA/ProbabilisticRobotics2024.git
$ cd ProbabilisticRobotics2024
$ ls
LICENSE  MCL_demo.py  README.md
```

# MCL_demo
初期位置を50(0〜100)として，1次元の数直線上を左右に動くロボットを想定し，MCL(Monte Carlo Localization)を使用して目標位置へ追従するシミュレーションデモを実装した．なお，目標位置は乱数で決定される． 結果は時間と位置の2次元のグラフとして出力される．

# Environment
* Ubuntu 20.04.4 LTS
* python 3.8.10

(上記環境にてテスト済み)


# Demo
実行例を示す. 例として，タイムステップが100まで，動作時のノイズを1.0，センサのノイズを2.0とそれぞれ設定して実行した．実行時の出力を下図に示す．横軸がタイムステップ，縦軸が位置，青が乱数で決定された目標位置，赤がMCLを使用して推定した位置をそれぞれ示している．
```
$ python3 MCL_demo.py
```

[![実行例の出力図](/example.png "実行時に出力される図例")]

# License
* このソフトウェアパッケージは, [3条項BSDライセンス](https://opensource.org/license/bsd-3-clause/)の下, 再配布および使用が許可されています. 
* © 2024 Hibiki Chiba
