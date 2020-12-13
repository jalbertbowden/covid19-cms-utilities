# -*- coding: utf-8 -*-
import re

def normalize_NM(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # NM
      newNameAlt = re.sub('BLOOMFIELD NURSING AND REHABILITATION CENTER, BLOOMFIELD', 'BLOOMFIELD NURSING AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('CASA ARENA BLANCA NURSING CENTER, ALAMOGORDO', 'CASA ARENA BLANCA NURSING CENTER', newNameAlt)
      newNameAlt = re.sub('CASA DE ORO CENTER, LAS CRUCES', 'CASA DE ORO CENTER', newNameAlt)
      newNameAlt = re.sub('CASA MARIA, ROSWELL', 'CASA MARIA HEALTHCARE CENTER AND PECOS VALLEY REHABILITATION', newNameAlt)
      newNameAlt = re.sub('CLOVIS HEALTHCARE AND REHABILITATION CLOVIS', 'CLOVIS HEALTHCARE AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('GOOD SAMARITAN, LAS CRUCES', 'GOOD SAMARITAN SOCIETY - LAS CRUCES', newNameAlt)
      newNameAlt = re.sub('MISSION ARCH CENTER (ROSWELL)', 'MISSION ARCH CENTER', newNameAlt)
      newNameAlt = re.sub('RATON NURSING AND REHABILITATION CENTER, RATON', 'RATON NURSING AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('RETIREMENT RANCHES-CLOVIS', 'RETIREMENT RANCHES', newNameAlt)
      newNameAlt = re.sub('SANDIA RIDGE GENESIS, ALBUQUERQUE', 'SANDIA RIDGE GENESIS', newNameAlt)
      newNameAlt = re.sub('SUNSET VILLA NURSING HOME, ROSWELL', 'SUNSET VILLA NURSING HOME', newNameAlt)
      newNameAlt = re.sub('VILLAGE AT NORTHRISE, LAS CRUCES', 'VILLAGE AT NORTHRISE', newNameAlt)
      newNameAlt = re.sub('WHITE SANDS HEALTHCARE, HOBBS', 'WHITE SANDS HEALTHCARE', newNameAlt)

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt