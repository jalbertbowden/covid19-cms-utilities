# -*- coding: utf-8 -*-
import re

def normalize_KY(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # KY 
      newNameAlt = re.sub('LEE COUNTY CARE AND REHABILITATION', 'LEE COUNTY CARE AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('SPRINGFIELD NURSING AND REHABILITATION', 'SPRINGFIELD NURSING AND REHABILITATION CENTER', newNameAlt)

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt