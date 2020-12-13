# -*- coding: utf-8 -*-
import re

def normalize_NJ(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # NJ
      # SOMERSET WOODS REHABILITATION AND NURSING CENTER §
      newNameAlt = re.sub('ALARIS AT CASTLE HILL', 'ALARIS HEALTH AT CASTLE HILL', newNameAlt)
      newNameAlt = re.sub('ARISTCARE AT WHITING', 'ARISTACARE AT WHITING', newNameAlt)
      newNameAlt = re.sub('CAREONE AT EVESHAM AL', 'CARE ONE AT EVESHAM', newNameAlt)
      newNameAlt = re.sub('CAREONE AT VALLEY', 'CARE ONE AT VALLEY', newNameAlt)
      newNameAlt = re.sub('CAREONE AT MOORESTOWN', 'CARE ONE AT MOORESTOWN', newNameAlt)
      newNameAlt = re.sub('CHESTNUT HILL RESIDENCE', 'CHESTNUT HILL CONVALESCENT CENTER', newNameAlt)
      newNameAlt = re.sub('INGLEMOOR REHABILITATION AND CARE CENTER OF LIIVNGSTON', 'INGLEMOOR REHABILITATION AND CARE CENTER OF LIVINGSTON', newNameAlt)
      newNameAlt = re.sub('MANORCARE VOORHEES', 'MANOR CARE HEALTH SERVICES - VOORHEES', newNameAlt)
      newNameAlt = re.sub('MAPLE GLEN CENTER \(GENESIS HEALTH CARE\)', 'MAPLE GLEN CENTER', newNameAlt)
      newNameAlt = re.sub('MERIDIAN NURSING AND REHABILITATION AR BRICK', 'MERIDIAN NURSING AND REHABILITATION AT BRICK', newNameAlt)
      newNameAlt = re.sub('ANDOVER SUBACUTE AND REHABILITATION II', 'ANDOVER SUBACUTE AND REHABILITATION CENTER II', newNameAlt)

      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt