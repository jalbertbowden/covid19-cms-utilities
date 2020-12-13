# -*- coding: utf-8 -*-
import re

def normalize_cms_IA(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      #IA
      newName = re.sub('GLEN HAVEN HOME', 'GLEN HAVEN VILLAGE', newName)
      newName = re.sub('GRANDVIEW HEALTHCARE CENTER', 'GRANDVIEW HEALTH CARE', newName)
      newName = re.sub('EVENTIDE LUTHERAN HOME FOR', 'EVENTIDE LUTHERAN HOME', newName)
      newName = re.sub('HARMONY HOUSE HEALTH CARE CENT', 'HARMONY HOUSE HEALTH CARE HOME', newName)
      newName = re.sub('HEGG MEMORIAL HEALTH CENTER', 'HEGG MEMORIAL HEALTH CENTER HSP-NF', newName)
      newName = re.sub('KAHL HOME FOR THE AGED AND INFIRMED', 'KAHL HOME', newName)
      newName = re.sub('MANORCARE HEALTH SERVICES -WEST DES MOINES', 'MANORCARE HEALTH SERVICES - WEST DES MOINES', newName)
      newName = re.sub('MERCYONE DYSERVILLE SENIOR CARE HSF-NSF', 'MERCYONE DYSERVILLE SENIOR CARE HSF-NSF', newName)
      newName = re.sub('MERCYONE DYSERVILLE SENIOR CARE', 'MERCYONE DYSERVILLE SENIOR CARE HSF-NSF', newName)
      newName = re.sub('MERCYONE DYERSVILLE SENIOR CARE', 'MERCYONE DYERSVILLE SENIOR CARE HSF-NSF', newName)
      newName = re.sub('NEW HAMPTON NURSING AND REHABILITATION CE', 'NEW HAMPTON NURSING AND REHABILITATION CENTER', newName)
      # newName = re.sub('PINNACLE SPECIALTY CARE', 'PINNACLE SPECIALITY CARE', newName)
      newName = re.sub('RIVER HILLS VILLAGE IN KEOKUK', 'RIVER HILLS VILLAGE', newName)

      return newName