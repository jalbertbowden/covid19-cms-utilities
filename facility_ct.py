# -*- coding: utf-8 -*-
import re

def normalize_CT(newNameAlt):
      # print('passed in facility name: ', newNameAlt)

      # CT
      newNameAlt = re.sub('THREE RIVERS HEALTHCARE*', 'THREE RIVERS HEALTHCARE', newNameAlt)
      newNameAlt = re.sub('HARBOR VILLAGE', 'HARBOR VILLAGE NORTH HEALTH AND REHABILITATION CENTER', newNameAlt)

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt