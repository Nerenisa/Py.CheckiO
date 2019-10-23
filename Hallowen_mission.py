#!/usr/bin/env python3
# coding: utf-8

import re
from itertools import combinations
import itertools

M = ['skeleton', 'ghost', 'jack', 'vampire', 'witch', 'mummy', 'zombie', 'werewolf', 'frankenstein'] 








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
    for i in M:
        k = []
        if len(spell) >= len(i):
            
            a = []
            for d in i:
                for s in spell:
                    if d == s:
                        a.append(s)
            h = ''.join(a)
        if h = i:
           k.append(h) 
           print(k)
        # elif len(spell) < len(i):
        #    for d in i:
        #         for s in spell:
        #             if d == s:
        #                 a.append(s)
        
    #print(a)  
    
    
    



if __name__ == '__main__':
    assert halloween_monsters('casjokthg') == 2, 'jack ghost'
    assert halloween_monsters('leumooeeyzwwmmirbmf') == 3, 'mummy zombie werewolf'
    assert halloween_monsters('nafrweiicttwneshhtikcn') == 3, 'witch witch frankenstein'
    assert halloween_monsters('kenoistcepajmlvre') == 2, 'skeleton vampire (not jack)'
    assert halloween_monsters('miaimavrurymepepv') == 2, 'vampire vampire (not mummy)'
    print("Your spell seem to be okay. It's time to check.")