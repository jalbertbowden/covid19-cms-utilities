# -*- coding: utf-8 -*-
import re

def normalize_ND(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # ND
      newNameAlt = re.sub('MAPLE VIEW MEMORY CARE- BISMARCK', 'MAPLE VIEW MEMORY CARE - BISMARCK', newNameAlt)
      newNameAlt = re.sub('MCKENZIE COUNTY-GOOD SHEPHERD LONG TERM CARE', 'MCKENZIE COUNTY - GOOD SHEPHERD LONG TERM CARE', newNameAlt)
      newNameAlt = re.sub('PEAK RESOURCES ', 'PEAK RESOURCES - ', newNameAlt)
      # newNameAlt = re.sub('EVENTIDE$', 'EVENTIDE FARGO', newNameAlt)
      # newNameAlt = re.sub('EVENTIDE DOWNTOWN','', newNameAlt)
      newNameAlt = re.sub('EVENTIDE JAMESTOWN','EVENTIDE JAMESTOWN ASSISTED LIVING', newNameAlt)
      newNameAlt = re.sub('EVENTIDE SHEYENNE CROSSINGS','EVENTIDE SHEYENNE CROSSINGS ASSISTED LIVING', newNameAlt)
      newNameAlt = re.sub('GOOD SAM, LAKOTA', 'GOOD SAMARITAN SOCIETY - LAKOTA', newNameAlt)
      newNameAlt = re.sub('GOOD SAMARITAN BOTTINEAU', 'GOOD SAMARITAN SOCIETY - BOTTINEAU', newNameAlt)
      newNameAlt = re.sub('GOOD SAMARITAN FARGO', 'GOOD SAMARITAN SOCIETY - FARGO', newNameAlt)
      newNameAlt = re.sub('GOOD SAMARITAN LAKOTA','GOOD SAMARITAN SOCIETY - LAKOTA', newNameAlt)
      newNameAlt = re.sub('GOOD SAMARITAN MOHALL', 'GOOD SAMARITAN SOCIETY - MOHALL', newNameAlt)
      # newNameAlt = re.sub('GOOD SAMARITAN MOTT', 'GOOD SAMARITAN SOCIETY - MOTT', newNameAlt)
      newNameAlt = re.sub('GOOD SAM MOTT', 'GOOD SAMARITAN SOCIETY - MOTT', newNameAlt)
      newNameAlt = re.sub('GOOD SAMARITAN OAKES', 'GOOD SAMARITAN SOCIETY - OAKES', newNameAlt)
      newNameAlt = re.sub('GOOD SAMARITAN PARK RIVER', 'GOOD SAMARITAN SOCIETY - PARK RIVER', newNameAlt)
      # newNameAlt = re.sub('HEART OF AMERICA', 'HEART OF AMERICA CARE CENTER', newNameAlt)
      newNameAlt = re.sub('MCKENZIE COUNTY HEALTH-GOOD SHEPHERD','MCKENZIE COUNTY - GOOD SHEPHERD LONG TERM CARE', newNameAlt)
      

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt