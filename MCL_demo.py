#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Hibiki Chiba
# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
import matplotlib.pyplot as plt
import time

# 定義
line_size = 100         # 数直線の長さ
time_remit = 100        # 動作時間
num_particles = 1000    # 粒子数
motion_noise = 1.0      # 動作時のノイズ
sensor_noise = 2.0      # センサのノイズ
true_position = 50      # ロボットの真値（初期位置設定）

# 粒子の初期化
particles = np.random.uniform( 0, line_size, num_particles )
weights = np.ones( num_particles ) / num_particles

# ロボットの移動モデル
def move( position, distance ):
    position += distance + np.random.normal( 0, motion_noise )
    return position % line_size

# ロボットのセンサモデル
def sense( true_position ):
    return true_position + np.random.normal(0, sensor_noise)

# 粒子の重みを更新
def weight_update( particles, measurement ):
    weights = np.exp( -( ( particles - measurement ) ** 2 ) / ( 2 * sensor_noise ** 2 ) )
    weights += 1e-300  # ゼロ除算を防ぐ
    return weights / weights.sum()

# 重みを考慮して粒子をリサンプリング
def resample( particles, weights ):
    indices = np.random.choice( range( num_particles ), size=num_particles, p=weights )
    return particles[ indices ]

# プロット設定
plt.ion()
fig, ax = plt.subplots( figsize=( 10, 6 ) )

# 実行ループ
true_positions = [ true_position ]
estimated_positions = []

step = 0
try:
    while True:
        move_distance = np.random.uniform( -5, 5 )  # 動作指令
        true_position = move( true_position, move_distance )
        true_positions.append( true_position )

        # 観測
        measurement = sense( true_position )

        # 重み更新
        weights = weight_update( particles, measurement )

        # 推定位置計算
        estimated_position = np.average( particles, weights=weights )
        estimated_positions.append( estimated_position )

        # リサンプリング
        particles = resample( particles, weights )

        # 移動
        particles = np.array( [ move( p, move_distance ) for p in particles ] )

        # プロット更新
        ax.clear()
        ax.plot( true_positions, label='True Position', marker='o', color='blue', linestyle='-' )
        ax.plot( estimated_positions, label='Estimated Position', marker='x', color='red', linestyle='--' )
        ax.set_xlim( 0, len( true_positions ) )
        ax.set_ylim( 0, line_size )
        ax.set_xlabel( 'Time Step' )
        ax.set_ylabel( 'Position' )
        ax.set_title( '1D Monte Carlo Localization' )
        ax.legend()
        ax.grid()

        plt.pause( 0.1 )  # 表示周期

        # ステップカウントしタイムリミットで停止
        step += 1
        if step >= time_remit:
            break

finally:
    plt.ioff()
    plt.show()
