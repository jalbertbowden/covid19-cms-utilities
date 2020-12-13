# -*- coding: utf-8 -*-
import re

def normalize_cms_DC(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      # DC
      newName = re.sub('BRIDGEPOINT SUB-ACUTE AND REHABILITATION CAPITOL HILL', 'BRIDGEPOINT CAPITOL HILL', newName)
      newName = re.sub('BRIDGEPOINT SUBACUTE AND REHABILITATION NATIONAL HARBOR', 'BRIDGEPOINT NATIONAL HARBOR', newName)
      newName = re.sub('CARROLL MANOR NURSING AND REHABILITATION', 'CARROLL MANOR', newName)
      newName = re.sub('DEANWOOD REHABILITATION AND WELLNESS CENTER', 'DEANWOOD', newName)
      newName = re.sub('FOREST HILLS OF DC', 'FOREST HILLS', newName)
      newName = re.sub('INGLESIDE AT ROCK CREEK', 'INGLESIDE', newName)
      newName = re.sub('INSPIRE REHABILITATION AND HEALTH CENTER', 'INSPIRE', newName)
      newName = re.sub('JEANNE JUGAN RESIDENCE', 'JEANNE JUGAN LITTLE SISTERS OF THE POOR', newName)
      newName = re.sub('KNOLLWOOD HSC', 'KNOLLWOOD', newName)
      newName = re.sub('LISNER LOUISE DICKSON HURTHOME', 'LISNER HOME', newName)
      newName = re.sub('SERENITY REHABILITATION AND HEALTH CENTER', 'SERENITY', newName)
      newName = re.sub('STODDARD BAPTIST NURSING HOME', 'STODDARD BAPTIST', newName)
      # newName = re.sub('', 'THOMAS CIRCLE', newName)
      newName = re.sub('TRANSITIONS HEALTHCARE CAPITOL CITY', 'TRANSITIONS', newName)
      newName = re.sub('UNITED MEDICAL NURSING HOME', 'UMNC', newName)
      newName = re.sub('UNIQUE REHABILITATION AND HEALTH CENTER', 'UNIQUE', newName)
      newName = re.sub('WASHINGTON CENTER FOR AGING SVCS', 'WASHINGTON CENTER FOR AGING SERVICES', newName)



      return newName