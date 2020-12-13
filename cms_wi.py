# -*- coding: utf-8 -*-
import re

def normalize_cms_WI(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      # WI
      newName = re.sub('ALDEN MEADOW PARK HCC', 'ALDEN MEADOW PARK', newName)
      newName = re.sub('BADGER PRAIRIE HCC', 'BADGER PRAIRIE HEALTH CARE CENTER', newName)
      newName = re.sub('BAY AT BURLINGTON HEALTH AND REHABILITATION', 'BAY AT BURLINGTON', newName)
      newName = re.sub('BAY AT SURING HEALTH AND REHABILITATION CENTER', 'BAY AT SURING', newName)
      newName = re.sub('BEAVER DAM HEALTH CARE CENTER', 'BEAVER DAM HCS AT BEAVER DAM', newName)
      newName = re.sub('BELMONT NURSING AND REHABILITATION CENTER', 'BELMONT LTCF AND REHABILITATION CENTER', newName)
      newName = re.sub('CHIPPEWA MANOR NURSING AND REHABILITATION', 'CHIPPEWA MANOR AND REHABILITATION', newName)
      newName = re.sub('WI VETERANS HM AINSWORTH HALL', 'WISCONSIN VETERANS HOME AINSWORTH HALL', newName)
      newName = re.sub('WI VETERANS HM MACARTHUR HALL', 'WISCONSIN VETERANS HOME MACARTHUR HALL', newName)
      newName = re.sub('WI VETERANS HM OLSON HALL', 'WISCONSIN VETERANS HOME OLSON HALL', newName)
      newName = re.sub('WI VETERANS HOME AT CHIPPEWA FALLS', 'WISCONSIN VETERANS HOME AT CHIPPEWA FALLS', newName)
      newName = re.sub('WI VETERANS HOME-BOLAND HALL', 'WISCONSIN VETERANS HOME AT BOLAND HALL', newName)
      
      return newName