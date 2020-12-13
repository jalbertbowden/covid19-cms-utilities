# -*- coding: utf-8 -*-
import re

def normalize_cms_WV(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      # WV 
      newName = re.sub('WAR MEMORIAL HOSPITAL', 'WAR MEMORIAL HOSPITAL EXTENDED CARE FACILITY', newName)
      newName = re.sub('MAPLES NURSING HOME', 'MAPLES HEALTH CARE', newName)
      newName = re.sub('JOHN MANCHIN SR HEALTH CARE CENTER', 'JOHN MANCHIN SR. HEALTH CARE CENTER', newName)
      newName = re.sub('MADISON$', 'MADISON CENTER', newName)
      newName = re.sub('HOLBROOK HEALTHCARE CENTER', 'HOLBROOK NURSING HOME', newName)
      
      return newName