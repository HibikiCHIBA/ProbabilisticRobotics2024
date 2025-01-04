# ProbabilisticRobotics2024

千葉工業大学 上田隆一先生の講義 確率ロボティクス 2024年度版の内容に沿って作成した課題の提出用リポジトリ

# Install
インストールは, 下記コマンドのようにインストールしたいGithubページのURLを挿入することで開始される. インストールが終了したら, robosys2023ディレクトリへ移動し, 内部ファイルが正しくインストールされているかを確認すること. 
```
$ git clone https://github.com/HibikiCHIBA/ProbabilisticRobotics2024.git
$ cd ProbabilisticRobotics2024
$ ls
LICENSE  README.md  MLC_demo.py
```

# MLC_demo
1, -2, 3, -4, …, といった数列から標準入力値(自然数)で指定した数列の整数までの総和を計算する. 例えば標準入力値が, 1, 2, 3, 4, …, であった場合, 出力は, 1, -1, 2, -2, …, となる. 

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
