# -*- coding: utf-8 -*-
import re

def normalize_AR(newNameAlt):
      # print('passed in facility name: ', newNameAlt)

      # AR

      newNameAlt = re.sub(' OF UNION CO$', ' OF UNION COUNTY', newNameAlt)
      newNameAlt = re.sub('GOOD SAMARITAN SOCIETY-HOT SPRINGS VILLAGE', 'GOOD SAMARITAN SOCIETY - HOT SPRINGS VILLAGE', newNameAlt)
      # newNameALt = re.sub('HIGHLAND COURT A REHABILITATION AND RESIDENT CARE FACILITY', 'XXXHIGHLAND COURT, A REHABILITATION AND RESIDENT CARE', newNameAlt)
      newNameAlt = re.sub('MONTGOMERY CO NURSING HOME', 'MONTGOMERY COUNTY NURSING HOME', newNameAlt)
      newNameAlt = re.sub('RANDOLPH CO NURSING HOME', 'RANDOLPH COUNTY NURSING HOME', newNameAlt)
      newNameAlt = re.sub('WALNUT RIDGE N AND R', 'WALNUT RIDGE NURSING AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('ARKANSAS NURSING AND REHABILITATION', 'ARKANSAS NURSING AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('B RIARWOOD NURSING AND REHABILITATION CENTER', 'BRIARWOOD NURSING AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('CONWAY HEALTHCARE AND REHABILITATION', 'CONWAY HEALTHCARE AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('G ENERAL BAPTIST NURSING HOME OF PIGGOTT', 'GENERAL BAPTIST NURSING HOME OF PIGGOTT', newNameAlt)
      newNameAlt = re.sub('GREENHOUSE COTTAGES OF POPLAR GROVE', 'THE GREEN HOUSE COTTAGES OF POPLAR GROVE', newNameAlt)
      newNameAlt = re.sub('HEATHER MANOR REHABILITATION', 'HEATHER MANOR NURSING AND REHABILITATION CENTER', newNameAlt)
      newNameAlt = re.sub('MIDTOWN POST ACUTE AND REHABILITATION-A WATERS COMMUNITY', 'MIDTOWN POST ACUTE AND REHABILITATION - A WATERS COMMUNITY', newNameAlt)
      newNameAlt = re.sub('N URSING AND REHABILITATION CENTER AT GOOD SHEPHERD', 'NURSING AND REHABILITATION CENTER AT GOOD SHEPHERD', newNameAlt)
      newNameAlt = re.sub('O AK RIDGE HEALTH AND REHABILITATION', 'OAK RIDGE HEALTH AND REHABILITATION', newNameAlt)
      newNameAlt = re.sub('SOMERSET SENIOR LIVING AT MOUNT VISTA/MOUNT VISTA R AND H CENTER', 'SOMERSET SENIOR LIVING AT MOUNT VISTA', newNameAlt)
      newNameAlt = re.sub('THE GREENHOUSE COTTAGES OF BELLE MEADE', 'THE GREEN HOUSE COTTAGES OF BELLE MEADE', newNameAlt)

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt