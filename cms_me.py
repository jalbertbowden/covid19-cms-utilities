# -*- coding: utf-8 -*-
import re

def normalize_cms_ME(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      # ME
      newName = re.sub('CLOVER MANOR', 'CLOVER HEALTH CARE', newName)
      newName = re.sub('MAPLECREST REHABILITATION AND LIVING CENTER', 'MAPLECREST REHABILITATION CENTER', newName)
      newName = re.sub('PINNACLE HEALTH AND REHABILITATION AT SANFORD', 'PINNACLE HEALTH CARE AND REHABILITATION OF SANFORD', newName)
      newName = re.sub('SEAL ROCK HEALTH CARE', 'SEAL ROCK HEALTHCARE', newName)
      newName = re.sub('THE COMMONS AT TALL PINES', 'TALL PINES', newName)
      newName = re.sub('CEDARS NURSING CARE CENTER', 'THE CEDARS ASSISTED LIVING', newName)

      return newName