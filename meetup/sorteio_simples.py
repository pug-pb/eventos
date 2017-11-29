import random #biblioteca python para sorteios
import sys

inscrições = """
14
16
23
13
8
4
28
17
30
36
11
6
5
33
3
19
26
34
15
2
21
18
37
29
20
32
24
10
27
1
7
25
31
22
12
35
9
40
41
42
43
44
"""

inscritos = inscrições.split('\n')

while True:
    print('S para sorteio, P para parar')
    if sys.version_info.major == 3:
        opt = input()
    else:
        opt = raw_input()
    if opt in ['S', 's']:
        ganhador = random.sample(inscritos, 1)
        inscritos.remove(ganhador[0])
        print(ganhador[0])
    else:
        break