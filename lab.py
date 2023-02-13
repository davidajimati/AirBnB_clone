#!/usr/bin/python3
string = 'User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")'
real = []

pre = string.split('.')
real.append(pre[0])

pre2 = pre[1].split('("')
real.append(pre2[0])

pre = string.split('.')
real.append(pre[0])

pre2 = pre[1].split('("')
real.append(pre2[0])

pre3 = pre2[1].split('")')
real.append(pre3[0])

print(real)
