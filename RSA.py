# 情報ネットワーク #RSA公開鍵暗号方式の計算

import math

P = 73  # 秘密情報 #素数
Q = 83  # 秘密情報 #素数

N = P*Q  # 公開情報
phi_N = (P-1)*(Q-1)  # オイラーのφ関数

e = 53  # 公開情報 #phi_Nと互いに素になる任意の整数

d = 1
while e*d % phi_N != 1:
    d += 1

print(f"P={P}, Q={Q}, N={N}, e={e}, φ(N)={phi_N}, d={d}")


# 暗号化と復号
a = 777  # 送るメッセージ
b = a**e % N  # 暗号化
a_decryption = b**d % N  # 復号
print(f"元のメッセージはA={a}, 暗号化されたメッセージはB={b}, 復号されたメッセージはA'={a_decryption}です。")


# 署名と検証
s = a**d % N  # 署名
a_decryption_test = s**e % N  # 復号（検証）
print(f"元のメッセージはA={a}, 署名はs={s}, 復号（検証）されたメッセージはA''={a_decryption_test}です。")
