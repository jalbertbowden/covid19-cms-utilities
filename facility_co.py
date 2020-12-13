# -*- coding: utf-8 -*-
import re

def normalize_CO(newNameAlt):
      # print('passed in facility name: ', newNameAlt)

      # CO
      newNameAlt = re.sub('REHABILITATION CENTER AT SANDALWOOD,THE', 'REHABILITATION CENTER AT SANDALWOOD', newNameAlt)
      newNameAlt = re.sub ('THE SUITES PARKER', 'SUITES PARKER', newNameAlt)
      newNameAlt = re.sub ('SUITES PARKER, THE ', 'SUITES PARKER', newNameAlt)
      newNameAlt = re.sub('CENTER AT CENTERPLACE, THE ', 'CENTER AT CENTERPLACE', newNameAlt)
      # newNameAlt = re.sub('GRACE POINTE CONT CARE SR CAMPUS, SKILLED NURSING ', 'GRACE POINTE CONTINUING CARE SENIOR CAMPUS, SKILLED NURSING ', newNameAlt)
      newNameAlt = re.sub('GRACE POINTE CONT CARE SR CAMPUS, SKILLED NURSING ', 'GRACE POINTE CONTINUING CARE SENIOR CAMPUS, SKILLED NURSING', newNameAlt)
      
      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt