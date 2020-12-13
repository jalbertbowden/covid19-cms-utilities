# -*- coding: utf-8 -*-
import re

def normalize_GA(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # GA
      # GRACEWOOD NSG FACILITY(UNIT 9)
      # newNameAlt = re.sub('WASHINGTON CO EXTENDED CARE FA', 'WASHINGTON CO EXTENDED CARE FACILITY', newNameAlt)
      
      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt