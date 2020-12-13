# -*- coding: utf-8 -*-
import re

def normalize_MI(newNameAlt):
      # print('passed in facility name: ', newNameAlt)
      # MI
      # THE OASIS AT MONROE REHABILITATION AND NUR
      # OCEANA CO MD CARE FACILITY
      # IRON CO MEDICAL CARE FACILITY
      # HILLSDALE CO MEDICAL CARE FACILITY
      # HALLMARK LIVING--BENTON HARBOR
      newNameAlt = re.sub('ADVANTAGE LIVING CENTER HARPER WOODS', 'ADVANTAGE LIVING CENTER - HARPER WOODS', newNameAlt)
      newNameAlt = re.sub('ADVANTAGE LIVING CENTER NORTHWEST', 'ADVANTAGE LIVING CENTER - NORTHWEST', newNameAlt)
      newNameAlt = re.sub('ADVANTAGE LIVING CENTER REDFORD', 'ADVANTAGE LIVING CENTER - REDFORD', newNameAlt)
      newNameAlt = re.sub('ADVANTAGE LIVING CENTER SOUTHGATE', 'ADVANTAGE LIVING CENTER - SOUTHGATE', newNameAlt)
      newNameAlt = re.sub('ADVANTAGE LIVING CENTER WAYNE', 'ADVANTAGE LIVING CENTER - WAYNE', newNameAlt)
      newNameAlt = re.sub('AERIUS HEALTH CENTER ', 'AERIUS HEALTH CENTER', newNameAlt)
      newNameAlt = re.sub('BEAUMONT REHABILITATION AND CONTINUING CARE - DBN', 'BEAUMONT REHABILITATION AND CONTINUING CARE - DEARBORN', newNameAlt)
      newNameAlt = re.sub('BEAUMONT REHABILITATION AND CONTINUING CARE FARMING', 'BEAUMONT REHABILITATION AND CONTINUING CARE - FARMINGTON HILLS', newNameAlt)
      newNameAlt = re.sub('CAMBRIDGE NORTH HEALTHCARE CENTER ', 'CAMBRIDGE NORTH HEALTHCARE CENTER', newNameAlt)
      newNameAlt = re.sub('CHIPPEWA COUNTY WAR MEM HOSPITAL LTCU', 'CHIPPEWA COUNTY WAR MEMORIAL HOSPITAL LTCU', newNameAlt)
      newNameAlt = re.sub('GOGEBIC MEDICAL CARE FACILITY ', 'GOGEBIC MEDICAL CARE FACILITY', newNameAlt)
      newNameAlt = re.sub('HALLMARK LIVING--BENTON HARBOR', 'HALLMARK LIVING BENTON HARBOR', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HCC - ANN ARBOR', 'HEARTLAND HEALTH CARE CENTER - ANN ARBOR', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HCC - BATTLE CREEK', 'HEARTLAND HEALTH CARE CENTER - BATTLE CREEK', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HCC - GROSSE POINTE WOODS', 'HEARTLAND HEALTH CARE CENTER - GROSSE POINT WOODS', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HCC - HAMPTON', 'HEARTLAND HEALTH CARE CENTER - HAMPTON', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HCC BRIARWOOD', 'HEARTLAND HEALTH CARE CENTER - BRIARWOOD', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HCC FOSTRIAN', 'HEARTLAND HEALTH CARE CENTER - FOSTRIAN', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HEALTH CARE CENTER - THREE RIV', 'HEARTLAND HEALTH CARE CENTER - THREE RIVERS', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HEALTH CARE CENTER ALLEN PARK', 'HEARTLAND HEALTH CARE CENTER - ALLEN PARK', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HEALTH CARE CENTER-LIVONIA', 'HEARTLAND HEALTH CARE CENTER - LIVONIA', newNameAlt)
      newNameAlt = re.sub('HEARTLAND HEALTHCARE - STERLING HEIGHTS', 'HEARTLAND HEALTH CARE CENTER - STERLING HEIGHTS', newNameAlt)
      newNameAlt = re.sub('HENRY FORD VILLAGE $', 'HENRY FORD VILLAGE', newNameAlt)
      newNameAlt = re.sub('JACKSON COUNTY MEDICAL CARE FACILITY ', 'JACKSON COUNTY MEDICAL CARE FACILITY', newNameAlt)
      newNameAlt = re.sub('LENAWEE MEDICAL CARE FACILITY ', 'LENAWEE MEDICAL CARE FACILITY', newNameAlt)
      newNameAlt = re.sub('LIFE CARE CENTER OF PLAINWELL ', 'LIFE CARE CENTER OF PLAINWELL', newNameAlt)
      newNameAlt = re.sub('LOURDES REHABILITATION AND HEALTHCARE ', 'LOURDES REHABILITATION AND HEALTHCARE', newNameAlt)
      newNameAlt = re.sub('MARVIN AND BETTY DANTO FAMILY HEALTH CARE ', 'MARVIN AND BETTY DANTO FAMILY HEALTH CARE', newNameAlt)
      newNameAlt = re.sub('MEADOW BROOK MCF', 'MEADOW BROOK MEDICAL CARE FACILITY', newNameAlt)
      newNameAlt = re.sub('MEDILODGE ALPENA', 'MEDILODGE OF ALPENA', newNameAlt)
      newNameAlt = re.sub('MEDILODGE OF CHEBOYGAN ', 'MEDILODGE OF CHEBOYGAN', newNameAlt)
      newNameAlt = re.sub('MEDILODGE OF PLYMOUTH ', 'MEDILODGE OF PLYMOUTH', newNameAlt)
      newNameAlt = re.sub('MEDILODGE OF PORT HURON ', 'MEDILODGE OF PORT HURON', newNameAlt)
      newNameAlt = re.sub('MUNSON HEALTH CRAWFORD CONTINUING CARE ', 'MUNSON HEALTH CRAWFORD CONTINUING CARE', newNameAlt)
      newNameAlt = re.sub('PLAINWELL PINES NURSING AND REHAB.', 'PLAINWELL PINES NURSING AND REHAB', newNameAlt)
      newNameAlt = re.sub('REGENCY A VILLA CENTER ', 'REGENCY A VILLA CENTER', newNameAlt)
      newNameAlt = re.sub('SAMARITAS  SENIOR LIVING SAGINAW', 'SAMARITAS SENIOR LIVING SAGINAW', newNameAlt)
      newNameAlt = re.sub('SKLD LIVONIA ', 'SKLD - LIVONIA', newNameAlt)
      newNameAlt = re.sub('SKLD BELTLINE', 'SKLD - BELTLINE', newNameAlt)
      newNameAlt = re.sub('SKLD IONIA', 'SKLD - IONIA', newNameAlt)
      newNameAlt = re.sub('SKLD LEONARD', 'SKLD - LEONARD', newNameAlt)
      newNameAlt = re.sub('SKLD MUSKEGON', 'SKLD - MUSKEGON', newNameAlt)
      newNameAlt = re.sub('SKLD PLYMOUTH', 'SKLD - PLYMOUTH', newNameAlt)
      newNameAlt = re.sub('SKLD WHITEHALL', 'SKLD - WHITEHALL', newNameAlt)
      newNameAlt = re.sub('SKLD WYOMING', 'SKLD - WYOMING', newNameAlt)
      newNameAlt = re.sub('SKLD ZEELAND', 'SKLD - ZEELAND', newNameAlt)
      newNameAlt = re.sub('SPECENTERUM HEALTH REHABILITATION AND NURSING FULLER', 'SPECENTERUM HEALTH REHABILITATION AND NURSING - FULLER', newNameAlt)
      newNameAlt = re.sub('SPECENTERUM HEALTH RNC - KELSEY HOSPITAL', 'SPECENTERUM HEALTH REHABILITATION AND NURSING CENTER - KELSEY HOSPITAL', newNameAlt)
      newNameAlt = re.sub('SPECENTERUM HEALTH RNC - UNITED HOSPITAL', 'SPECENTERUM HEALTH REHABILITATION AND NURSING CENTER - UNITED HOSPITAL', newNameAlt)
      newNameAlt = re.sub('STRATFORD PINES ', 'STRATFORD PINES', newNameAlt)
      newNameAlt = re.sub('THE OASIS AT MONROE REHABILITATION AND NUR', 'THE OASIS AT MONROE REHABILITATION AND NURSING CENTER', newNameAlt)
      newNameAlt = re.sub('THE RIVERS HEALTH AND REHABILITATION CENTER OF GROSSE PT', 'THE RIVERS HEALTH AND REHABILITATION CENTER OF GROSSE POINTE', newNameAlt)
      newNameAlt = re.sub('THE WILLOWS AT HOWELL ', 'THE WILLOWS AT HOWELL', newNameAlt)
      newNameAlt = re.sub('TUSCOLA COUNT MEDICAL CARE COMMUNITY ', 'TUSCOLA COUNTY MEDICAL CARE FACILITY', newNameAlt)
      newNameAlt = re.sub('VILLA AT ROSE CITY ', 'THE VILLA AT ROSE CITY', newNameAlt)
      newNameAlt = re.sub('VILLA AT SILVERBELL ESTATE', 'THE VILLA AT SILVERBELL ESTATES', newNameAlt)
      newNameAlt = re.sub('VILLA AT WEST BRANCH', 'THE VILLA AT WEST BRANCH', newNameAlt)
      # newNameAlt = re.sub('WELLBRIDGE OF GRAND BLANC ', 'WELLBRIDGE OF GRAND BLANC', newNameAlt)
      newNameAlt = re.sub('WELLBRIDGE OF PINCKNEY ', 'WELLBRIDGE OF PINCKNEY', newNameAlt)
      newNameAlt = re.sub('WOODHAVEN RETIREMENT COMMUNITY ', 'WOODHAVEN RETIREMENT COMMUNITY', newNameAlt)

      
      # print('moduled normalized new name alt: ', newNameAlt)

      return newNameAlt