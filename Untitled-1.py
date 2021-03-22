# coding: utf-8

''' inputデータを逆順にリスト化 '''
s_list = [int(i) for i in list(input())]
s_list_inv = list(reversed(s_list))
t_list = [int(i) for i in list(input())]
t_list_inv = list(reversed(t_list))
ans_list = []
frag = 0                        # 繰り上がりフラグ
# print(s_list_inv, t_list_inv)

for i in range(len(s_list)):
    
    tmp = s_list_inv[i] + t_list_inv[i] + frag
    ans_list.append(str(tmp % 10))  # .join()は数値型があればエラーとなる

    if tmp >= 10:
        frag = 1
    else:
        frag = 0
        
    # print(ans_list)

if frag == 1:   # 最後の桁の繰り上がり
    ans_list.append(str(frag))
    
ans_list_inv = list(reversed(ans_list))

ans = ''.join(ans_list_inv)
print(ans)
