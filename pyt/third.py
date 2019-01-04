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
            filecsv='interval-'+key1+"-"+key2+".csv"
            listLong = []
            listShort = []
            with open(filecsv, newline='') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                    for row in spamreader:
                        listLong.append(row[1])
                        listShort.append(row[2])
                        if len(listLong) >100 :
                            listLong.pop(0)
                            listShort.pop(0)
                    listLong=set(listLong)
                    listShort=set(listShort)
            newListOfData=[]
            resorted={'open': [],'high': [],'low': [], 'close': [],'volume':[],'time':[]}
            with open(filename, newline='') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                    for row in spamreader:
                        newListOfData.append({'open': float(row[1]),'high': float(row[4]),'low': float(row[3]), 'close': float(row[2]),'volume':float(row[5]),'time':float(row[0])})
            
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

            