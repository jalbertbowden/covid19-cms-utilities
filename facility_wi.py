# -*- coding: utf-8 -*-
import re

def normalize_WI(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # WI
      newNameAlt = re.sub('\*BENEDICTINE MANOR', 'BENEDICTINE MANOR', newNameAlt)
      newNameAlt = re.sub('\*LAKELAND HEALTH CARE CENTER', 'LAKELAND HEALTH CARE CENTER', newNameAlt)
      newNameAlt = re.sub('\*MANITOWOC HEALTH AND REHABILITATION CENTER', 'MANITOWOC HEALTH AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('\*MASONIC CENTER FOR HEALTH AND REHABILITATION', 'MASONIC CENTER FOR HEALTH AND REHABILITATION', newNameAlt)
      newNameAlt = re.sub('AUGUSTA HEALTH AND REHAILITATION', 'AUGUSTA HEALTH AND REHABILITATION', newNameAlt)

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt