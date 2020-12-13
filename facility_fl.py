# -*- coding: utf-8 -*-
import re

def normalize_FL(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # FL
      newNameAlt = re.sub('WILLOWBROOKE COURT SKILLED CARE CENTER- EDGEWATER AT BOCA POINTE', 'WILLOWBROOKE COURT SKILLED CARE CENTER - EDGEWATER AT BOCA POINTE', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HEALTH CARE CENTER-FT MYERS', 'HEARTLAND HEALTH CARE CENTER - FT MYERS', newNameAlt)
      newNameAlt = re.sub('REHABILITATION CENTER OF THE PALM BEACHES,THE', 'REHABILITATION CENTER OF THE PALM BEACHES', newNameAlt)
      newNameAlt = re.sub('BISHOP\'S GLEN RETIREMENT CENTER', 'BISHOPS GLEN RETIREMENT CENTER', newNameAlt)
      


      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt