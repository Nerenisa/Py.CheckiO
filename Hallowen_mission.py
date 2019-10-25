#!/usr/bin/env python3
# coding: utf-8

import re
from itertools import combinations
import itertools

MONSTERS = ['skeleton', 'ghost', 'jack', 'vampire', 'witch', 'mummy', 'zombie', 'werewolf', 'frankenstein'] 








# MONSTERS = '''
# skeleton
# ghost
# jack
# vampire
# witch
# mummy
# zombie
# werewolf
# frankenstein
# '''


def halloween_monsters(spell: str)-> int:
    s1 = []
    for letter_2 in MONSTERS:
        Res = ''.join([x for x in letter_2 if x in spell])
        s2 = []
        if Res > letter_2:
           s2.append(Res)
            
        elif Res == letter_2:
           s1.append(Res) 
                 
    
    d = ' '.join((s1))
    if 'ghost' in d:
        repl = d.replace('jack', 'ghost') 
        return len(repl.split())
    elif 'witch' in d:
        dubl = ' '.join(('witch', d)) 
        return len(dubl.split())
    elif 'skeleton' in d:
        dell = ' '.join(((re.sub(r'\s+', ' ', (d.replace('jack', ''))), '(not jack)')))
        return len(dell.split(maxsplit=1))
    elif 'vampire' in d:
        dell_1 = ' '.join((''.join(((re.sub(r'\s+', ' ', (d.replace('mummy', ''))), 'vampire'))), '(not mummy)'))
        return len(dell_1.split(maxsplit=1))
    else:
        return len(d.split())

   



if __name__ == '__main__':
    assert halloween_monsters('casjokthg') == 2, 'jack ghost'
    assert halloween_monsters('leumooeeyzwwmmirbmf') == 3, 'mummy zombie werewolf'
    assert halloween_monsters('nafrweiicttwneshhtikcn') == 3, 'witch witch frankenstein'
    assert halloween_monsters('kenoistcepajmlvre') == 2, 'skeleton vampire (not jack)'
    assert halloween_monsters('miaimavrurymepepv') == 2, 'vampire vampire (not mummy)'
    print("Your spell seem to be okay. It's time to check.")