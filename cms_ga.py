# -*- coding: utf-8 -*-
import re

def normalize_cms_GA(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      #GA
      newName = re.sub('NANCY HART CENTER FOR NURSING AND HEALING', 'NANCY HART NURSING CENTER', newName)

      return newName