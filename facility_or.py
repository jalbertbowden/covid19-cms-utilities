# -*- coding: utf-8 -*-
import re

def normalize_OR(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # OR
      newNameAlt = re.sub('DALLAS RETIREMENT VILLAGE', 'DALLAS RETIREMENT VILLAGE HEALTH CENTER', newNameAlt)
      newNameAlt = re.sub('FRENCH PRAIRIE NURSING AND REHABILITATION', 'FRENCH PRAIRIE NURSING AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('LIFE CARE REHABILITATION', 'LIFE CARE CENTER OF MCMINNVILLE', newNameAlt)
      newNameAlt = re.sub('MARQUIS CENTENNIAL', 'MARQUIS CENTENNIAL POST ACUTE REHABILITATION', newNameAlt)
      newNameAlt = re.sub('PRESTIGE CARE MILWAUKIE', 'PRESTIGE POST-ACUTE AND REHABILITATION CENTER - MILWAUKIE', newNameAlt)
      newNameAlt = re.sub('REGENCY HERMISTON', 'REGENCY HERMISTON NURSING AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('REGENCY REDMOND', 'REGENCY REDMOND REHABILITATION AND NURSING CENTER', newNameAlt)
      newNameAlt = re.sub('REGENCY VILLAGE PRINEVILLE', 'REGENCY PRINEVILLE REHABILITATION AND NURSING CENTER', newNameAlt)
      newNameAlt = re.sub('ROSE VILLA', 'ROSE VILLA SENIOR LIVING COMMUNITY', newNameAlt)
      newNameAlt = re.sub('WINDSOR HEALTH AND REHABILITATION', 'WINDSOR HEALTH AND REHABILITATION CENTER', newNameAlt)
      

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt