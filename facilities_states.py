# -*- coding: utf-8 -*-
import facility_ak
import facility_al
import facility_ar
import facility_az
import facility_ca
import facility_co
import facility_ct
import facility_dc
import facility_de
import facility_fl
import facility_ga
import facility_gu
import facility_hi
import facility_ia
import facility_id
import facility_il
import facility_in
import facility_ks
import facility_ky
import facility_la
import facility_ma
import facility_md
import facility_me
import facility_mi
import facility_mn
import facility_mo
import facility_ms
import facility_mt
import facility_nc
import facility_nd
import facility_ne
import facility_nh
import facility_nj
import facility_nm
import facility_nv
import facility_ny
import facility_oh
import facility_ok
import facility_or
import facility_pa
import facility_pr
import facility_ri
import facility_sc 
import facility_sd
import facility_tn
import facility_tx
import facility_ut
import facility_va
import facility_vt
import facility_wa
import facility_wi
import facility_wv
import facility_wy


# ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 
# 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 
# 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
def normalize_state(state, newNameAlt):
      print('state to be normalized: ', state)
      print('passed in facility name: ', newNameAlt)
      if state == 'AK':
            print('state matches: ', state)
            newNameAlt = facility_ak.normalize_AK(newNameAlt)
      elif state == 'AL':
            print('state matches: ', state)
            newNameAlt = facility_al.normalize_AL(newNameAlt)
      elif state == 'AR':
            print('state matches: ', state)
            newNameAlt = facility_ar.normalize_AR(newNameAlt)
      elif state == 'AZ':
            print('state matches: ', state)
            newNameAlt = facility_az.normalize_AZ(newNameAlt)
      elif state == 'CA':
            print('state matches: ', state)
            newNameAlt = facility_ca.normalize_CA(newNameAlt)
      elif state == 'CO':
            print('state matches: ', state)
            newNameAlt = facility_co.normalize_CO(newNameAlt)
      elif state == 'CT':
            print('state matches: ', state)
            newNameAlt = facility_ct.normalize_CT(newNameAlt)
      elif state == 'DC':
            print('state matches: ', state)
            newNameAlt = facility_dc.normalize_DC(newNameAlt)
      elif state == 'DE':
            print('state matches: ', state)
            newNameAlt = facility_de.normalize_DE(newNameAlt)
      elif state == 'FL':
            print('state matches: ', state)
            newNameAlt = facility_fl.normalize_FL(newNameAlt)
      elif state == 'GA':
            print('state matches: ', state)
            newNameAlt = facility_ga.normalize_GA(newNameAlt)
      elif state == 'GU':
            print('state matches: ', state)
            newNameAlt = facility_gu.normalize_GA(newNameAlt)
      elif state == 'HI':
            print('state matches: ', state)
            newNameAlt = facility_hi.normalize_HI(newNameAlt)
      elif state == 'IA':
            print('state matches: ', state)
            newNameAlt = facility_ia.normalize_IA(newNameAlt)
      elif state == 'ID':
            print('state matches: ', state)
            newNameAlt = facility_id.normalize_ID(newNameAlt)
      elif state == 'IL':
            print('state matches: ', state)
            newNameAlt = facility_il.normalize_IL(newNameAlt)
      elif state == 'IN':
            print('state matches: ', state)
            newNameAlt = facility_in.normalize_IN(newNameAlt)
      elif state == 'KS':
            print('state matches: ', state)
            newNameAlt = facility_ks.normalize_KS(newNameAlt)
      elif state == 'KY':
            print('state matches: ', state)
            newNameAlt = facility_ky.normalize_KY(newNameAlt)
      elif state == 'LA':
            print('state matches: ', state)
            newNameAlt = facility_la.normalize_LA(newNameAlt)
      elif state == 'MA':
            print('state matches: ', state)
            newNameAlt = facility_ma.normalize_MA(newNameAlt)
      elif state == 'MD':
            print('state matches: ', state)
            newNameAlt = facility_md.normalize_MD(newNameAlt)
      elif state == 'ME':
            print('state matches: ', state)
            newNameAlt = facility_me.normalize_ME(newNameAlt)
      elif state == 'MI':
            print('state matches: ', state)
            newNameAlt = facility_mi.normalize_MI(newNameAlt)
      elif state == 'MN':
            print('state matches: ', state)
            newNameAlt = facility_mn.normalize_MN(newNameAlt)
      elif state == 'MO':
            print('state matches: ', state)
            newNameAlt = facility_mo.normalize_MO(newNameAlt)
      elif state == 'MS':
            print('state matches: ', state)
            newNameAlt = facility_ms.normalize_MS(newNameAlt)
      elif state == 'MT':
            print('state matches: ', state)
            newNameAlt = facility_mt.normalize_MT(newNameAlt)
      elif state == 'NC':
            print('state matches: ', state)
            newNameAlt = facility_nc.normalize_NC(newNameAlt)
      elif state == 'ND':
            print('state matches: ', state)
            newNameAlt = facility_nd.normalize_ND(newNameAlt)
      elif state == 'NE':
            print('state matches: ', state)
            newNameAlt = facility_ne.normalize_NE(newNameAlt)
      elif state == 'NH':
            print('state matches: ', state)
            newNameAlt = facility_nh.normalize_NH(newNameAlt)
      elif state == 'NJ':
            print('state matches: ', state)
            newNameAlt = facility_nj.normalize_NJ(newNameAlt)
      elif state == 'NM':
            print('state matches: ', state)
            newNameAlt = facility_nm.normalize_NM(newNameAlt)
      elif state == 'NV':
            print('state matches: ', state)
            newNameAlt = facility_nv.normalize_NV(newNameAlt)
      elif state == 'NY':
            print('state matches: ', state)
            newNameAlt = facility_ny.normalize_NY(newNameAlt)
      elif state == 'OH':
            print('state matches: ', state)
            newNameAlt = facility_oh.normalize_OH(newNameAlt)
      elif state == 'OK':
            print('state matches: ', state)
            newNameAlt = facility_ok.normalize_OK(newNameAlt)
      elif state == 'OR':
            print('state matches: ', state)
            newNameAlt = facility_or.normalize_OR(newNameAlt)
      elif state == 'PA':
            print('state matches: ', state)
            newNameAlt = facility_pa.normalize_PA(newNameAlt)
      elif state == 'PR':
            print('state matches: ', state)
            newNameAlt = facility_pr.normalize_PR(newNameAlt)
      elif state == 'RI':
            print('state matches: ', state)
            newNameAlt = facility_ri.normalize_RI(newNameAlt)
      elif state == 'SC':
            print('state matches: ', state)
            newNameAlt = facility_sc.normalize_SC(newNameAlt)
      elif state == 'SD':
            print('state matches: ', state)
            newNameAlt = facility_sc.normalize_SC(newNameAlt)
      elif state == 'TN':
            print('state matches: ', state)
            newNameAlt = facility_tn.normalize_TN(newNameAlt)
      elif state == 'TX':
            print('state matches: ', state)
            newNameAlt = facility_tx.normalize_TX(newNameAlt)
      elif state == 'UT':
            print('state matches: ', state)
            newNameAlt = facility_ut.normalize_UT(newNameAlt)
      elif state == 'VA':
            print('state matches: ', state)
            newNameAlt = facility_va.normalize_VA(newNameAlt)
      elif state == 'VT':
            print('state matches: ', state)
            newNameAlt = facility_vt.normalize_VT(newNameAlt)
      elif state == 'WA':
            print('state matches: ', state)
            newNameAlt = facility_wa.normalize_WA(newNameAlt)
      elif state == 'WI':
            print('state matches: ', state)
            newNameAlt = facility_wi.normalize_WI(newNameAlt)
      elif state == 'WV':
            print('state matches: ', state)
            newNameAlt = facility_wv.normalize_WV(newNameAlt)
      elif state == 'WY':
            print('state matches: ', state)
            newNameAlt = facility_wy.normalize_WY(newNameAlt)
      else:
            print('state does not match: ', state)

      print('this is dumb')

      return newNameAlt