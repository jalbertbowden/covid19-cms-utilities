# -*- coding: utf-8 -*-
import re

def normalize_cms_WY(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      # WY
      # newName = re.sub('ST JOHN\'S NURSING HOME', 'ST JOHNS LIVING CENTER', newName)
      newName = re.sub('CASPER MOUNTAIN REHABILITATION AND CARE CENTER', 'CASPER MOUNTAIN REHABILITATION', newName)
      newName = re.sub('DOUGLAS CARE CENTER LLC', 'DOUGLAS CARE CENTER', newName)
      newName = re.sub('ST JOHN\'S NURSING HOME', 'ST JOHNS LIVING CENTER', newName)
      newName = re.sub('THE LEGACY LIVING AND REHABILITATION CENTER', 'LEGACY LIVING AND REHABILITATION CENTER', newName)
      newName = re.sub('WESTON COUNTY HEALTH SERVICES', 'WESTON COUNTY MANOR', newName)
      
      return newName