# -*- coding: utf-8 -*-
import re

def normalize_ID(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # ID
      newNameAlt = re.sub('ADVANCED HEALTH CARE OF COEUR D’ALENE', 'ADVANCED HEALTH CARE OF COEUR D\'ALENE', newNameAlt)
      newNameAlt = re.sub('BEAR LAKE MANOR', 'BEAR LAKE MEMORIAL SKILLED NURSING FACILITY', newNameAlt)
      newNameAlt = re.sub('GOOD SAMARITAN – IDAHO FALLS VILLAGE', 'GOOD SAMARITAN SOCIETY - IDAHO FALLS VILLAGE', newNameAlt)
      newNameAlt = re.sub('LIFE CARE CENTER OF COEUR D’ALENE', 'LIFE CARE CENTER OF COEUR D\'ALENE', newNameAlt)
      newNameAlt = re.sub('RIVER’S EDGE REHABILITATION', 'RIVER\'S EDGE REHABILITATION', newNameAlt)
      
      newNameAlt = re.sub('STATE VETERANS HOME - BOISE', 'IDAHO STATE VETERANS HOME - BOISE', newNameAlt)
      newNameAlt = re.sub('STATE VETERANS HOME - LEWISTON', 'IDAHO STATE VETERANS HOME - LEWISTON', newNameAlt)
      newNameAlt = re.sub('STATE VETERANS HOME – POCATELLO', 'IDAHO STATE VETERANS HOME - POCATELLO', newNameAlt)
           

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt