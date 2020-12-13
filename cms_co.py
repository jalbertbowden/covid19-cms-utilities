# -*- coding: utf-8 -*-
import re

def normalize_cms_CO(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      


      # CO
      newName = re.sub('BELMONT LODGE HEALTH CARE CENTER', 'BELMONT LODGE HEALTHCARE CENTER', newName)
      # newName = re.sub('GRACE POINTE CONT CARE SR CAMPUS, SKILLED NURSING', 'GRACE POINTE CONTINUING CARE SENIOR CAMPUS, SKILLED NURSING', newName)
      newName = re.sub('GRACE POINTE CONT CARE SR CAMPUS, SKILLED NURSING', 'GRACE POINTE CONTINUING CARE SENIOR CAMPUS ASSISTED LIVING', newName)
      newName = re.sub('MANORCARE HEALTH SERVICES-DENVER', 'MANORCARE HEALTH SERVICES - DENVER', newName)
      newName = re.sub('FRASIER MEADOWS HEALTH CARE CENTER', 'FRASIER MEADOWS', newName)
      newName = re.sub('SUITES AT HOLLY CREEK CARE CENTER', 'SUITES AT HOLLY CREEK ASSISTED LIVING', newName)
      newName = re.sub('SUITES AT SOMEREN GLEN CARE CENTER', 'THE SUITES AT SOMEREN GLEN CARE CENTER', newName)
      newName = re.sub('VI AT HIGHLANDS RANCH SKILLED NURSING', 'VI AT HIGHLANDS RANCH', newName)


      return newName