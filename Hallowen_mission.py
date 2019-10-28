#!/usr/bin/env python3
# coding: utf-8

import re
# from collections import Counter
# from copy import deepcopy

MONSTERS = ['skeleton', 'ghost', 'jack', 'vampire', 'witch', 'mummy', 'zombie', 'werewolf', 'frankenstein'] 



def halloween_monsters(spell: str)-> int:
   newmonstr = []
   notmonstr = []
   for letter_2 in MONSTERS:
        Res = ''.join([x for x in letter_2 if x in spell])
        if Res != letter_2:
           notmonstr.append(Res) 
        elif Res == letter_2:
           newmonstr.append(Res) 
                 
   #k = ' '.join(''.join(notmonstr))  # ?
   d = ' '.join((newmonstr))
   try:
      if notmonstr not in MONSTERS:
         return 0
   finally:
      if 'ghost' in d:
        return len (d.replace('jack', 'ghost').split())
      elif 'witch' in d:
        return len(' '.join(('witch', d)).split())
      elif 'skeleton' in d:
        return len(' '.join(((re.sub(r'\s+', ' ', (d.replace('jack', ''))), '(not jack)'))).split(maxsplit=1))
      elif 'vampire' in d:
        return len(' '.join((''.join(((re.sub(r'\s+', ' ', (d.replace('mummy', ''))), 'vampire'))), '(not mummy)')).split(maxsplit=1))
      else:
        return len(d.split())



if __name__ == '__main__':
  #  assert halloween_monsters('casjokthg') == 2, 'jack ghost'
  #  assert halloween_monsters('leumooeeyzwwmmirbmf') == 3, 'mummy zombie werewolf'
  #  assert halloween_monsters('nafrweiicttwneshhtikcn') == 3, 'witch witch frankenstein'
  #  assert halloween_monsters('kenoistcepajmlvre') == 2, 'skeleton vampire (not jack)'
  #  assert halloween_monsters('miaimavrurymepepv') == 2, 'vampire vampire (not mummy)'
  assert halloween_monsters('ctiqzyfnlsjlpbxkxrgqosokkimthutcyekbrjadzogwufzxbwqeuvhsnhv') == 5, 'jack gohst gohst zombie witch'
  assert halloween_monsters('qldwfrzqrzmqojxsdecnfn') == 0, 'qldwfrzqrzmqojxsdecnfn'
  assert halloween_monsters('klojpaeeeusdopxwpbnlurfqlsbhrkjxecyihgtnyqjcqabwtrmmcdmfadnzkctavgxsrmvq') == 7, 'jack jack jack gohst vampire mummy werewolf'
  print("Your spell seem to be okay. It's time to check.")








