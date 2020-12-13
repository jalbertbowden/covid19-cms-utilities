# -*- coding: utf-8 -*-
import re

def normalize_cms_OR(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      # OR
      newName = re.sub('GRACELEN TERRACE NF', 'GRACELEN TERRACE', newName)
      newName = re.sub('LAURELHURST VILLAGE', 'LAURELHURST VILLAGE REHABILITATION', newName)
      newName = re.sub('MARQUIS FOREST GROVE POST ACUTE REHABILITATION', 'MARQUIS FOREST GROVE ASSISTED LIVING', newName)
      newName = re.sub('MARQUIS MILL PARK', 'MARQUIS MILL PARK POST ACUTE REHABILITATION', newName)
      newName = re.sub('MARQUIS MT TABOR', 'MARQUIS MT. TABOR', newName)
      newName = re.sub('PROVIDENCE BENEDICTINE NURSING CENTER', 'PROVIDENCE BENEDICTINE MT. ANGEL', newName)
      newName = re.sub('ROBISON JEWISH HEALTH CENTER', 'ROBISON HEALTH AND REHABILITATION CENTER', newName)
      
      return newName