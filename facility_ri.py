# -*- coding: utf-8 -*-
import re

def normalize_RI(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # RI
      # this is to strip the '(locality)' appended to each facility list name string
      newNameAltSplit = newNameAlt.split('(')
      newNameAlt = newNameAltSplit[0]

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt