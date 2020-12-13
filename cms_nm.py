# -*- coding: utf-8 -*-
import re

def normalize_cms_NM(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      # NM
      newName = re.sub('BEAR CANYON REHABILITATION CENTER', 'BEAR CANYON', newName)
      newName = re.sub('BELEN MEADOWS HEALTHCARE AND REHABILITATION CENTER', 'BELEN MEADOWS', newName)
      newName = re.sub('CASA DEL SOL CENTER', 'CASA DEL SOL CENTER, LAS CRUCES', newName)
      newName = re.sub('CASA MARIA HEALTHCARE CENTER AND PECOS VALLEY REHA', 'CASA MARIA HEALTHCARE CENTER AND PECOS VALLEY REHABILITATION', newName)
      newName = re.sub('COLFAX GENERAL LTC', 'COLFAX LONG TERM CARE CENTER', newName)
      newName = re.sub('GOOD SAMARITAN SOCIETY LAS CRUCES VILLAGE', 'GOOD SAMARITAN SOCIETY - LAS CRUCES', newName)
      newName = re.sub('LAGUNA RAINBOW NURSING CENTER', 'LAGUNA RAINBOW CARE', newName)
      newName = re.sub('LAS PALOMAS CENTER', 'LAS PALOMAS GENESIS', newName)
      newName = re.sub('MISSION ARCH CENTER', 'MISSION ARCH CENTER (ROSWELL)', newName)
      newName = re.sub('NEIGHBORHOOD IN RIO RANCHO', 'NEIGHBORHOOD IN RIO RANCHO, HEALTH CARE', newName)
      newName = re.sub('RIO RANCHO CENTER', 'GENESIS RIO RANCHO CENTER', newName)
      newName = re.sub('SANDIA RIDGE CENTER', 'SANDIA RIDGE GENESIS', newName)
      newName = re.sub('SAN JUAN CENTER', 'GENESIS SAN JUAN CENTER, FARMINGTON', newName)
      newName = re.sub('SILVER CITY CARE CENTER', 'GENESIS SILVER CITY CARE CENTER, SILVER CITY', newName)
      newName = re.sub('SOUTH VALLEY CARE CENTER', 'SOUTH VALLEY CARE CENTER, ALBUQUERQUE', newName)
      newName = re.sub('SUNSET VILLA CARE CENTER', 'SUNSET VILLA NURSING HOME', newName)
      newName = re.sub('VILLAGE AT NORTHRISE \(THE\) - DESERT WILLOW I', 'VILLAGE AT NORTHRISE', newName)
      
      return newName