# -*- coding: utf-8 -*-
import re

def normalize_DC(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # DC
      # newNameAlt = re.sub('', '', newNameAlt)
      newNameAltSplit = newNameAlt.split('(')
      # this is to strip the '(bedroom values)' appended to each facility list name string
      print('1: ', newNameAltSplit[0])
      print('2: ', newNameAltSplit[1])

      newNameAlt = newNameAltSplit[0]


      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt