import os
import re
import csv
import talib
import numpy as np
inputs = {
    'open': np.random.random(100),
    'high': np.random.random(100),
    'low': np.random.random(100),
    'close': np.random.random(100),
    'volume': np.random.random(100)
}
#print (inputs)
for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)
        if filename.startswith( 'eggs' ) & filename.endswith('.csv'):
            m = re.search('eggs(?P<key1>\w+)-(?P<key2>\w+).csv', filename)
            if m is None:
                continue
            key1= None
            key2= None
            if m is not None:
                key1=m.group('key1')
                key2=m.group('key2')
            
            print('key1'+key1)
            print('key2'+key2)
            print(filename)
            if 1==1 :
                newListOfData=[]
                resorted={'open': [],'high': [],'low': [], 'close': [],'volume':[],'time':[]}
                with open(filename, newline='') as csvfile:
                        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                        for row in spamreader:
                            if len(row)==6 :
                                newListOfData.append({'open': float(row[1]),'high': float(row[4]),'low': float(row[3]), 'close': float(row[2]),'volume':float(row[5]),'time':row[0]})
                
                filecsv='interval-'+key1+"-"+key2+".csv"
                listLong = []
                listShort = []
            
                with open(filecsv, newline='') as csvfile:
                        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                        for row in spamreader:
                            listLong.append(row[1])
                            listShort.append(row[2])
                            if len(listLong) >10*len(newListOfData)/100.0 :
                                listLong.pop(0)
                                listShort.pop(0)
                        listLong=set(listLong)
                        listShort=set(listShort)

                newListOfData=sorted(newListOfData, key=lambda student: float(student['time']))
                for row in newListOfData:
                    resorted['open'].append(row['open'])
                    resorted['high'].append(row['high'])
                    resorted['low'].append(row['low'])
                    resorted['close'].append(row['close'])
                    resorted['volume'].append(row['volume'])
                    resorted['time'].append(row['time'])
                
                resorted={'open': np.array(resorted['open'])
                            ,'high': np.array(resorted['high'])
                            ,'low': np.array(resorted['low'])
                            , 'close': np.array(resorted['close'])
                            ,'volume':np.array(resorted['volume'])
                            ,'time':np.array(resorted['time'])}
                
                ##Classic
                bb_upperband, bb_middleband, bb_lowerband =talib.BBANDS(resorted['close'])
                dema_real = talib.DEMA(resorted['close'])
                ema_real = talib.EMA(resorted['close'])
                httrend_real = talib.HT_TRENDLINE(resorted['close'])
                kama_real = talib.KAMA(resorted['close'])
                ma_real = talib.MA(resorted['close'])
                mama_real,fama_real = talib.MAMA(resorted['close'])
                #mavp_real = talib.MAVP(resorted['close'])
                midpoint_real = talib.MIDPOINT(resorted['close'])
                midprice_real = talib.MIDPRICE(resorted['high'],resorted['low'])
                sar_real = talib.SAR(resorted['high'],resorted['low'])
                sarext_real = talib.SAREXT(resorted['high'],resorted['low'])
                sma_real = talib.SMA(resorted['close'])
                t3_real = talib.T3(resorted['close'])
                tema_real = talib.TEMA(resorted['close'])
                trima_real = talib.TRIMA(resorted['close'])
                wma_real = talib.WMA(resorted['close'])

                ##Momentum
                adx_real = talib.ADX(resorted['high'], resorted['low'], resorted['close'])
                adxrx_real = talib.ADXR(resorted['high'], resorted['low'], resorted['close'])
                apo_real = talib.APO(resorted['close'])
                aroondown_real,aroonup_real = talib.AROON(resorted['high'], resorted['low'])
                aroonosc_real = talib.AROONOSC(resorted['high'], resorted['low'])
                bop_real = talib.BOP(resorted['open'], resorted['high'], resorted['low'], resorted['close'])
                cci_real = talib.CCI(resorted['high'], resorted['low'], resorted['close'])
                cmo_real = talib.CMO(resorted['close'])
                dx_real = talib.DX(resorted['high'], resorted['low'], resorted['close'])
                macd_real, macdsignal_real, macdhist_real = talib.MACD(resorted['close'])
                macdext_real, macdsignalext_real, macdhistext_real = talib.MACDEXT(resorted['close'])
                macdfix_real, macdsignalfix_real, macdhistfix_real = talib.MACDFIX(resorted['close'])
                mfi_real = talib.MFI( resorted['high'], resorted['low'], resorted['close'], resorted['volume'])
                minus_di_real = talib.MINUS_DI(resorted['high'], resorted['low'], resorted['close'])
                minus_dm_real = talib.MINUS_DM(resorted['high'], resorted['low'])
                mom_real = talib.MOM(resorted['close'])
                plus_di_real = talib.PLUS_DI(resorted['high'], resorted['low'], resorted['close'])
                plus_dm_real = talib.PLUS_DM(resorted['high'], resorted['low'])
                ppo_real = talib.PPO(resorted['close'])
                roc_real = talib.ROC(resorted['close'])
                rocp_real = talib.ROCP(resorted['close'])
                rocr_real = talib.ROCR(resorted['close'])
                rocr100_real = talib.ROCR100(resorted['close'])
                rsi_real = talib.RSI(resorted['close'])
                slowk_real,slowd_real = talib.STOCH(resorted['high'], resorted['low'], resorted['close'])
                fastk_real,fastd_real = talib.STOCHF(resorted['high'], resorted['low'], resorted['close'])
                fastk_rsi_real,fastd_rsi_real = talib.STOCHRSI( resorted['close'])
                trix_real = talib.TRIX(resorted['close'])
                ultosc_real = talib.ULTOSC(resorted['high'], resorted['low'], resorted['close'])
                willr_real = talib.WILLR(resorted['high'], resorted['low'], resorted['close'])

                #Volume
                ad_real = talib.AD( resorted['high'], resorted['low'], resorted['close'], resorted['volume'])
                adosc_real = talib.ADOSC( resorted['high'], resorted['low'], resorted['close'], resorted['volume'])
                obv_real = talib.OBV(resorted['close'], resorted['volume'])

                #Volatility
                atr_real = talib.ATR(resorted['high'], resorted['low'], resorted['close'])
                natr_real = talib.NATR(resorted['high'], resorted['low'], resorted['close'])
                trange_real = talib.TRANGE(resorted['high'], resorted['low'], resorted['close'])

                #Price Transform
                avgprice_real = talib.AVGPRICE( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                medprice_real = talib.MEDPRICE(resorted['high'], resorted['low'])
                typprice_real = talib.TYPPRICE(resorted['high'], resorted['low'], resorted['close'])
                wlcprice_real = talib.WCLPRICE(resorted['high'], resorted['low'], resorted['close'])

                #Cycle Indicators
                ht_dcperiod_real = talib.HT_DCPERIOD(resorted['close'])
                ht_dcphase_real = talib.HT_DCPHASE(resorted['close'])
                inphase_real, quadrature_real = talib.HT_PHASOR(resorted['close'])
                sine_real, leadsine_real = talib.HT_SINE(resorted['close'])
                ht_trendmode_real = talib.HT_TRENDMODE(resorted['close'])

                #Pattern
                CDL2CROWS_real = talib.CDL2CROWS( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDL3BLACKCROWS_real = talib.CDL3BLACKCROWS( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDL3INSIDE_real = talib.CDL3INSIDE( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDL3LINESTRIKE_real = talib.CDL3LINESTRIKE( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDL3OUTSIDE_real = talib.CDL3OUTSIDE( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDL3STARSINSOUTH_real = talib.CDL3STARSINSOUTH( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDL3WHITESOLDIERS_real = talib.CDL3WHITESOLDIERS( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLABANDONEDBABY_real = talib.CDLABANDONEDBABY( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLADVANCEBLOCK_real = talib.CDLADVANCEBLOCK( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLBELTHOLD_real = talib.CDLBELTHOLD( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLBREAKAWAY_real = talib.CDLBREAKAWAY( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLCLOSINGMARUBOZU_real = talib.CDLCLOSINGMARUBOZU( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLCONCEALBABYSWALL_real = talib.CDLCONCEALBABYSWALL( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLCOUNTERATTACK_real = talib.CDLCOUNTERATTACK( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLDARKCLOUDCOVER_real = talib.CDLDARKCLOUDCOVER( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLDOJI_real = talib.CDLDOJI( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLDOJISTAR_real = talib.CDLDOJISTAR( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLDRAGONFLYDOJI_real = talib.CDLDRAGONFLYDOJI( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLENGULFING_real = talib.CDLENGULFING( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLEVENINGDOJISTAR_real = talib.CDLEVENINGDOJISTAR( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLEVENINGSTAR_real = talib.CDLEVENINGSTAR( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLGAPSIDESIDEWHITE_real = talib.CDLGAPSIDESIDEWHITE( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLGRAVESTONEDOJI_real = talib.CDLGRAVESTONEDOJI( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLHAMMER_real = talib.CDLHAMMER( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLHANGINGMAN_real = talib.CDLHANGINGMAN( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLHARAMI_real = talib.CDLHARAMI( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLHARAMICROSS_real = talib.CDLHARAMICROSS( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLHIGHWAVE_real = talib.CDLHIGHWAVE( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLHIKKAKE_real = talib.CDLHIKKAKE( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLHIKKAKEMOD_real = talib.CDLHIKKAKEMOD( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLHOMINGPIGEON_real = talib.CDLHOMINGPIGEON( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLIDENTICAL3CROWS_real = talib.CDLIDENTICAL3CROWS( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLINNECK_real = talib.CDLINNECK( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLINVERTEDHAMMER_real = talib.CDLINVERTEDHAMMER( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLKICKING_real = talib.CDLKICKING( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLKICKINGBYLENGTH_real = talib.CDLKICKINGBYLENGTH( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLLADDERBOTTOM_real = talib.CDLLADDERBOTTOM( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLLONGLEGGEDDOJI_real = talib.CDLLONGLEGGEDDOJI( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLLONGLINE_real = talib.CDLLONGLINE( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLMARUBOZU_real = talib.CDLMARUBOZU( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLMATCHINGLOW_real = talib.CDLMATCHINGLOW( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLMATHOLD_real = talib.CDLMATHOLD( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLMORNINGDOJISTAR_real = talib.CDLMORNINGDOJISTAR( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLMORNINGSTAR_real = talib.CDLMORNINGSTAR( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLONNECK_real = talib.CDLONNECK( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLPIERCING_real = talib.CDLPIERCING( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLRICKSHAWMAN_real = talib.CDLRICKSHAWMAN( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLRISEFALL3METHODS_real = talib.CDLRISEFALL3METHODS( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLSEPARATINGLINES_real = talib.CDLSEPARATINGLINES( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLSHOOTINGSTAR_real = talib.CDLSHOOTINGSTAR( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLSHORTLINE_real = talib.CDLSHORTLINE( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLSPINNINGTOP_real = talib.CDLSPINNINGTOP( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLSTALLEDPATTERN_real = talib.CDLSTALLEDPATTERN( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLSTICKSANDWICH_real = talib.CDLSTICKSANDWICH( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLTAKURI_real = talib.CDLTAKURI( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLTASUKIGAP_real = talib.CDLTASUKIGAP( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLTHRUSTING_real = talib.CDLTHRUSTING( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLTRISTAR_real = talib.CDLTRISTAR( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLUNIQUE3RIVER_real = talib.CDLUNIQUE3RIVER( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLUPSIDEGAP2CROWS_real = talib.CDLUPSIDEGAP2CROWS( resorted['open'],resorted['high'], resorted['low'], resorted['close'])
                CDLXSIDEGAP3METHODS_real = talib.CDLXSIDEGAP3METHODS( resorted['open'],resorted['high'], resorted['low'], resorted['close'])

                #stats
                beta_real = talib.BETA(resorted['high'], resorted['low'])
                correl_real = talib.CORREL(resorted['high'], resorted['low'])
                linearreg_real = talib.LINEARREG(resorted['close'])
                linearregang_real = talib.LINEARREG_ANGLE(resorted['close'])
                linearreginter_real = talib.LINEARREG_INTERCEPT(resorted['close'])
                linearregslope_real = talib.LINEARREG_SLOPE(resorted['close'])
                stdev_real = talib.STDDEV(resorted['close'])
                tsf_real = talib.TSF(resorted['close'])
                var_real = talib.VAR(resorted['close'])

                fileoutput='indicators-'+key1+"-"+key2+".csv"
                try:
                    os.remove(fileoutput)
                except:
                    print ('clean '+fileoutput)
                with open(fileoutput, 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    counter=0
                    for val in resorted['close']:
                        aval=[]
                        if counter+1 < len(resorted['time']) and (resorted['time'][counter+1] in listLong) :
                            aval.append(1)
                        else:
                            aval.append(0)
                        if counter+1 < len(resorted['time']) and (resorted['time'][counter+1] in listShort) :
                            aval.append(1)
                        else:
                            aval.append(0)
                        aval.append(resorted ['open'][counter])    
                        aval.append(resorted ['high'][counter])    
                        aval.append(resorted ['low'][counter])    
                        aval.append(resorted ['close'][counter])    
                        aval.append(resorted ['volume'][counter])    
                        aval.append(resorted ['time'][counter])    
                        aval.append(bb_upperband[counter])
                        aval.append(bb_middleband[counter])
                        aval.append(bb_lowerband[counter])
                        aval.append(dema_real[counter])
                        aval.append(ema_real[counter])
                        aval.append(httrend_real[counter])
                        aval.append(kama_real[counter])
                        aval.append(ma_real[counter])
                        aval.append(mama_real[counter])
                        aval.append(fama_real[counter])
                        aval.append(midpoint_real[counter])
                        aval.append(midprice_real[counter])
                        aval.append(sar_real[counter])
                        aval.append(sarext_real[counter])
                        aval.append(sma_real[counter])
                        aval.append(t3_real[counter])
                        aval.append(tema_real[counter])
                        aval.append(trima_real[counter])
                        aval.append(wma_real[counter])
                        aval.append(adx_real[counter])
                        aval.append(adxrx_real[counter])
                        aval.append(apo_real[counter])
                        aval.append(aroondown_real[counter])
                        aval.append(aroonup_real[counter])
                        aval.append(aroonosc_real[counter])
                        aval.append(bop_real[counter])
                        aval.append(cci_real[counter])
                        aval.append(cmo_real[counter])
                        aval.append(dx_real[counter])
                        aval.append(macd_real[counter])
                        aval.append(macdsignal_real[counter])
                        aval.append(macdhist_real[counter])
                        aval.append(macdext_real[counter])
                        aval.append(macdsignalext_real[counter])
                        aval.append(macdhistext_real[counter])
                        aval.append(macdfix_real[counter])
                        aval.append(macdsignalfix_real[counter])
                        aval.append(macdhistfix_real[counter])
                        aval.append(mfi_real[counter])
                        aval.append(minus_di_real[counter])
                        aval.append(minus_dm_real[counter])
                        aval.append(mom_real[counter])
                        aval.append(plus_di_real[counter])
                        aval.append(plus_dm_real[counter])
                        aval.append(ppo_real[counter])
                        aval.append(roc_real[counter])
                        aval.append(rocp_real[counter])
                        aval.append(rocr_real[counter])
                        aval.append(rocr100_real[counter])
                        aval.append(rsi_real[counter])
                        aval.append(slowk_real[counter])
                        aval.append(slowd_real[counter])
                        aval.append(fastk_real[counter])
                        aval.append(fastd_real[counter])
                        aval.append(fastk_rsi_real[counter])
                        aval.append(fastd_rsi_real[counter])
                        aval.append(trix_real[counter])
                        aval.append(ultosc_real[counter])
                        aval.append(willr_real[counter])
                        aval.append(ad_real[counter])
                        aval.append(adosc_real[counter])
                        aval.append(obv_real[counter])

                        #Volatility
                        aval.append(atr_real[counter])
                        aval.append(natr_real[counter])
                        aval.append(trange_real[counter])

                        #Price Transform
                        aval.append(avgprice_real[counter])
                        aval.append(medprice_real[counter])
                        aval.append(typprice_real[counter])
                        aval.append(wlcprice_real[counter])

                        #Cycle Indicators
                        aval.append(ht_dcperiod_real[counter])
                        aval.append(ht_dcphase_real[counter])
                        aval.append(inphase_real[counter])
                        aval.append(quadrature_real[counter])
                        aval.append(sine_real[counter])
                        aval.append(leadsine_real[counter])
                        aval.append(ht_trendmode_real[counter])

                        aval.append(CDL2CROWS_real[counter])
                        aval.append(CDL3BLACKCROWS_real[counter])
                        aval.append(CDL3INSIDE_real[counter])
                        aval.append(CDL3LINESTRIKE_real[counter])
                        aval.append(CDL3OUTSIDE_real[counter])
                        aval.append(CDL3STARSINSOUTH_real[counter])
                        aval.append(CDL3WHITESOLDIERS_real[counter])
                        aval.append(CDLABANDONEDBABY_real[counter])
                        aval.append(CDLADVANCEBLOCK_real[counter])
                        aval.append(CDLBELTHOLD_real[counter])
                        aval.append(CDLBREAKAWAY_real[counter])
                        aval.append(CDLCLOSINGMARUBOZU_real[counter])
                        aval.append(CDLCONCEALBABYSWALL_real[counter])
                        aval.append(CDLCOUNTERATTACK_real[counter])
                        aval.append(CDLDARKCLOUDCOVER_real[counter])
                        aval.append(CDLDOJI_real[counter])
                        aval.append(CDLDOJISTAR_real[counter])
                        aval.append(CDLDRAGONFLYDOJI_real[counter])
                        aval.append(CDLENGULFING_real[counter])
                        aval.append(CDLEVENINGDOJISTAR_real[counter])
                        aval.append(CDLEVENINGSTAR_real[counter])
                        aval.append(CDLGAPSIDESIDEWHITE_real[counter])
                        aval.append(CDLGRAVESTONEDOJI_real[counter])
                        aval.append(CDLHAMMER_real[counter])
                        aval.append(CDLHANGINGMAN_real[counter])
                        aval.append(CDLHARAMI_real[counter])
                        aval.append(CDLHARAMICROSS_real[counter])
                        aval.append(CDLHIGHWAVE_real[counter])
                        aval.append(CDLHIKKAKE_real[counter])
                        aval.append(CDLHIKKAKEMOD_real[counter])
                        aval.append(CDLHOMINGPIGEON_real[counter])
                        aval.append(CDLIDENTICAL3CROWS_real[counter])
                        aval.append(CDLINNECK_real[counter])
                        aval.append(CDLINVERTEDHAMMER_real[counter])
                        aval.append(CDLKICKING_real[counter])
                        aval.append(CDLKICKINGBYLENGTH_real[counter])
                        aval.append(CDLLADDERBOTTOM_real[counter])
                        aval.append(CDLLONGLEGGEDDOJI_real[counter])
                        aval.append(CDLLONGLINE_real[counter])
                        aval.append(CDLMARUBOZU_real[counter])
                        aval.append(CDLMATCHINGLOW_real[counter])
                        aval.append(CDLMATHOLD_real[counter])
                        aval.append(CDLMORNINGDOJISTAR_real[counter])
                        aval.append(CDLMORNINGSTAR_real[counter])
                        aval.append(CDLONNECK_real[counter])
                        aval.append(CDLPIERCING_real[counter])
                        aval.append(CDLRICKSHAWMAN_real[counter])
                        aval.append(CDLRISEFALL3METHODS_real[counter])
                        aval.append(CDLSEPARATINGLINES_real[counter])
                        aval.append(CDLSHOOTINGSTAR_real[counter])
                        aval.append(CDLSHORTLINE_real[counter])
                        aval.append(CDLSPINNINGTOP_real[counter])
                        aval.append(CDLSTALLEDPATTERN_real[counter])
                        aval.append(CDLSTICKSANDWICH_real[counter])
                        aval.append(CDLTAKURI_real[counter])
                        aval.append(CDLTASUKIGAP_real[counter])
                        aval.append(CDLTHRUSTING_real[counter])
                        aval.append(CDLTRISTAR_real[counter])
                        aval.append(CDLUNIQUE3RIVER_real[counter])
                        aval.append(CDLUPSIDEGAP2CROWS_real[counter])
                        aval.append(CDLXSIDEGAP3METHODS_real[counter]) 

                        aval.append(beta_real[counter]) 
                        aval.append(correl_real[counter]) 
                        aval.append(linearreg_real[counter]) 
                        aval.append(linearregang_real[counter]) 
                        aval.append(linearreginter_real[counter]) 
                        aval.append(linearregslope_real[counter]) 
                        aval.append(stdev_real[counter]) 
                        aval.append(tsf_real[counter]) 
                        aval.append(var_real[counter]) 
                        spamwriter.writerow(aval)
                        counter=counter+1
           


            