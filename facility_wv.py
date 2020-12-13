# -*- coding: utf-8 -*-
import re

def normalize_WV(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # WV
      newNameAlt = re.sub('NELLAS NURSING HOME', 'NELLA\'S NURSING HOME', newNameAlt)
      newNameAlt = re.sub('MONTGOMERY GENERAL HOSPITAL \(SKILLED NURSING\)', 'MONTGOMERY GENERAL HOSPITAL', newNameAlt)

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt