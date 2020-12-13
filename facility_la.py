# -*- coding: utf-8 -*-
import re

def normalize_LA(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # LA
      # LANDMARK OF PLAQUEMINE*
      newNameAlt = re.sub('HARMONY HOUSE NURSING AND REHABILITATION CENTER.', 'HARMONY HOUSE NURSING AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('LANDMARK OF PLAQUEMINE*', 'LANDMARK OF PLAQUEMINE', newNameAlt)
      newNameAlt = re.sub('SOUTHERN OAKS NURSING AND REHABILITATION CENTER.', 'SOUTHERN OAKS NURSING AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('TERREBONNE GEN. MED. CENTER - SNF', 'TERREBONNE GENERAL MEDICAL CENTER - SNF', newNameAlt)
      
      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt