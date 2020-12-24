# -*- coding: utf-8 -*-
import cms_ak
import cms_al
import cms_ar
import cms_az
import cms_ca
import cms_co
import cms_ct
import cms_dc
import cms_de
import cms_fl
import cms_ga
import cms_gu
import cms_hi
import cms_ia
import cms_id
import cms_il
import cms_in
import cms_ks
import cms_ky
import cms_la
import cms_ma
import cms_md
import cms_me
import cms_mi
import cms_mn
import cms_mo
import cms_ms
import cms_mt
import cms_nc
import cms_nd
import cms_ne
import cms_nh
import cms_nj
import cms_nm
import cms_nv
import cms_ny
import cms_oh
import cms_ok
import cms_or
import cms_pa
import cms_pr
import cms_ri
import cms_sc 
import cms_sd
import cms_tn
import cms_tx
import cms_ut
import cms_va
import cms_vt
import cms_wa
import cms_wi
import cms_wv
import cms_wy

def normalize_cms_state(state, newName):
      # print('state to be normalized: ', state)
      # print('passed in facility name: ', newName)
      if state == 'AK':
            # print('state matches: ', state)
            newName = cms_ak.normalize_cms_AK(newName)
      elif state == 'AL':
            # print('state matches: ', state)
            newName = cms_al.normalize_cms_AL(newName)
      elif state == 'AR':
            # print('state matches: ', state)
            newName = cms_ar.normalize_cms_AR(newName)
      elif state == 'AZ':
            # print('state matches: ', state)
            newName = cms_az.normalize_cms_AZ(newName)
      elif state == 'CA':
            # print('state matches: ', state)
            newName = cms_ca.normalize_cms_CA(newName)
      elif state == 'CO':
            # print('state matches: ', state)
            newName = cms_co.normalize_cms_CO(newName)
      elif state == 'CT':
            # print('state matches: ', state)
            newName = cms_ct.normalize_cms_CT(newName)
      elif state == 'DC':
            # print('state matches: ', state)
            newName = cms_dc.normalize_cms_DC(newName)
      elif state == 'DE':
            # print('state matches: ', state)
            newName = cms_de.normalize_cms_DE(newName)
      elif state == 'FL':
            # print('state matches: ', state)
            newName = cms_fl.normalize_cms_FL(newName)
      elif state == 'GA':
            # print('state matches: ', state)
            newName = cms_ga.normalize_cms_GA(newName)
      elif state == 'GU':
            # print('state matches: ', state)
            newName = cms_gu.normalize_cms_GU(newName)
      elif state == 'HI':
            # print('state matches: ', state)
            newName = cms_hi.normalize_cms_HI(newName)
      elif state == 'IA':
            # print('state matches: ', state)
            newName = cms_ia.normalize_cms_IA(newName)
      elif state == 'ID':
            # print('state matches: ', state)
            newName = cms_id.normalize_cms_ID(newName)
      elif state == 'IL':
            # print('state matches: ', state)
            newName = cms_il.normalize_cms_IL(newName)
      elif state == 'IN':
            # print('state matches: ', state)
            newName = cms_in.normalize_cms_IN(newName)
      elif state == 'KS':
            # print('state matches: ', state)
            newName = cms_ks.normalize_cms_KS(newName)
      elif state == 'KY':
            # print('state matches: ', state)
            newName = cms_ky.normalize_cms_KY(newName)
      elif state == 'LA':
            # print('state matches: ', state)
            newName = cms_la.normalize_cms_LA(newName)
      elif state == 'MA':
            # print('state matches: ', state)
            newName = cms_ma.normalize_cms_MA(newName)
      elif state == 'MD':
            # print('state matches: ', state)
            newName = cms_md.normalize_cms_MD(newName)
      elif state == 'ME':
            # print('state matches: ', state)
            newName = cms_me.normalize_cms_ME(newName)
      elif state == 'MI':
            # print('state matches: ', state)
            newName = cms_mi.normalize_cms_MI(newName)
      elif state == 'MN':
            # print('state matches: ', state)
            newName = cms_mn.normalize_cms_MN(newName)
      elif state == 'MO':
            # print('state matches: ', state)
            newName = cms_mo.normalize_cms_MO(newName)
      elif state == 'MS':
            # print('state matches: ', state)
            newName = cms_ms.normalize_cms_MS(newName)
      elif state == 'MT':
            # print('state matches: ', state)
            newName = cms_mt.normalize_cms_MT(newName)
      elif state == 'NC':
            # print('state matches: ', state)
            newName = cms_nc.normalize_cms_NC(newName)
      elif state == 'ND':
            # print('state matches: ', state)
            newName = cms_nd.normalize_cms_ND(newName)
      elif state == 'NE':
            # print('state matches: ', state)
            newName = cms_ne.normalize_cms_NE(newName)
      elif state == 'NH':
            # print('state matches: ', state)
            newName = cms_nh.normalize_cms_NH(newName)
      elif state == 'NJ':
            # print('state matches: ', state)
            newName = cms_nj.normalize_cms_NJ(newName)
      elif state == 'NM':
            # print('state matches: ', state)
            newName = cms_nm.normalize_cms_NM(newName)
      elif state == 'NV':
            # print('state matches: ', state)
            newName = cms_nv.normalize_cms_NV(newName)
      elif state == 'NY':
            # print('state matches: ', state)
            newName = cms_ny.normalize_cms_NY(newName)
      elif state == 'OH':
            # print('state matches: ', state)
            newName = cms_oh.normalize_cms_OH(newName)
      elif state == 'OK':
            # print('state matches: ', state)
            newName = cms_ok.normalize_cms_OK(newName)
      elif state == 'OR':
            # print('state matches: ', state)
            newName = cms_or.normalize_cms_OR(newName)
      elif state == 'PA':
            # print('state matches: ', state)
            newName = cms_pa.normalize_cms_PA(newName)
      elif state == 'PR':
            # print('state matches: ', state)
            newName = cms_pr.normalize_cms_PR(newName)
      elif state == 'RI':
            # print('state matches: ', state)
            newName = cms_ri.normalize_cms_RI(newName)
      elif state == 'SC':
            # print('state matches: ', state)
            newName = cms_sc.normalize_cms_SC(newName)
      elif state == 'SD':
            # print('state matches: ', state)
            newName = cms_sc.normalize_cms_SC(newName)
      elif state == 'TN':
            # print('state matches: ', state)
            newName = cms_tn.normalize_cms_TN(newName)
      elif state == 'TX':
            # print('state matches: ', state)
            newName = cms_tx.normalize_cms_TX(newName)
      elif state == 'UT':
            # print('state matches: ', state)
            newName = cms_ut.normalize_cms_UT(newName)
      elif state == 'VA':
            # print('state matches: ', state)
            newName = cms_va.normalize_cms_VA(newName)
      elif state == 'VT':
            # print('state matches: ', state)
            newName = cms_vt.normalize_cms_VT(newName)
      elif state == 'WA':
            # print('state matches: ', state)
            newName = cms_wa.normalize_cms_WA(newName)
      elif state == 'WI':
            # print('state matches: ', state)
            newName = cms_wi.normalize_cms_WI(newName)
      elif state == 'WV':
            # print('state matches: ', state)
            newName = cms_wv.normalize_cms_WV(newName)
      elif state == 'WY':
            # print('state matches: ', state)
            newName = cms_wy.normalize_cms_WY(newName)
      else:
            print('state does not match: ', state)

      return newName