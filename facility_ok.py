# -*- coding: utf-8 -*-
import re

def normalize_OK(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # OK
      newNameAlt = re.sub('QUAIL RIDGE LIVING CENTER \(COLCORD, OK\)', 'QUAIL RIDGE LIVING CENTER', newNameAlt)
      
      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt