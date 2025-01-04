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
初期位置を50(0〜100)として，1次元の数直線上を左右に動くロボットを想定し，MCL(Monte Carlo Localization)を使用して目標位置へ追従するシミュレーションデモを実装した．なお，目標位置は乱数で決定される． 

# Environment
* Ubuntu 20.04.4 LTS
* python 3.8.10

(上記環境にてテスト済み)


# Demo
実行例を示す. 例として標準入力が5と6の場合の実行コマンドが下記の通りである. 
```
$ seq 5 | ./plus  
3
$ seq 6 | ./plus  
-3
```

# License
* このソフトウェアパッケージは, [3条項BSDライセンス](https://opensource.org/license/bsd-3-clause/)の下, 再配布および使用が許可されています. 
* © 2024 Hibiki Chiba
