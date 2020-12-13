# -*- coding: utf-8 -*-
import re

def normalize_cms_MA(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      # MA
      newName = re.sub('WINGATE AT HAVERHILL', 'WINGATE RESIDENCES AT HAVERHILL',newName)
      newName = re.sub('WINGATE AT NEEDHAM', 'WINGATE RESIDENCES AT NEEDHAM',newName)
      newName = re.sub('WINGATE AT NORTON', 'WINGATE RESIDENCES AT NORTON',newName)


      return newName