# -*- coding: utf-8 -*-
import re

def normalize_cms_LA(newName):
      # print('state to be normalized: ', state)
      print('passed in facility name: ', newName)
      #LA
      newName = re.sub('ACADIA ST. LANDRY GUEST HOUSE', 'ACADIA ST. LANDRY GUEST HOME', newName)
      newName = re.sub('AVALON PLACE', 'AVALON PLACE NURSING HOME', newName)
      newName = re.sub('BATON ROUGE GEN MED CENTER, SNF', 'BATON ROUGE GENERAL MEDICAL CENTER, SNF', newName)
      newName = re.sub('BAYOU VISTA COMMUNITY CARE CENTER', 'BAYOU VISTA COMMUNITY CARE', newName)
      newName = re.sub('BELLE MAISON NURSING AND REHABILITATION', 'BELLE MAISON NURSING AND REHABILITATION CENTER', newName)
      newName = re.sub('BOOKER T.WASHINGTON SKILLED NURSING AND REHABILITA', 'BOOKER T. WASHINGTON SKILLED NURSING AND REHABILITATION', newName)
      newName = re.sub('CAMELOT LEISURE LIVING', 'CAMELOT LEISURE AND LIVING', newName)
      newName = re.sub('CHATEAU LIVING CENTER', 'CHATEAU LIVING CENTER OF KENNER', newName)
      newName = re.sub('CHATEAU TERREBONNE HEALTH CARE', 'CHATEAU TERREBONNE', newName)
      newName = re.sub('CHERRY RIDGE', 'CHERRY RIDGE SKILLED NURSING FACILITY', newName)
      newName = re.sub('CHRISTWOOD', 'CHRISTWOOD- SKILLED CARE', newName)
      newName = re.sub('CONSOLATA HOME', 'CONSOLATA NURSING HOME', newName)
      newName = re.sub('COURTYARD MANOR NURSE CARE CENTER AND ASSISTED LIV', 'COURTYARD MANOR NURSE CARE CENTER AND ASSISTED LIVING', newName)
      newName = re.sub('COVENANT HOME', 'COVENANT NURSING HOME', newName)
      newName = re.sub('GRACE NURSING HOME', 'GRACE HEALTH AND REHABILITATION', newName)
      newName = re.sub('GARDENS AND GUARDIAN', 'GARDENS AND GUARDIAN HOUSE', newName)
      newName = re.sub('GUEST HOUSE SKILLED NURSING REHABILITATION', 'GUEST HOUSE SKILLED NURSING AND REHABILITATION', newName)
      newName = re.sub('HERITAGE MANOR HEALTH AND REHABILITATION', 'HERITAGE MANOR HEALTH AND REHABILITATION CENTER', newName)
      newName = re.sub('HERITAGE MANOR OF BATON ROUGE I I', 'HERITAGE MANOR OF BATON ROUGE', newName)
      newName = re.sub('HERITAGE MANOR OF STRATMORE NURSING AND REHABILITATION CENTER', 'HERITAGE MANOR STRATMORE NURSING AND REHABILITATION CENTER', newName)
      newName = re.sub('JEFFERSON MANOR NURSING AND RE', 'JEFFERSON MANOR NURSING AND REHABILITATION CENTER', newName)
      newName = re.sub('JO ELLEN SMITH CONVALESCENT CENTER', 'JO ELLEN SMITH LIVING CENTER', newName)
      newName = re.sub('JOHN J HAINKEL JR HOME AND REHABILITATION CENTER', 'JOHN J. HAINKEL JR HOME AND REHABILITATION CENTER', newName)
      newName = re.sub('LAFOURCHE HOME FOR AGED AND INFIRM', 'LAFOURCHE HOME FOR THE AGED', newName)
      newName = re.sub('LANDMARK NURSING AND REHABILITATION CENTER', 'LANDMARK NURSING AND REHABILITATION CENTER OF WEST MONROE', newName)
      newName = re.sub('LANDMARK NURSING CENTER HAMMOND', 'LANDMARK NURSING CENTER IN HAMMOND', newName)
      newName = re.sub('LANDMARK OF ACADIANA', 'LANDMARK OF ACADIANA NURSING HOME', newName)
      newName = re.sub('LEGRAND HEALTHCARE AND REHABILITATION CENTER', 'LEGRAND HEALTHCARE AND REHABILITATION', newName)
      newName = re.sub('LIVE OAK', 'LIVE OAKS RETIREMENT COMMUNITY', newName)
      newName = re.sub('LOUISIANA WAR VETERANS HOME', 'LOUISIANA WAR VETERANS\' HOME', newName)
      newName = re.sub('MAISON DE\'VILLE NURSING HOME OF HARVEY', 'MAISON DE\'VILLE OF HARVEY', newName)
      newName = re.sub('MAISON DE\'VILLE NURSING HOME', 'MAISON DEVILLE HOUMA', newName)
      newName = re.sub('MAISON DU MONDE LIVING CENTER', 'MAISON DU MONDE', newName)
      newName = re.sub('MAISON ORLEANS HEALTHCARE OF NEW ORLEANS', 'MAISON ORLEANS (UPTOWN HEALTHCARE CENTER)', newName)
      newName = re.sub('MANY HEALTHCARE AND REHABILITATION CENTER', 'MANY HEALTHCARE CENTER', newName)
      newName = re.sub('MARRERO HEALTHCARE CENTER', 'MARRERO HEALTH CARE CENTER', newName)
      newName = re.sub('MATTHEWS MEMORIAL HEALTH CARE CENTER', 'MATTHEWS MEMORIAL HEALTH CARE IN ALEXANDRIA', newName)
      newName = re.sub('MEADOWVIEW HEALTH AND REHABILITATION CENTER', 'MEADOWVIEW HEALTH AND REHABILITATION', newName)
      newName = re.sub('METAIRIE HEALTH CARE CENTER', 'METAIRIE HEALTHCARE', newName)
      newName = re.sub('NAOMI HEIGHTS NURSING AND REHABILITATION CENTER', 'NAOMI HEIGHT NURSING AND REHABILITATION', newName)
      newName = re.sub('NATCHITOCHES NURSING AND REHABILITATION CENTER,LLC', 'NATCHITOCHES NURSING AND REHABILITATION CENTER', newName)
      newName = re.sub('NORTHEAST LA WAR VETERANS HOME', 'NORTHEAST LOUISIANA WAR VETERANS HOME', newName)
      # newName = re.sub('NORTHEAST LOUISIANA WAR VETERANS HOME', 'NORTHWEST LOUISIANA VETERANS HOME', newName)
      newName = re.sub('OCHSNER MEDICAL CENTER SKILLED NURSING FACILITY', 'OCHSNER MEDICAL CENTER SKILLED NURSING FACILITY (SNF)', newName)
      newName = re.sub('OLLIE STEELE BURDEN MANOR', 'OLLIE STEELE BURDEN MANOR NURSING HOME', newName)
      newName = re.sub('OUR LADY OF PROMPT SUCCOR NURSING FACILITY', 'OUR LADY OF PROMPT SUCCOR NURSING HOME', newName)
      newName = re.sub('PRINCETON PLACE-RUSTON', 'PRINCETON PLACE - RUSTON', newName)
      newName = re.sub('RIVER PALMS NURSING AND REHABILITATION', 'RIVER PALM NURSING AND REHABILITATION', newName)
      newName = re.sub('RIVERVIEW CARE CENTER', 'RIVERVIEW CARE CENTER BOSSIER CITY SENIOR LIVING', newName)
      newName = re.sub('RUSTON NURSING AND REHABILITATION CENTER,LLC', 'RUSTON NURSING AND REHABILITATION', newName)
      newName = re.sub('SAGE REHABILITATION HOSPITAL SNF', 'SAGE REHABILITATION HOSPITAL (SNF)', newName)
      newName = re.sub('SOUTHEAST LOUISIANA WAR VETERANS\' HOME', 'SOUTHEAST LOUISIANA WAR VETERANS HOME', newName)
      newName = re.sub('SOUTHWEST LOUISIANA WAR VETERANS\' HOME', 'SOUTHWEST LOUISIANA WAR VETERANS HOME', newName)
      newName = re.sub('SOUTHWIND NURSING AND REHABILITATION CENTER', 'SOUTHWIND HEALTHCARE AND REHABILITATION', newName)
      newName = re.sub('ST AGNES HEALTHCARE AND REHABILITATION CENTER', 'ST. AGNES HEALTHCARE AND REHABILITATION CENTER', newName)
      newName = re.sub('ST ANTHONY\'S NURSING HOME', 'ST. ANTHONY\'S NURSING HOME', newName)
      newName = re.sub('ST CHRISTINA NURSING AND REHABILITATION CENTER', 'ST. CHRISTINA NURSING AND REHABILITATION CENTER', newName)
      newName = re.sub('ST CLARE MANOR', 'ST. CLARE MANOR NURSING HOME', newName)
      newName = re.sub('ST FRANCES NURSING AND REHABILITATION CENTER', 'ST. FRANCES NURSING AND REHABILITATION CENTER', newName)
      newName = re.sub('ST FRANCISVILLE COUNTRY MANOR', 'ST. FRANCISVILLE COUNTRY MANOR', newName)
      newName = re.sub('ST HELENA PARISH NURSING HOME', 'ST. HELENA PARISH NURSING HOME', newName)
      newName = re.sub('ST JAMES PLACE NURSING CARE CENTER', 'ST. JAMES PLACE RETIREMENT COMMUNITY', newName)
      newName = re.sub('ST JOSEPH OF HARAHAN', 'ST. JOSEPH OF HARAHAN', newName)
      newName = re.sub('ST JUDE\'S NURSING HOME', 'ST. JUDE\'S NURSING HOME', newName)
      newName = re.sub('ST LUKE\'S LIVING CENTER', 'ST. LUKE\'S LIVING CENTER', newName)
      newName = re.sub('ST MARGARET\'S DAUGHTERS HOME', 'ST. MARGARET\'S AT MERCY NURSING HOME', newName)
      newName = re.sub('ST MARTIN DE PORRES MULTI-CARE CENTER', 'ST. MARTIN DE PORRES', newName)
      newName = re.sub('STERLING PLACE', 'STERLING PLACE NURSING HOME', newName)
      newName = re.sub('TERREBONNE GENERAL MED CENTER SNF', 'TERREBONNE GENERAL MEDICAL CENTER - SNF', newName)
      newName = re.sub('TWIN OAKS NURSING HOME', 'TWIN OAKS NURSING', newName)
      newName = re.sub('VALLEY VIEW HEALTH CARE FACILITY', 'VALLEY VIEW HEALTHCARE', newName)
      newName = re.sub('VILLA FELICIANA CHRONIC DISEASE', 'VILLA FELICIANA CHRONIC DISEASE HOSPITAL AND REHABILITATION - SNF', newName)
      newName = re.sub('WEST JEFFERSON HEALTH CARE CENTER', 'WEST JEFFERSON HEALTHCARE', newName)
      newName = re.sub('WILLOW RIDGE NURSING AND REHABILITATION CENTER,LLC', 'WILLOW RIDGE NURSING HOME', newName)
      newName = re.sub('WILLOW WOOD AT WOLDENBERG VILLAGE', 'WILLOW WOOD AT WOLDENBERG SKILLED NURSING FACILITY', newName)
      newName = re.sub('WINNFIELD NURSING AND REHABILITATION CENTER', 'WINNFIELD NURSING AND REHABILITATION', newName)
      newName = re.sub('WOODLEIGH OF BATON ROUGE', 'WOODLEIGH OF BATON ROUGE SENIOR LIVING', newName)
      newName = re.sub('WOODS HAVEN SR CITIZENS HOME', 'WOODS HAVEN NURSING CARE AND REHABILITATION', newName)


      return newName