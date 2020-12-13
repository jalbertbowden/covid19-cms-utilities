# -*- coding: utf-8 -*-
import re

def normalize_WY(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # WY
      newNameAlt = re.sub('GOSHEN HEALTHCARE', 'GOSHEN HEALTHCARE COMMUNITY', newNameAlt)
      newNameAlt = re.sub('LIFECARE OF CASPER', 'LIFE CARE CENTER OF CASPER', newNameAlt)
      newNameAlt = re.sub('LIFECARE OF CHEYENNE', 'LIFE CARE CENTER OF CHEYENNE', newNameAlt)
      newNameAlt = re.sub('NEW HORIZAONS CARE CENTER', 'NEW HORIZONS CARE CENTER', newNameAlt)
      newNameAlt = re.sub('SHEPHERD OF THE VALLEY', 'SHEPHERD OF THE VALLEY REHABILITION AND WELLNESS', newNameAlt)

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt