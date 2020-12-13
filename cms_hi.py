# -*- coding: utf-8 -*-
import re

def normalize_cms_HI(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      #HI
      newName = re.sub('ANN PEARL NURSING FACILITY', 'ANN PEARL REHABILITATION AND HEALTHCARE', newName)
      newName = re.sub('AVALON CARE CENTER - HONOLULU', 'AVALON CARE CENTER', newName)
      newName = re.sub('CLARENCE TC CHING VILLAS AT ST FRANCIS', 'CLARENCE TC CHING VILLAS', newName)
      newName = re.sub('HALE ANUENUE RESTORATIVE CARE', 'HALE ANUENUE RESTORATIVE CARE CENTER', newName)
      newName = re.sub('HALE NANI REHABILITATION AND NURSING CENTER', 'HALE NANI', newName)
      newName = re.sub('LILIHA HEALTHCARE CENTER', 'LILIHA HEALTH CARE CENTER', newName)
      newName = re.sub('HI\'OLANI CARE CENTER AT KAHALA NUI', 'HI’OLANI CARE CENTER AT KAHALA NUI', newName)
      newName = re.sub('YUKIO OKUTSU STATE VETERANS HOME', 'YUKIO OKUTSU VETERANS STATE HOME', newName)


      return newName