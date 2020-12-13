# -*- coding: utf-8 -*-
import re

def normalize_cms_KS(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      # KS
      
      newName = re.sub('ABERDEEN VILLAGE', 'ABERDEEN VILLAGE ASSISTED LIVING', newName)
      newName = re.sub('ROLLING HILLS HEALTH AND REHABILITATION', 'ROLLING HILLS HEALTHCARE AND REHABILITATION', newName)
      newName = re.sub('ST LUKE LIVING CENTER', 'ST. LUKE LIVING CENTER', newName)
      newName = re.sub('LEGACY ON 10TH AVENUE', 'THE LEGACY ON 10TH AVENUE', newName)


      return newName