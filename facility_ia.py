# -*- coding: utf-8 -*-
import re

def normalize_IA(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # IA
      newNameAlt = re.sub('DENVER SUNSE HOME', 'DENVER SUNSET HOME', newNameAlt)
      newNameAlt = re.sub('DUNLAP SPECIALITY CARE', 'DUNLAP SPECIALTY CARE', newNameAlt)
      newNameAlt = re.sub('PANORA SPECIALITY CARE', 'PANORA SPECIALTY CARE', newNameAlt)
      newNameAlt = re.sub('PRARIE VIEW HOME', 'PRAIRIE VIEW HOME', newNameAlt)
      newNameAlt = re.sub('PREMIER ESTATES FO MUSCATINE', 'PREMIER ESTATES OF MUSCATINE', newNameAlt)
      newNameAlt = re.sub('PREMIER ESTATES SENIOR LIFE CENTER', 'PREMIER ESTATES OF MUSCATINE', newNameAlt)
      newNameAlt = re.sub('RAVENWOOD SPECIALTY', 'RAVENWOOD SPECIALTY CARE', newNameAlt)

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt