# -*- coding: utf-8 -*-
import re

def normalize_KS(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      #KS
      # this is to strip the '( - MONTH YEAR)' appended to each facility list name string
      newNameAltSplit = newNameAlt.split('-')
      print('1: ', newNameAltSplit[0])
      # print('2: ', newNameAltSplit[1])
      newNameAlt = newNameAltSplit[0]
      newNameAlt = re.sub('PLAZE WEST HEALTHCARE AND REHABILITATION CENTER', 'PLAZA WEST HEALTHCARE AND REHABILITATION', newNameAlt)
      newNameAlt = re.sub('ROSSVILLE HEALTHCARE AND REHAV', 'ROSSVILLE HEALTHCARE AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('TOPEKA PREBYTERIAN MANOR', 'TOPEKA PRESBYTERIAN MANOR', newNameAlt)



      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt