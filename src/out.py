def prediction(t_minus30, t_minus29, t_minus28, t_minus27, t_minus26, t_minus25, t_minus24, t_minus23, t_minus22, t_minus21, t_minus20, t_minus19, t_minus18, t_minus17, t_minus16, t_minus15, t_minus14, t_minus13, t_minus12, t_minus11, t_minus10, t_minus9, t_minus8, t_minus7, t_minus6, t_minus5, t_minus4, t_minus3, t_minus2, t_minus1, avedif):
    # Initial probabilities (F0)
    scores = [-0.12293963054198524, -3.9483244592778517]

# Update scores for each estimator
    if  avedif <= 2.7833333015441895:
        if  t_minus15 <= 3950.5:
            if  t_minus22 <= 3953.5:
                scores[0] += 0.2 * -0.824996502299065
            else:
                scores[0] += 0.2 * 7.1552470911655774
        else:
            if t_minus30 <= 3948.5:
                scores[0] += 0.2 * 5.305449283329978
            else:
                scores[0] += 0.2 * 0.16162650218284266
    else:
        if  t_minus24 <= 3946.5:
            if  t_minus17 <= 3950.5:
                scores[0] += 0.2 * -0.6648941104381286
            else:
                scores[0] += 0.2 * 7.3422951922982005
        else:
            if  t_minus2 <= 3946.5:
                scores[0] += 0.2 * 9.69286632986483
            else:
                scores[0] += 0.2 * 4.208318079109365

    if  t_minus19 <= 3950.5:
        if  t_minus7 <= 3952.5:
            if  t_minus22 <= 3952.5:
                scores[0] += 0.2 * -0.7109672059911861
            else:
                scores[0] += 0.2 * 2.770478974953316
        else:
            if  t_minus24 <= 3949.5:
                scores[0] += 0.2 * 3.0764420673125574
            else:
                scores[0] += 0.2 * 0.532416842928369
    else:
        if  avedif <= 2.5833332538604736:
            if t_minus30 <= 3946.5:
                scores[0] += 0.2 * 3.2667117466638214
            else:
                scores[0] += 0.2 * 0.1850883648373778
        else:
            if  t_minus2 <= 3952.5:
                scores[0] += 0.2 * 2.588583422193853
            else:
                scores[0] += 0.2 * 1.05625161748839

    if  t_minus16 <= 3950.5:
        if  t_minus23 <= 3953.5:
            if  t_minus28 <= 3954.5:
                scores[0] += 0.2 * -0.6010728306503155
            else:
                scores[0] += 0.2 * 2.366681500402511
        else:
            if  t_minus5 <= 3952.5:
                scores[0] += 0.2 * 2.4758669029391243
            else:
                scores[0] += 0.2 * -1.2656852422579141
    else:
        if  avedif <= 2.25:
            if t_minus30 <= 3948.5:
                scores[0] += 0.2 * 1.4450895776659183
            else:
                scores[0] += 0.2 * -0.013766637070128387
        else:
            if t_minus30 <= 3952.5:
                scores[0] += 0.2 * 2.1730480547202853
            else:
                scores[0] += 0.2 * 0.9106495240333428

    if  t_minus20 <= 3950.5:
        if  t_minus4 <= 3952.5:
            if  t_minus23 <= 3952.5:
                scores[0] += 0.2 * -0.6357256653634009
            else:
                scores[0] += 0.2 * 2.3349055850314655
        else:
            if  t_minus21 <= 3945.5:
                scores[0] += 0.2 * 0.2202408191555429
            else:
                scores[0] += 0.2 * 2.3046151173266343
    else:
        if  avedif <= 4.3500001430511475:
            if  t_minus3 <= 3946.5:
                scores[0] += 0.2 * 3.350883578896404
            else:
                scores[0] += 0.2 * 0.241888241186554
        else:
            if  t_minus22 <= 3957.5:
                scores[0] += 0.2 * 1.6197946426944803
            else:
                scores[0] += 0.2 * -0.4581239540694452

    if  avedif <= 1.6166666746139526:
        if  t_minus15 <= 3953.5:
            if  t_minus22 <= 3959.5:
                scores[0] += 0.2 * -0.6356839659374497
            else:
                scores[0] += 0.2 * 12.906009521638898
        else:
            if  t_minus29 <= 3950.5:
                scores[0] += 0.2 * 2.884989243676111
            else:
                scores[0] += 0.2 * -0.010686901754850889
    else:
        if  t_minus21 <= 3946.5:
            if  t_minus29 <= 3950.5:
                scores[0] += 0.2 * -0.6984434097524886
            else:
                scores[0] += 0.2 * 2.421064654869199
        else:
            if  avedif <= 4.3500001430511475:
                scores[0] += 0.2 * 0.6188823809900429
            else:
                scores[0] += 0.2 * 1.2950307607270366

    if  t_minus23 <= 3950.5:
        if  t_minus9 <= 3952.5:
            if  t_minus2 <= 3952.5:
                scores[0] += 0.2 * -0.6088501428204544
            else:
                scores[0] += 0.2 * 1.7106787157891943
        else:
            if  t_minus25 <= 3944.5:
                scores[0] += 0.2 * 0.014386332276520874
            else:
                scores[0] += 0.2 * 1.528350491544016
    else:
        if  avedif <= 1.6833333373069763:
            if  t_minus5 <= 3946.5:
                scores[0] += 0.2 * 9.08491175636227
            else:
                scores[0] += 0.2 * -0.05974554332229631
        else:
            if t_minus30 <= 3949.5:
                scores[0] += 0.2 * 1.9731168976438034
            else:
                scores[0] += 0.2 * 0.5151672792838823

    if  avedif <= 4.3500001430511475:
        if  t_minus17 <= 3951.5:
            if  t_minus28 <= 3953.5:
                scores[0] += 0.2 * -0.5054806225259794
            else:
                scores[0] += 0.2 * 2.043715945919927
        else:
            if t_minus30 <= 3950.5:
                scores[0] += 0.2 * 1.295344410264731
            else:
                scores[0] += 0.2 * -0.01687205531816118
    else:
        if  t_minus20 <= 3946.5:
            if  t_minus22 <= 3951.5:
                scores[0] += 0.2 * -0.42645930753294453
            else:
                scores[0] += 0.2 * 1.8506824663979862
        else:
            if  t_minus28 <= 3957.5:
                scores[0] += 0.2 * 1.1471456283353452
            else:
                scores[0] += 0.2 * -0.9272748893204028

    if  avedif <= 1.6166666746139526:
        if  t_minus15 <= 3956.5:
            if  t_minus8 <= 3960.5:
                scores[0] += 0.2 * -0.38838858605853865
            else:
                scores[0] += 0.2 * 13.115724744320072
        else:
            if  t_minus29 <= 3952.5:
                scores[0] += 0.2 * 3.582317468332446
            else:
                scores[0] += 0.2 * 0.37913188378233464
    else:
        if  t_minus25 <= 3946.5:
            if  t_minus21 <= 3951.5:
                scores[0] += 0.2 * -0.3803822839165301
            else:
                scores[0] += 0.2 * -1.8394072815753195
        else:
            if  t_minus1 <= 3946.5:
                scores[0] += 0.2 * 0.935713454538858
            else:
                scores[0] += 0.2 * 0.30799488977562917

    if  t_minus21 <= 3950.5:
        if  t_minus8 <= 3952.5:
            if  t_minus13 <= 3955.5:
                scores[0] += 0.2 * -0.4378330915517752
            else:
                scores[0] += 0.2 * 3.724047145331088
        else:
            if  t_minus9 <= 3955.5:
                scores[0] += 0.2 * 1.5240111754788455
            else:
                scores[0] += 0.2 * -0.2717746854570237
    else:
        if t_minus30 <= 3948.5:
            if  t_minus13 <= 3952.5:
                scores[0] += 0.2 * 0.2794350200197196
            else:
                scores[0] += 0.2 * 1.2898769996099404
        else:
            if  t_minus4 <= 3950.5:
                scores[0] += 0.2 * 0.798974796758899
            else:
                scores[0] += 0.2 * -0.06261982929488792

    if  t_minus19 <= 3952.5:
        if  t_minus3 <= 3954.5:
            if t_minus30 <= 3954.5:
                scores[0] += 0.2 * -0.3230601332928152
            else:
                scores[0] += 0.2 * 1.2132490115604793
        else:
            if  t_minus24 <= 3946.5:
                scores[0] += 0.2 * -0.20966912743669797
            else:
                scores[0] += 0.2 * 1.827474745066327
    else:
        if t_minus30 <= 3952.5:
            if  t_minus20 <= 3953.5:
                scores[0] += 0.2 * 0.8821531300450964
            else:
                scores[0] += 0.2 * 2.122088113401296
        else:
            if  t_minus11 <= 3951.5:
                scores[0] += 0.2 * 1.1749152294906777
            else:
                scores[0] += 0.2 * -0.23784942822054278

    if  avedif <= 1.6166666746139526:
        if  t_minus5 <= 3956.5:
            if  t_minus16 <= 3957.5:
                scores[0] += 0.2 * -0.34039680803947525
            else:
                scores[0] += 0.2 * 1.465723163461755
        else:
            if  t_minus1 <= 3957.5:
                scores[0] += 0.2 * 1.2441688198678231
            else:
                scores[0] += 0.2 * -1.1610526339041887
    else:
        if  t_minus27 <= 3946.5:
            if  t_minus4 <= 3949.5:
                scores[0] += 0.2 * -0.7920861978066663
            else:
                scores[0] += 0.2 * 0.5282823089430977
        else:
            if  t_minus1 <= 3946.5:
                scores[0] += 0.2 * 0.8242709637301857
            else:
                scores[0] += 0.2 * 0.1897542510890478

    if  t_minus26 <= 3945.5:
        if t_minus30 <= 3954.5:
            if  t_minus1 <= 3949.5:
                scores[0] += 0.2 * -0.7386395141855677
            else:
                scores[0] += 0.2 * 0.4842315563923244
        else:
            if  t_minus24 <= 3944.5:
                scores[0] += 0.2 * 24.012669216613897
            else:
                scores[0] += 0.2 * -1.4031451147398282
    else:
        if  avedif <= 1.6166666746139526:
            if  t_minus14 <= 3941.5:
                scores[0] += 0.2 * 7.105363205027486
            else:
                scores[0] += 0.2 * -0.11158693654629344
        else:
            if  t_minus29 <= 3958.5:
                scores[0] += 0.2 * 0.29974298162046076
            else:
                scores[0] += 0.2 * -1.2956439409107479

    if  t_minus12 <= 3955.5:
        if  t_minus7 <= 3956.5:
            if  t_minus3 <= 3958.5:
                scores[0] += 0.2 * -0.13291003399659007
            else:
                scores[0] += 0.2 * 2.73089059584954
        else:
            if  t_minus11 <= 3952.5:
                scores[0] += 0.2 * 2.1959520142306115
            else:
                scores[0] += 0.2 * 0.5660154641968317
    else:
        if t_minus30 <= 3952.5:
            if  t_minus24 <= 3948.5:
                scores[0] += 0.2 * -0.2929130145270183
            else:
                scores[0] += 0.2 * 2.005881443296271
        else:
            if  avedif <= 13.683333396911621:
                scores[0] += 0.2 * 0.07746086639772808
            else:
                scores[0] += 0.2 * -2.9865251329757485

    if  t_minus28 <= 3958.5:
        if  t_minus12 <= 3956.5:
            if  t_minus4 <= 3956.5:
                scores[0] += 0.2 * -0.08981585070719018
            else:
                scores[0] += 0.2 * 0.6538281262701844
        else:
            if  t_minus24 <= 3958.5:
                scores[0] += 0.2 * 0.7448771259195045
            else:
                scores[0] += 0.2 * -1.282733568412855
    else:
        if  t_minus3 <= 3934.5:
            if  t_minus16 <= 3949.5:
                scores[0] += 0.2 * -2.330692890163387
            else:
                scores[0] += 0.2 * -4.77007284528949
        else:
            if  t_minus22 <= 3955.5:
                scores[0] += 0.2 * 1.04938628312452
            else:
                scores[0] += 0.2 * -1.1184277535383222

    if  t_minus23 <= 3959.5:
        if  t_minus18 <= 3959.5:
            if  t_minus20 <= 3953.5:
                scores[0] += 0.2 * -0.10208005223430205
            else:
                scores[0] += 0.2 * 0.23245202261090941
        else:
            if  t_minus17 <= 3960.5:
                scores[0] += 0.2 * -1.433281387925762
            else:
                scores[0] += 0.2 * 9.067048468363286
    else:
        if  avedif <= 9.733333110809326:
            if  t_minus5 <= 3954.5:
                scores[0] += 0.2 * 2.3257373803280723
            else:
                scores[0] += 0.2 * -1.021572992118839
        else:
            if  t_minus28 <= 3955.5:
                scores[0] += 0.2 * -4.700365274695705
            else:
                scores[0] += 0.2 * -3.7895452957734372

    if  avedif <= 4.3500001430511475:
        if  t_minus1 <= 3958.5:
            if  t_minus6 <= 3956.5:
                scores[0] += 0.2 * -0.09397094815365722
            else:
                scores[0] += 0.2 * 0.5870734664221073
        else:
            if  t_minus16 <= 3954.5:
                scores[0] += 0.2 * 2.9153897431924425
            else:
                scores[0] += 0.2 * -1.2775965630239736
    else:
        if  t_minus29 <= 3957.5:
            if  t_minus19 <= 3945.5:
                scores[0] += 0.2 * -0.38784746500629386
            else:
                scores[0] += 0.2 * 0.6546706642861397
        else:
            if  t_minus7 <= 3938.5:
                scores[0] += 0.2 * -4.7114964110174355
            else:
                scores[0] += 0.2 * -0.9280759327125931

    if  avedif <= 1.6166666746139526:
        if  t_minus18 <= 3954.5:
            if  t_minus14 <= 3959.5:
                scores[0] += 0.2 * -0.31541618906659247
            else:
                scores[0] += 0.2 * 4.3770006242478185
        else:
            if t_minus30 <= 3952.5:
                scores[0] += 0.2 * 1.8582812280314003
            else:
                scores[0] += 0.2 * -0.05950913810593503
    else:
        if  t_minus7 <= 3958.5:
            if  t_minus27 <= 3944.5:
                scores[0] += 0.2 * -0.4036482827222736
            else:
                scores[0] += 0.2 * 0.2469677796997123
        else:
            if  t_minus24 <= 3945.5:
                scores[0] += 0.2 * -2.192871492363775
            else:
                scores[0] += 0.2 * -1.0480143181549968

    if  t_minus27 <= 3959.5:
        if  t_minus7 <= 3956.5:
            if  t_minus10 <= 3960.5:
                scores[0] += 0.2 * -0.03817416772147918
            else:
                scores[0] += 0.2 * 8.596050002783988
        else:
            if  t_minus22 <= 3956.5:
                scores[0] += 0.2 * 0.7914789502991418
            else:
                scores[0] += 0.2 * -0.4533759072256625
    else:
        if  t_minus21 <= 3955.5:
            if  t_minus15 <= 3955.5:
                scores[0] += 0.2 * 3.993675747582867
            else:
                scores[0] += 0.2 * -1.2451042201314027
        else:
            if t_minus30 <= 3948.5:
                scores[0] += 0.2 * -2.3206884000920183
            else:
                scores[0] += 0.2 * -1.1928750775779215

    if  t_minus28 <= 3958.5:
        if  t_minus12 <= 3956.5:
            if  t_minus6 <= 3960.5:
                scores[0] += 0.2 * -0.030366869773830348
            else:
                scores[0] += 0.2 * 10.008544171012844
        else:
            if  t_minus4 <= 3953.5:
                scores[0] += 0.2 * 1.4493165698986266
            else:
                scores[0] += 0.2 * 0.15741941349321076
    else:
        if  avedif <= 3.166666626930237:
            if  t_minus16 <= 3952.0:
                scores[0] += 0.2 * 1.9330520473317927
            else:
                scores[0] += 0.2 * -0.8739424453301025
        else:
            if  avedif <= 14.400000095367432:
                scores[0] += 0.2 * -1.376024816118318
            else:
                scores[0] += 0.2 * 1.403730253514302

    if  t_minus26 <= 3945.5:
        if  t_minus8 <= 3957.5:
            if  t_minus14 <= 3952.5:
                scores[0] += 0.2 * -0.46564104248645893
            else:
                scores[0] += 0.2 * 0.8458193492382496
        else:
            if  t_minus18 <= 3951.0:
                scores[0] += 0.2 * -0.25085648743629585
            else:
                scores[0] += 0.2 * -2.2155392281874247
    else:
        if  t_minus16 <= 3942.5:
            if  t_minus2 <= 3939.5:
                scores[0] += 0.2 * -0.29817230497405406
            else:
                scores[0] += 0.2 * 2.7797021245184035
        else:
            if  t_minus4 <= 3946.5:
                scores[0] += 0.2 * 0.5636568100331896
            else:
                scores[0] += 0.2 * -0.013965802888842591

    if  t_minus23 <= 3959.5:
        if  t_minus18 <= 3959.5:
            if  t_minus2 <= 3956.5:
                scores[0] += 0.2 * -0.02196030810174738
            else:
                scores[0] += 0.2 * 0.35599469052510363
        else:
            if  avedif <= 12.25:
                scores[0] += 0.2 * -0.8752463281690506
            else:
                scores[0] += 0.2 * -2.988880881534889
    else:
        if  avedif <= 9.733333110809326:
            if  t_minus5 <= 3954.5:
                scores[0] += 0.2 * 1.892047132832284
            else:
                scores[0] += 0.2 * -0.9554990392661966
        else:
            if  t_minus4 <= 3937.5:
                scores[0] += 0.2 * -2.72861479331759
            else:
                scores[0] += 0.2 * -2.911157971271087

    if  t_minus3 <= 3959.5:
        if  t_minus26 <= 3950.5:
            if  t_minus13 <= 3952.5:
                scores[0] += 0.2 * -0.263179563474833
            else:
                scores[0] += 0.2 * 0.7809792953432704
        else:
            if  t_minus2 <= 3950.5:
                scores[0] += 0.2 * 0.7309826975936047
            else:
                scores[0] += 0.2 * -0.08694807972557822
    else:
        if  t_minus5 <= 3952.0:
            scores[0] += 0.2 * 1.7329159903104703
        else:
            if  t_minus27 <= 3938.5:
                scores[0] += 0.2 * -1.9318395108366049
            else:
                scores[0] += 0.2 * -0.9273892795837769

    if t_minus30 <= 3959.5:
        if  t_minus7 <= 3956.5:
            if  t_minus24 <= 3957.5:
                scores[0] += 0.2 * -0.0408137123792639
            else:
                scores[0] += 0.2 * 0.7693037212873202
        else:
            if  t_minus22 <= 3956.5:
                scores[0] += 0.2 * 0.5906994986769827
            else:
                scores[0] += 0.2 * -0.38361274453520067
    else:
        if  t_minus27 <= 3955.5:
            if  t_minus24 <= 3956.0:
                scores[0] += 0.2 * 4.23647329168684
            else:
                scores[0] += 0.2 * -0.5759830309906327
        else:
            if  avedif <= 6.900000095367432:
                scores[0] += 0.2 * -1.1518515935897524
            else:
                scores[0] += 0.2 * -3.7890247933968935

    if  t_minus24 <= 3959.5:
        if  avedif <= 0.550000011920929:
            if  t_minus12 <= 3956.5:
                scores[0] += 0.2 * -0.3408626778797119
            else:
                scores[0] += 0.2 * 0.5139981763732933
        else:
            if  t_minus1 <= 3939.5:
                scores[0] += 0.2 * -0.640311915192762
            else:
                scores[0] += 0.2 * 0.11705445096933573
    else:
        if  avedif <= 2.7333333492279053:
            if  t_minus12 <= 3955.5:
                scores[0] += 0.2 * 5.026035260590538
            else:
                scores[0] += 0.2 * -1.0701038439696116
        else:
            if  t_minus10 <= 3948.0:
                scores[0] += 0.2 * 1.1314705498967348
            else:
                scores[0] += 0.2 * -1.5141320500041549

    if  t_minus8 <= 3959.5:
        if  t_minus6 <= 3956.5:
            if  t_minus23 <= 3957.5:
                scores[0] += 0.2 * -0.04148967001003204
            else:
                scores[0] += 0.2 * 0.8274800722019263
        else:
            if  t_minus23 <= 3956.5:
                scores[0] += 0.2 * 0.6441180086508117
            else:
                scores[0] += 0.2 * -0.5302960425940301
    else:
        if  t_minus7 <= 3960.5:
            if t_minus30 <= 3952.5:
                scores[0] += 0.2 * -1.7436772699264784
            else:
                scores[0] += 0.2 * -0.7948510405865081
        else:
            scores[0] += 0.2 * 5.461637676729802

    if  t_minus28 <= 3955.5:
        if  t_minus13 <= 3957.5:
            if  t_minus23 <= 3957.5:
                scores[0] += 0.2 * -0.0034543811429087194
            else:
                scores[0] += 0.2 * 1.224068088534375
        else:
            if  t_minus26 <= 3946.5:
                scores[0] += 0.2 * -1.3191228989026385
            else:
                scores[0] += 0.2 * 1.5221948441696447
    else:
        if  t_minus25 <= 3948.5:
            if  t_minus10 <= 3952.5:
                scores[0] += 0.2 * 6.083769182689017
            else:
                scores[0] += 0.2 * -1.6763265127943645
        else:
            if  t_minus21 <= 3945.5:
                scores[0] += 0.2 * -2.2385852318179866
            else:
                scores[0] += 0.2 * -0.1813401575394257

    if  t_minus10 <= 3957.5:
        if  t_minus10 <= 3956.5:
            if  t_minus2 <= 3956.5:
                scores[0] += 0.2 * -0.04496327002882139
            else:
                scores[0] += 0.2 * 0.40893071473496684
        else:
            if  t_minus6 <= 3948.0:
                scores[0] += 0.2 * 5.069340814009253
            else:
                scores[0] += 0.2 * 0.5225051913039415
    else:
        if  t_minus25 <= 3946.5:
            if  avedif <= 5.2833333015441895:
                scores[0] += 0.2 * -2.1829851597499506
            else:
                scores[0] += 0.2 * -1.1648519802733912
        else:
            if  t_minus27 <= 3952.5:
                scores[0] += 0.2 * 2.078266116089833
            else:
                scores[0] += 0.2 * -0.5694089427437211

    if  t_minus1 <= 3957.5:
        if  t_minus6 <= 3956.5:
            if  t_minus16 <= 3957.5:
                scores[0] += 0.2 * -0.030405058871618484
            else:
                scores[0] += 0.2 * 0.8099881284268913
        else:
            if  t_minus12 <= 3952.5:
                scores[0] += 0.2 * 2.024636406518119
            else:
                scores[0] += 0.2 * 0.1986071461912398
    else:
        if  t_minus27 <= 3931.5:
            if  t_minus19 <= 3949.5:
                scores[0] += 0.2 * 1.884636762452752
            else:
                scores[0] += 0.2 * 2.472969186942739
        else:
            if  avedif <= 13.016666412353516:
                scores[0] += 0.2 * -0.4253442885960777
            else:
                scores[0] += 0.2 * 4.131360578762133

    if  t_minus28 <= 3955.5:
        if  t_minus19 <= 3957.5:
            if  t_minus11 <= 3957.5:
                scores[0] += 0.2 * -0.002955915056891996
            else:
                scores[0] += 0.2 * 1.0355547089979378
        else:
            if t_minus30 <= 3956.5:
                scores[0] += 0.2 * 1.5112525422576808
            else:
                scores[0] += 0.2 * -1.1136167183845498
    else:
        if  t_minus25 <= 3948.5:
            if  t_minus18 <= 3952.5:
                scores[0] += 0.2 * 2.791850675619947
            else:
                scores[0] += 0.2 * -1.4931645269865432
        else:
            if  t_minus21 <= 3945.5:
                scores[0] += 0.2 * -1.7279683318524202
            else:
                scores[0] += 0.2 * -0.1587345514498634

    if  avedif <= 4.3500001430511475:
        if  t_minus1 <= 3958.5:
            if  t_minus5 <= 3956.5:
                scores[0] += 0.2 * -0.05175861862631092
            else:
                scores[0] += 0.2 * 0.30196940933277616
        else:
            if  t_minus16 <= 3954.5:
                scores[0] += 0.2 * 1.3818037422550082
            else:
                scores[0] += 0.2 * -1.1276842790046844
    else:
        if  t_minus12 <= 3958.5:
            if  t_minus2 <= 3942.5:
                scores[0] += 0.2 * -0.4464938504225367
            else:
                scores[0] += 0.2 * 0.5385792287623291
        else:
            if  t_minus6 <= 3955.5:
                scores[0] += 0.2 * -3.2595879553888905
            else:
                scores[0] += 0.2 * -1.4303769703298468

    if  t_minus21 <= 3959.5:
        if  t_minus5 <= 3960.5:
            if  t_minus28 <= 3945.5:
                scores[0] += 0.2 * -0.29957566223927223
            else:
                scores[0] += 0.2 * 0.06024443271072566
        else:
            scores[0] += 0.2 * 2.303529177495159
    else:
        if  t_minus1 <= 3938.5:
            if  t_minus23 <= 3958.0:
                scores[0] += 0.2 * -3.155266456478308
            else:
                scores[0] += 0.2 * -5.453980947579214
        else:
            if  t_minus28 <= 3954.5:
                scores[0] += 0.2 * 2.2873297753073256
            else:
                scores[0] += 0.2 * -1.0603989623483787

    if  t_minus4 <= 3953.5:
        if  t_minus21 <= 3952.5:
            if  t_minus9 <= 3954.5:
                scores[0] += 0.2 * -0.11728520377591918
            else:
                scores[0] += 0.2 * 1.7023268112862784
        else:
            if  t_minus6 <= 3951.5:
                scores[0] += 0.2 * 1.243887100815981
            else:
                scores[0] += 0.2 * 0.029942716839915652
    else:
        if t_minus30 <= 3952.5:
            if  t_minus26 <= 3946.5:
                scores[0] += 0.2 * -0.45752764904358384
            else:
                scores[0] += 0.2 * 0.9467500336720371
        else:
            if  avedif <= 2.5166666507720947:
                scores[0] += 0.2 * -0.24714246683484148
            else:
                scores[0] += 0.2 * -0.666151523858097

    if  t_minus27 <= 3959.5:
        if  t_minus5 <= 3960.5:
            if  t_minus10 <= 3956.5:
                scores[0] += 0.2 * -0.018056960757867137
            else:
                scores[0] += 0.2 * 0.22591398047905628
        else:
            scores[0] += 0.2 * 1.939506827845418
    else:
        if  t_minus4 <= 3936.5:
            scores[0] += 0.2 * -2.6691689548365396
        else:
            if  t_minus24 <= 3955.5:
                scores[0] += 0.2 * 1.3961909937440051
            else:
                scores[0] += 0.2 * -1.1650232894140309

    if  t_minus23 <= 3959.5:
        if  t_minus28 <= 3958.5:
            if  t_minus11 <= 3956.5:
                scores[0] += 0.2 * -0.011057214732092356
            else:
                scores[0] += 0.2 * 0.30216467949267944
        else:
            if  t_minus4 <= 3938.5:
                scores[0] += 0.2 * -1.7716207934356156
            else:
                scores[0] += 0.2 * -0.5197344962377451
    else:
        if  t_minus4 <= 3945.0:
            if  t_minus18 <= 3955.5:
                scores[0] += 0.2 * -2.2993867169307918
            else:
                scores[0] += 0.2 * -2.8687495799481466
        else:
            if  t_minus5 <= 3954.5:
                scores[0] += 0.2 * 1.7311677344451624
            else:
                scores[0] += 0.2 * -0.8656785595869283

    if  avedif <= 1.6166666746139526:
        if  t_minus15 <= 3956.5:
            if  t_minus1 <= 3956.5:
                scores[0] += 0.2 * -0.176132172811602
            else:
                scores[0] += 0.2 * 0.6907826837878922
        else:
            if  t_minus28 <= 3952.5:
                scores[0] += 0.2 * 1.7789117359597013
            else:
                scores[0] += 0.2 * 0.16608186011287682
    else:
        if  t_minus4 <= 3953.5:
            if  t_minus3 <= 3952.5:
                scores[0] += 0.2 * 0.13073416056471954
            else:
                scores[0] += 0.2 * 0.6641146482581682
        else:
            if  t_minus29 <= 3952.5:
                scores[0] += 0.2 * 0.2509144247651322
            else:
                scores[0] += 0.2 * -0.43761268215785065

    if  t_minus1 <= 3955.5:
        if  t_minus23 <= 3951.5:
            if  t_minus5 <= 3952.5:
                scores[0] += 0.2 * -0.16535639549340012
            else:
                scores[0] += 0.2 * 0.5255577587592506
        else:
            if  t_minus7 <= 3951.5:
                scores[0] += 0.2 * 0.714021025007876
            else:
                scores[0] += 0.2 * -0.09418145279714978
    else:
        if  t_minus29 <= 3952.5:
            if t_minus30 <= 3948.5:
                scores[0] += 0.2 * -0.43047085629992105
            else:
                scores[0] += 0.2 * 0.9686580680844841
        else:
            if  avedif <= 2.8499999046325684:
                scores[0] += 0.2 * -0.1761203909022369
            else:
                scores[0] += 0.2 * -1.05785697992832

    if  t_minus3 <= 3959.5:
        if  avedif <= 8.416666507720947:
            if  avedif <= 7.483333349227905:
                scores[0] += 0.2 * 0.007266017027579457
            else:
                scores[0] += 0.2 * 0.9670933516375982
        else:
            if  t_minus18 <= 3957.5:
                scores[0] += 0.2 * -0.23002033458957882
            else:
                scores[0] += 0.2 * -2.418253438148147
    else:
        if  t_minus12 <= 3951.5:
            if  t_minus24 <= 3958.5:
                scores[0] += 0.2 * -1.2983249086606468
            else:
                scores[0] += 0.2 * -1.5101673986568556
        else:
            if  t_minus25 <= 3960.5:
                scores[0] += 0.2 * -0.7797964190214438
            else:
                scores[0] += 0.2 * -1.7140901590844144

    if  t_minus4 <= 3959.5:
        if  t_minus15 <= 3960.5:
            if  t_minus8 <= 3956.5:
                scores[0] += 0.2 * -0.016859875262946113
            else:
                scores[0] += 0.2 * 0.21252824738390025
        else:
            scores[0] += 0.2 * 3.43500902798547
    else:
        if  t_minus28 <= 3942.5:
            if  t_minus3 <= 3957.5:
                scores[0] += 0.2 * -2.771683800541887
            else:
                scores[0] += 0.2 * -1.2301009690240665
        else:
            if  t_minus11 <= 3953.5:
                scores[0] += 0.2 * 1.8106239024245585
            else:
                scores[0] += 0.2 * -0.8764702655959853

    if  t_minus5 <= 3959.5:
        if  t_minus14 <= 3956.5:
            if  t_minus13 <= 3959.5:
                scores[0] += 0.2 * -0.01130609495637552
            else:
                scores[0] += 0.2 * -1.5293026981286197
        else:
            if  t_minus18 <= 3952.5:
                scores[0] += 0.2 * 1.5806802478849549
            else:
                scores[0] += 0.2 * 0.12598942976971356
    else:
        if  t_minus29 <= 3942.5:
            scores[0] += 0.2 * -2.070647881630212
        else:
            if  t_minus29 <= 3955.5:
                scores[0] += 0.2 * 0.6286720882253138
            else:
                scores[0] += 0.2 * -1.1261173056141047

    if  t_minus10 <= 3957.5:
        if  t_minus10 <= 3956.5:
            if t_minus30 <= 3957.5:
                scores[0] += 0.2 * -0.02882235878805437
            else:
                scores[0] += 0.2 * 0.6507039450520339
        else:
            if  t_minus6 <= 3946.0:
                scores[0] += 0.2 * 8.450675895306873
            else:
                scores[0] += 0.2 * 0.41845993205376397
    else:
        if  t_minus25 <= 3946.5:
            if  t_minus4 <= 3956.5:
                scores[0] += 0.2 * -1.783322736807439
            else:
                scores[0] += 0.2 * -1.1653984001449746
        else:
            if  t_minus25 <= 3954.5:
                scores[0] += 0.2 * 1.1613207794491691
            else:
                scores[0] += 0.2 * -0.6329444513749551

    if  t_minus1 <= 3955.5:
        if  t_minus18 <= 3956.5:
            if  t_minus23 <= 3958.5:
                scores[0] += 0.2 * 0.012091087895133279
            else:
                scores[0] += 0.2 * -1.9036103133619264
        else:
            if  avedif <= 1.9166666269302368:
                scores[0] += 0.2 * 1.7408501505758491
            else:
                scores[0] += 0.2 * -0.24417447712940232
    else:
        if  t_minus24 <= 3952.5:
            if  avedif <= 3.100000023841858:
                scores[0] += 0.2 * 1.7336241438068987
            else:
                scores[0] += 0.2 * -0.19742014316149728
        else:
            if  avedif <= 1.9833333492279053:
                scores[0] += 0.2 * -0.11535074557073542
            else:
                scores[0] += 0.2 * -0.6368615590044431

    if  t_minus5 <= 3953.5:
        if  t_minus19 <= 3952.5:
            if  t_minus2 <= 3952.5:
                scores[0] += 0.2 * -0.16155321673426584
            else:
                scores[0] += 0.2 * 0.9344880501372799
        else:
            if t_minus30 <= 3949.5:
                scores[0] += 0.2 * 1.3858284806215628
            else:
                scores[0] += 0.2 * 0.22053405786578842
    else:
        if  t_minus29 <= 3952.5:
            if  t_minus27 <= 3946.5:
                scores[0] += 0.2 * -0.39553712720645956
            else:
                scores[0] += 0.2 * 0.8263602753773531
        else:
            if  t_minus2 <= 3956.5:
                scores[0] += 0.2 * -0.3885538734249649
            else:
                scores[0] += 0.2 * 0.18756732755172925

    if  t_minus4 <= 3959.5:
        if  t_minus15 <= 3960.5:
            if  t_minus10 <= 3960.5:
                scores[0] += 0.2 * 0.00045141859239441275
            else:
                scores[0] += 0.2 * 2.190118952255804
        else:
            scores[0] += 0.2 * 1.8095127999173488
    else:
        if  t_minus28 <= 3942.5:
            if  t_minus19 <= 3954.0:
                scores[0] += 0.2 * -2.285664883986719
            else:
                scores[0] += 0.2 * -1.1688493257270194
        else:
            if  t_minus10 <= 3951.5:
                scores[0] += 0.2 * 1.3409405860039036
            else:
                scores[0] += 0.2 * -0.8752652083480078

    if  t_minus6 <= 3951.5:
        if  t_minus24 <= 3952.5:
            if  t_minus8 <= 3954.5:
                scores[0] += 0.2 * -0.10644611025580829
            else:
                scores[0] += 0.2 * 3.187824062012777
        else:
            if  t_minus2 <= 3943.5:
                scores[0] += 0.2 * -0.6825093594550702
            else:
                scores[0] += 0.2 * 1.4304187229982224
    else:
        if  t_minus29 <= 3949.5:
            if  t_minus3 <= 3954.5:
                scores[0] += 0.2 * 0.8801468622986083
            else:
                scores[0] += 0.2 * -0.21693022104379073
        else:
            if  t_minus5 <= 3946.0:
                scores[0] += 0.2 * 18.74878385653208
            else:
                scores[0] += 0.2 * -0.19883110232333445

    if  avedif <= 17.983333587646484:
        if  avedif <= 16.449999809265137:
            if  t_minus6 <= 3948.5:
                scores[0] += 0.2 * 0.1676654965428625
            else:
                scores[0] += 0.2 * -0.059817618430705925
        else:
            if  t_minus19 <= 3954.0:
                scores[0] += 0.2 * 0.07376194628646592
            else:
                scores[0] += 0.2 * -2.4572623870863612
    else:
        if  t_minus8 <= 3955.0:
            if  t_minus20 <= 3954.0:
                scores[0] += 0.2 * 1.264504253879492
            else:
                scores[0] += 0.2 * 1.1042290707591433
        else:
            scores[0] += 0.2 * -1.379344560498054

    if  t_minus5 <= 3956.5:
        if  t_minus12 <= 3960.5:
            if  t_minus22 <= 3957.5:
                scores[0] += 0.2 * -0.040683816689128606
            else:
                scores[0] += 0.2 * 0.6623485128779909
        else:
            scores[0] += 0.2 * 2.8723804622688913
    else:
        if  t_minus22 <= 3956.5:
            if  t_minus24 <= 3946.5:
                scores[0] += 0.2 * -0.9226265028688371
            else:
                scores[0] += 0.2 * 0.6508717524080552
        else:
            if  t_minus23 <= 3951.5:
                scores[0] += 0.2 * 1.968184266283437
            else:
                scores[0] += 0.2 * -0.45118170006041664

    if  t_minus3 <= 3959.5:
        if  t_minus3 <= 3956.5:
            if  t_minus20 <= 3957.5:
                scores[0] += 0.2 * -0.03839176556495055
            else:
                scores[0] += 0.2 * 0.8143877976541336
        else:
            if  t_minus20 <= 3956.5:
                scores[0] += 0.2 * 0.6053478562000112
            else:
                scores[0] += 0.2 * -0.399267394948159
    else:
        if  t_minus25 <= 3960.5:
            if  t_minus5 <= 3952.0:
                scores[0] += 0.2 * 1.2184997019212187
            else:
                scores[0] += 0.2 * -0.945374153803093
        else:
            if  t_minus21 <= 3955.5:
                scores[0] += 0.2 * -1.818692671525589
            else:
                scores[0] += 0.2 * -1.0427296046793892

    if  t_minus9 <= 3948.5:
        if t_minus30 <= 3948.5:
            if  t_minus17 <= 3952.5:
                scores[0] += 0.2 * -0.3726216475263186
            else:
                scores[0] += 0.2 * 1.9892124188050109
        else:
            if  t_minus3 <= 3947.5:
                scores[0] += 0.2 * 1.2278767481122144
            else:
                scores[0] += 0.2 * 0.51067223459997
    else:
        if t_minus30 <= 3946.5:
            if  t_minus4 <= 3954.5:
                scores[0] += 0.2 * 0.8301905221616181
            else:
                scores[0] += 0.2 * -0.3381112159184497
        else:
            if  t_minus29 <= 3942.5:
                scores[0] += 0.2 * 5.1299963521569225
            else:
                scores[0] += 0.2 * -0.09491596656545431

    if  t_minus6 <= 3956.5:
        if  t_minus23 <= 3957.5:
            if  t_minus18 <= 3959.5:
                scores[0] += 0.2 * -0.03258029580828852
            else:
                scores[0] += 0.2 * -1.878952657572068
        else:
            if  avedif <= 3.2166666984558105:
                scores[0] += 0.2 * 1.0499893433703162
            else:
                scores[0] += 0.2 * -1.0884535554959816
    else:
        if  t_minus23 <= 3956.5:
            if  t_minus1 <= 3953.5:
                scores[0] += 0.2 * 1.3612938752046295
            else:
                scores[0] += 0.2 * 0.26521367119214184
        else:
            if  t_minus24 <= 3952.0:
                scores[0] += 0.2 * 5.313137637441337
            else:
                scores[0] += 0.2 * -0.4416624587345796

    if  t_minus5 <= 3960.5:
        if t_minus30 <= 3959.5:
            if  t_minus8 <= 3956.5:
                scores[0] += 0.2 * -0.018510934191114013
            else:
                scores[0] += 0.2 * 0.21749872769400344
        else:
            if  t_minus18 <= 3950.5:
                scores[0] += 0.2 * -2.569977373595967
            else:
                scores[0] += 0.2 * -0.5488710028359977
    else:
        if  t_minus9 <= 3954.5:
            scores[0] += 0.2 * 1.9958169455562278
        else:
            scores[0] += 0.2 * -1.0027406143534843

    if  t_minus28 <= 3958.5:
        if  t_minus10 <= 3960.5:
            if  t_minus16 <= 3956.5:
                scores[0] += 0.2 * -0.01580416358068997
            else:
                scores[0] += 0.2 * 0.2121324455127389
        else:
            scores[0] += 0.2 * 1.8639939869638973
    else:
        if  t_minus4 <= 3938.5:
            if  t_minus19 <= 3952.5:
                scores[0] += 0.2 * -0.11772238912333645
            else:
                scores[0] += 0.2 * -2.4975007262395756
        else:
            if  t_minus13 <= 3953.5:
                scores[0] += 0.2 * 1.372662173654938
            else:
                scores[0] += 0.2 * -0.6510433768574332

    if  t_minus8 <= 3951.5:
        if  t_minus23 <= 3952.5:
            if  t_minus17 <= 3955.5:
                scores[0] += 0.2 * -0.07733256404994704
            else:
                scores[0] += 0.2 * 2.28284442103372
        else:
            if  t_minus2 <= 3942.5:
                scores[0] += 0.2 * -0.9278684675174916
            else:
                scores[0] += 0.2 * 1.3999391547880886
    else:
        if  t_minus29 <= 3949.5:
            if  t_minus11 <= 3955.5:
                scores[0] += 0.2 * 0.6386963696735909
            else:
                scores[0] += 0.2 * -0.6289838212876048
        else:
            if  t_minus7 <= 3945.5:
                scores[0] += 0.2 * 40.41392369925014
            else:
                scores[0] += 0.2 * -0.18319498532526465

    if  t_minus7 <= 3956.5:
        if  t_minus1 <= 3955.5:
            if  t_minus9 <= 3959.5:
                scores[0] += 0.2 * 0.013764684052371964
            else:
                scores[0] += 0.2 * 8.560285737108382
        else:
            if  t_minus12 <= 3941.0:
                scores[0] += 0.2 * 1.4646294496877217
            else:
                scores[0] += 0.2 * -0.26913299370777066
    else:
        if  t_minus24 <= 3956.5:
            if  t_minus5 <= 3956.5:
                scores[0] += 0.2 * 0.02366313393518798
            else:
                scores[0] += 0.2 * 1.0413461304739695
        else:
            if  t_minus25 <= 3951.5:
                scores[0] += 0.2 * 9.696402785721155
            else:
                scores[0] += 0.2 * -0.38397689554427833

    if  t_minus9 <= 3948.5:
        if  t_minus28 <= 3950.5:
            if  t_minus12 <= 3952.5:
                scores[0] += 0.2 * -0.11190382949288975
            else:
                scores[0] += 0.2 * 1.9335320325995171
        else:
            if t_minus30 <= 3954.5:
                scores[0] += 0.2 * 1.6094899936765747
            else:
                scores[0] += 0.2 * -0.32361815404803246
    else:
        if t_minus30 <= 3923.5:
            scores[0] += 0.2 * 2.1612483591788143
        else:
            if  t_minus5 <= 3942.0:
                scores[0] += 0.2 * -1.044746522729244
            else:
                scores[0] += 0.2 * -0.05120566664143709

    if  t_minus20 <= 3953.5:
        if  t_minus17 <= 3959.5:
            if  t_minus24 <= 3955.5:
                scores[0] += 0.2 * -0.033229336813858305
            else:
                scores[0] += 0.2 * -0.7260867997901291
        else:
            if  t_minus11 <= 3957.5:
                scores[0] += 0.2 * 2.5700330090955132
            else:
                scores[0] += 0.2 * -1.299984357519306
    else:
        if  t_minus18 <= 3949.5:
            if  t_minus10 <= 3952.5:
                scores[0] += 0.2 * 4.428020266344994
            else:
                scores[0] += 0.2 * -1.128184859338046
        else:
            if  t_minus29 <= 3951.5:
                scores[0] += 0.2 * 0.7222792943779246
            else:
                scores[0] += 0.2 * -0.04573241769206198

    if  t_minus4 <= 3956.5:
        if  t_minus21 <= 3957.5:
            if  t_minus6 <= 3951.5:
                scores[0] += 0.2 * 0.046691409160416295
            else:
                scores[0] += 0.2 * -0.13431224019931085
        else:
            if  avedif <= 3.5666667222976685:
                scores[0] += 0.2 * 1.182508735681975
            else:
                scores[0] += 0.2 * -0.80730751288221
    else:
        if  t_minus21 <= 3956.5:
            if  t_minus6 <= 3956.5:
                scores[0] += 0.2 * 0.05406404627005737
            else:
                scores[0] += 0.2 * 1.1761929318007092
        else:
            if  t_minus22 <= 3951.5:
                scores[0] += 0.2 * 8.09946113133831
            else:
                scores[0] += 0.2 * -0.49198111101757397

    if  t_minus19 <= 3953.5:
        if  t_minus23 <= 3955.5:
            if  t_minus13 <= 3956.5:
                scores[0] += 0.2 * -0.032471570447861677
            else:
                scores[0] += 0.2 * 1.3420264357344667
        else:
            if  t_minus15 <= 3942.0:
                scores[0] += 0.2 * -12.92059159733338
            else:
                scores[0] += 0.2 * -0.6170800340344079
    else:
        if  t_minus11 <= 3952.5:
            if  t_minus17 <= 3949.5:
                scores[0] += 0.2 * 2.8125939029422193
            else:
                scores[0] += 0.2 * 0.6947972475379673
        else:
            if  t_minus9 <= 3949.5:
                scores[0] += 0.2 * 2.756840163063267
            else:
                scores[0] += 0.2 * -0.07376056935324617

    if  avedif <= 4.3500001430511475:
        if  t_minus20 <= 3953.5:
            if  t_minus3 <= 3947.5:
                scores[0] += 0.2 * 0.17963800418630155
            else:
                scores[0] += 0.2 * -0.21516740096854925
        else:
            if  t_minus3 <= 3950.5:
                scores[0] += 0.2 * 1.9451731476371874
            else:
                scores[0] += 0.2 * 0.021039271097477434
    else:
        if  t_minus14 <= 3945.5:
            if  t_minus20 <= 3954.5:
                scores[0] += 0.2 * -0.2468240163476745
            else:
                scores[0] += 0.2 * -6.198401993248551
        else:
            if  t_minus12 <= 3951.5:
                scores[0] += 0.2 * 0.8924487325166309
            else:
                scores[0] += 0.2 * -0.2552980504960857

    if  t_minus17 <= 3953.5:
        if t_minus30 <= 3957.5:
            if  t_minus21 <= 3955.5:
                scores[0] += 0.2 * -0.03262928974926808
            else:
                scores[0] += 0.2 * -0.7948071305896801
        else:
            if  avedif <= 1.5166667103767395:
                scores[0] += 0.2 * 2.7284781045673863
            else:
                scores[0] += 0.2 * -0.08985245817294221
    else:
        if  t_minus15 <= 3949.5:
            if  t_minus9 <= 3952.5:
                scores[0] += 0.2 * 3.177591553080553
            else:
                scores[0] += 0.2 * -2.015353567552979
        else:
            if t_minus30 <= 3952.5:
                scores[0] += 0.2 * 0.5274303967347383
            else:
                scores[0] += 0.2 * -0.074931750367365

    if  t_minus10 <= 3956.5:
        if  t_minus27 <= 3956.5:
            if  t_minus19 <= 3959.5:
                scores[0] += 0.2 * -0.04107891427025907
            else:
                scores[0] += 0.2 * -1.746001339028248
        else:
            if  t_minus6 <= 3935.5:
                scores[0] += 0.2 * -1.0810167388412744
            else:
                scores[0] += 0.2 * 0.4320293397202834
    else:
        if  t_minus22 <= 3947.5:
            if  avedif <= 1.2999999821186066:
                scores[0] += 0.2 * -2.682437574818715
            else:
                scores[0] += 0.2 * -0.9791784790128325
        else:
            if  t_minus27 <= 3955.5:
                scores[0] += 0.2 * 0.716935317068009
            else:
                scores[0] += 0.2 * -0.08780160530423778

    if t_minus30 <= 3931.5:
        if  t_minus25 <= 3947.5:
            if  t_minus15 <= 3955.5:
                scores[0] += 0.2 * -0.7743402310152284
            else:
                scores[0] += 0.2 * -2.6648249086551785
        else:
            if  t_minus26 <= 3948.5:
                scores[0] += 0.2 * -1.93443288303615
            else:
                scores[0] += 0.2 * -2.4881269385248723
    else:
        if t_minus30 <= 3940.5:
            if  t_minus19 <= 3947.5:
                scores[0] += 0.2 * 1.3551233763681467
            else:
                scores[0] += 0.2 * 1.2547155004622825
        else:
            if  t_minus13 <= 3925.5:
                scores[0] += 0.2 * 4.139330246930595
            else:
                scores[0] += 0.2 * -0.025302565999705456

    if  t_minus26 <= 3950.5:
        if  t_minus25 <= 3955.5:
            if  t_minus14 <= 3952.5:
                scores[0] += 0.2 * -0.17283976728275124
            else:
                scores[0] += 0.2 * 0.4782594571396589
        else:
            scores[0] += 0.2 * -8.384818839139056
    else:
        if  t_minus11 <= 3949.5:
            if  t_minus13 <= 3953.5:
                scores[0] += 0.2 * 0.6475898988266381
            else:
                scores[0] += 0.2 * 2.882063518599756
        else:
            if  t_minus3 <= 3949.5:
                scores[0] += 0.2 * 0.4924172756225863
            else:
                scores[0] += 0.2 * -0.0997813034549616

    if  t_minus8 <= 3959.5:
        if  t_minus12 <= 3956.5:
            if  t_minus6 <= 3960.5:
                scores[0] += 0.2 * -0.01997873561187056
            else:
                scores[0] += 0.2 * 2.0753895321495515
        else:
            if  t_minus24 <= 3947.5:
                scores[0] += 0.2 * -1.0544711466759225
            else:
                scores[0] += 0.2 * 0.3166542323013416
    else:
        if t_minus30 <= 3952.5:
            if  avedif <= 0.9666666388511658:
                scores[0] += 0.2 * -1.2021729551879932
            else:
                scores[0] += 0.2 * -1.6683098642621024
        else:
            if  t_minus7 <= 3960.5:
                scores[0] += 0.2 * -0.5723237595443169
            else:
                scores[0] += 0.2 * 1.8865675395723065

    if  t_minus29 <= 3958.5:
        if  t_minus6 <= 3960.5:
            if  t_minus5 <= 3960.5:
                scores[0] += 0.2 * 0.0037945385608703463
            else:
                scores[0] += 0.2 * 1.6551807786602282
        else:
            scores[0] += 0.2 * 1.7100677045320773
    else:
        if  t_minus3 <= 3938.5:
            if  avedif <= 12.049999713897705:
                scores[0] += 0.2 * -2.2162404799729676
            else:
                scores[0] += 0.2 * -1.139240274556078
        else:
            if  t_minus26 <= 3955.5:
                scores[0] += 0.2 * 1.4331495152148406
            else:
                scores[0] += 0.2 * -0.8842129662728494

    if  avedif <= 0.6833333373069763:
        if  t_minus1 <= 3940.5:
            if  t_minus8 <= 3942.5:
                scores[0] += 0.2 * 1.493398128614115
            else:
                scores[0] += 0.2 * 48.40379721295182
        else:
            if  t_minus8 <= 3954.5:
                scores[0] += 0.2 * -0.38767718625265735
            else:
                scores[0] += 0.2 * 0.1326738367379015
    else:
        if  t_minus9 <= 3956.5:
            if  t_minus17 <= 3956.5:
                scores[0] += 0.2 * -0.0052020999172723015
            else:
                scores[0] += 0.2 * 0.4481148489056808
        else:
            if  t_minus13 <= 3952.5:
                scores[0] += 0.2 * 1.5964577600837262
            else:
                scores[0] += 0.2 * 0.186633061419326

    if  t_minus3 <= 3957.5:
        if  t_minus3 <= 3956.5:
            if  t_minus20 <= 3957.5:
                scores[0] += 0.2 * -0.03375459454272543
            else:
                scores[0] += 0.2 * 0.6170389275277661
        else:
            if  t_minus6 <= 3950.5:
                scores[0] += 0.2 * 8.818819898920646
            else:
                scores[0] += 0.2 * 0.393962798057834
    else:
        if  t_minus14 <= 3953.5:
            if  avedif <= 5.299999952316284:
                scores[0] += 0.2 * -1.2077239242688182
            else:
                scores[0] += 0.2 * -0.3418093823883311
        else:
            if  t_minus17 <= 3956.5:
                scores[0] += 0.2 * 0.6021638545027778
            else:
                scores[0] += 0.2 * -0.9285211322504872

    if  avedif <= 8.416666507720947:
        if  avedif <= 4.916666746139526:
            if  avedif <= 4.7833335399627686:
                scores[0] += 0.2 * -0.016754303214259053
            else:
                scores[0] += 0.2 * -1.1817861521833763
        else:
            if  t_minus2 <= 3942.5:
                scores[0] += 0.2 * -0.8593300333755323
            else:
                scores[0] += 0.2 * 0.656030721904209
    else:
        if  t_minus18 <= 3957.5:
            if  t_minus25 <= 3957.5:
                scores[0] += 0.2 * -0.08924530928605992
            else:
                scores[0] += 0.2 * -1.546105627974005
        else:
            if  t_minus12 <= 3956.5:
                scores[0] += 0.2 * -1.8320032462947
            else:
                scores[0] += 0.2 * -0.44864939452166863

    if  t_minus29 <= 3932.5:
        if  t_minus7 <= 3954.5:
            if  t_minus15 <= 3950.5:
                scores[0] += 0.2 * -1.1674346231113355
            else:
                scores[0] += 0.2 * 1.629603799348292
        else:
            if  t_minus21 <= 3950.5:
                scores[0] += 0.2 * -1.9856074433195203
            else:
                scores[0] += 0.2 * -2.920605055996814
    else:
        if  t_minus29 <= 3939.5:
            if  t_minus25 <= 3947.5:
                scores[0] += 0.2 * 1.174243516204298
            else:
                scores[0] += 0.2 * 1.788989830854212
        else:
            if  t_minus23 <= 3928.0:
                scores[0] += 0.2 * 5.4271319350088545
            else:
                scores[0] += 0.2 * -0.015867660900284433

    if t_minus30 <= 3945.5:
        if  t_minus27 <= 3952.5:
            if  t_minus11 <= 3951.5:
                scores[0] += 0.2 * -0.4090073680264197
            else:
                scores[0] += 0.2 * 0.323298762031462
        else:
            if  t_minus9 <= 3957.5:
                scores[0] += 0.2 * -3.4700621234579163
            else:
                scores[0] += 0.2 * -1.0810762573477768
    else:
        if  t_minus4 <= 3946.5:
            if  t_minus29 <= 3948.5:
                scores[0] += 0.2 * 0.09520317008124153
            else:
                scores[0] += 0.2 * 0.7676733043823274
        else:
            if  t_minus7 <= 3945.5:
                scores[0] += 0.2 * 1.7441116442428923
            else:
                scores[0] += 0.2 * -0.049895702160988764

    if  avedif <= 8.416666507720947:
        if  avedif <= 7.483333349227905:
            if  avedif <= 7.3500001430511475:
                scores[0] += 0.2 * 0.006431361692998116
            else:
                scores[0] += 0.2 * -2.3881369488300184
        else:
            if  t_minus4 <= 3953.5:
                scores[0] += 0.2 * 1.2515900842562584
            else:
                scores[0] += 0.2 * -0.9805657678819507
    else:
        if  t_minus11 <= 3954.5:
            if  avedif <= 8.449999809265137:
                scores[0] += 0.2 * -18.135494937606563
            else:
                scores[0] += 0.2 * -0.06603868193725018
        else:
            if  t_minus4 <= 3942.0:
                scores[0] += 0.2 * -3.1716369964867837
            else:
                scores[0] += 0.2 * -0.5302142046322423

    if  t_minus24 <= 3950.5:
        if  t_minus21 <= 3955.5:
            if  t_minus27 <= 3954.5:
                scores[0] += 0.2 * -0.09836592689212624
            else:
                scores[0] += 0.2 * 1.3600999129848417
        else:
            if  t_minus21 <= 3956.5:
                scores[0] += 0.2 * -5.694336436188029
            else:
                scores[0] += 0.2 * -0.828048213858321
    else:
        if  t_minus7 <= 3951.5:
            if  t_minus23 <= 3952.5:
                scores[0] += 0.2 * 0.05397169984862236
            else:
                scores[0] += 0.2 * 0.8720094740486639
        else:
            if t_minus30 <= 3949.5:
                scores[0] += 0.2 * 0.9093954855017142
            else:
                scores[0] += 0.2 * -0.1564415243422556

    if  t_minus2 <= 3959.5:
        if  t_minus7 <= 3956.5:
            if  t_minus24 <= 3957.5:
                scores[0] += 0.2 * -0.029171787002717504
            else:
                scores[0] += 0.2 * 0.46592288742374155
        else:
            if  t_minus15 <= 3954.5:
                scores[0] += 0.2 * 0.7537584312140626
            else:
                scores[0] += 0.2 * 0.05097591832797861
    else:
        if  t_minus28 <= 3947.0:
            if  t_minus23 <= 3950.5:
                scores[0] += 0.2 * -1.480533440528084
            else:
                scores[0] += 0.2 * -1.331282269419876
        else:
            if  t_minus12 <= 3952.0:
                scores[0] += 0.2 * 1.555016298087292
            else:
                scores[0] += 0.2 * -0.7369597912401248

    if  t_minus27 <= 3958.5:
        if  t_minus10 <= 3956.5:
            if  t_minus8 <= 3959.5:
                scores[0] += 0.2 * -0.009408195618968681
            else:
                scores[0] += 0.2 * -1.3870822559740557
        else:
            if  t_minus22 <= 3947.5:
                scores[0] += 0.2 * -1.129056015932781
            else:
                scores[0] += 0.2 * 0.29080428155160043
    else:
        if  t_minus9 <= 3939.5:
            if  t_minus4 <= 3934.0:
                scores[0] += 0.2 * -1.7808959486335119
            else:
                scores[0] += 0.2 * -1.808412325334745
        else:
            if  t_minus17 <= 3954.5:
                scores[0] += 0.2 * 0.9388304127844557
            else:
                scores[0] += 0.2 * -0.7257969999219795

    if  t_minus23 <= 3959.5:
        if  t_minus11 <= 3956.5:
            if  t_minus23 <= 3958.5:
                scores[0] += 0.2 * -0.020447597872447862
            else:
                scores[0] += 0.2 * 1.2224641162900491
        else:
            if  t_minus26 <= 3947.5:
                scores[0] += 0.2 * -1.0702036393994294
            else:
                scores[0] += 0.2 * 0.2820064746440206
    else:
        if  t_minus4 <= 3952.5:
            if  t_minus6 <= 3940.0:
                scores[0] += 0.2 * -1.75864090372995
            else:
                scores[0] += 0.2 * -1.3237680043288318
        else:
            if  t_minus20 <= 3955.5:
                scores[0] += 0.2 * 0.8474543899040717
            else:
                scores[0] += 0.2 * -1.0825605380026873

    if  t_minus10 <= 3957.5:
        if  t_minus10 <= 3956.5:
            if t_minus30 <= 3957.5:
                scores[0] += 0.2 * -0.02192072230806776
            else:
                scores[0] += 0.2 * 0.45257227680655143
        else:
            if  t_minus1 <= 3950.5:
                scores[0] += 0.2 * 1.2348762385165517
            else:
                scores[0] += 0.2 * 0.23231496956867587
    else:
        if  t_minus15 <= 3955.5:
            if  t_minus9 <= 3953.5:
                scores[0] += 0.2 * 13.465551355797038
            else:
                scores[0] += 0.2 * 0.5048178273058912
        else:
            if  t_minus24 <= 3945.0:
                scores[0] += 0.2 * -1.5273862563374636
            else:
                scores[0] += 0.2 * -0.691608347054869

    if  avedif <= 0.01666666753590107:
        if  t_minus10 <= 3955.5:
            if  t_minus23 <= 3951.5:
                scores[0] += 0.2 * -1.0187120659529678
            else:
                scores[0] += 0.2 * -1.0533797300854455
        else:
            if  t_minus29 <= 3954.0:
                scores[0] += 0.2 * -1.2394921694419125
            else:
                scores[0] += 0.2 * -1.0991879819009065
    else:
        if  t_minus28 <= 3958.5:
            if  t_minus16 <= 3955.5:
                scores[0] += 0.2 * -0.01575661938145541
            else:
                scores[0] += 0.2 * 0.12702929755519726
        else:
            if  t_minus3 <= 3933.5:
                scores[0] += 0.2 * -2.5448769016105053
            else:
                scores[0] += 0.2 * -0.4730393782119536

    if  t_minus28 <= 3955.5:
        if  t_minus19 <= 3957.5:
            if  t_minus22 <= 3959.5:
                scores[0] += 0.2 * 0.005778085601167822
            else:
                scores[0] += 0.2 * 4.830350646712625
        else:
            if t_minus30 <= 3956.5:
                scores[0] += 0.2 * 1.063318967020548
            else:
                scores[0] += 0.2 * -1.0865073880145757
    else:
        if  t_minus29 <= 3949.5:
            scores[0] += 0.2 * -18.741340289421032
        else:
            if  t_minus20 <= 3942.0:
                scores[0] += 0.2 * -2.285971868402634
            else:
                scores[0] += 0.2 * -0.07565941964656676

    if  t_minus1 <= 3955.5:
        if  t_minus10 <= 3958.5:
            if  t_minus21 <= 3957.5:
                scores[0] += 0.2 * 0.017594082729238913
            else:
                scores[0] += 0.2 * 0.700135980258664
        else:
            if  t_minus23 <= 3957.5:
                scores[0] += 0.2 * -1.273127596256463
            else:
                scores[0] += 0.2 * -1.0518426450700715
    else:
        if  t_minus11 <= 3953.5:
            if  t_minus15 <= 3939.5:
                scores[0] += 0.2 * 1.1781370443462218
            else:
                scores[0] += 0.2 * -0.5709049201789556
        else:
            if  t_minus24 <= 3952.5:
                scores[0] += 0.2 * 0.6850061561614371
            else:
                scores[0] += 0.2 * -0.11331734820881212

    if  t_minus19 <= 3958.5:
        if  t_minus4 <= 3956.5:
            if  t_minus4 <= 3953.5:
                scores[0] += 0.2 * 0.03854310654604102
            else:
                scores[0] += 0.2 * -0.14165595148021148
        else:
            if  t_minus23 <= 3946.5:
                scores[0] += 0.2 * -0.79747725336242
            else:
                scores[0] += 0.2 * 0.29762046080801746
    else:
        if  t_minus4 <= 3951.5:
            if  t_minus9 <= 3954.5:
                scores[0] += 0.2 * 1.0629728876712208
            else:
                scores[0] += 0.2 * -2.190883937642008
        else:
            if  t_minus5 <= 3953.5:
                scores[0] += 0.2 * 2.1621829437505005
            else:
                scores[0] += 0.2 * -0.5733768788841577

    if  t_minus21 <= 3959.5:
        if  t_minus12 <= 3936.5:
            if  t_minus23 <= 3954.5:
                scores[0] += 0.2 * -0.6654804858162356
            else:
                scores[0] += 0.2 * -3.3004828130323114
        else:
            if  t_minus10 <= 3940.5:
                scores[0] += 0.2 * 1.3229723471107462
            else:
                scores[0] += 0.2 * -0.010911443632550309
    else:
        if  avedif <= 14.016666412353516:
            if  t_minus14 <= 3953.0:
                scores[0] += 0.2 * 1.5523097144025888
            else:
                scores[0] += 0.2 * -0.7737911006113194
        else:
            if  t_minus14 <= 3954.5:
                scores[0] += 0.2 * -2.4133108052247585
            else:
                scores[0] += 0.2 * -1.8855042408191305

    if  t_minus3 <= 3959.5:
        if  t_minus8 <= 3956.5:
            if  t_minus25 <= 3957.5:
                scores[0] += 0.2 * -0.02602388764675994
            else:
                scores[0] += 0.2 * 0.5010033221213749
        else:
            if  t_minus13 <= 3952.5:
                scores[0] += 0.2 * 1.2289348532446533
            else:
                scores[0] += 0.2 * 0.08649484589036927
    else:
        if  t_minus10 <= 3955.5:
            if t_minus30 <= 3954.0:
                scores[0] += 0.2 * -1.2733534238838993
            else:
                scores[0] += 0.2 * -1.0633720825704296
        else:
            if  t_minus6 <= 3948.5:
                scores[0] += 0.2 * -1.1385471911815703
            else:
                scores[0] += 0.2 * -0.710786762154631

    if  t_minus29 <= 3958.5:
        if  t_minus2 <= 3958.5:
            if  t_minus12 <= 3956.5:
                scores[0] += 0.2 * -0.006614494664068291
            else:
                scores[0] += 0.2 * 0.22470548993067527
        else:
            if  avedif <= 0.15000000596046448:
                scores[0] += 0.2 * 1.983377921625416
            else:
                scores[0] += 0.2 * -0.7776644275687605
    else:
        if  t_minus3 <= 3938.5:
            if  t_minus3 <= 3934.0:
                scores[0] += 0.2 * -1.1066032507572119
            else:
                scores[0] += 0.2 * -1.8205629357287927
        else:
            if  t_minus26 <= 3955.5:
                scores[0] += 0.2 * 0.9739404378116814
            else:
                scores[0] += 0.2 * -0.8477203493107963

    if  t_minus8 <= 3950.5:
        if  t_minus11 <= 3952.5:
            if  t_minus3 <= 3952.5:
                scores[0] += 0.2 * -0.04925586460018949
            else:
                scores[0] += 0.2 * 1.759754067643352
        else:
            if  t_minus25 <= 3950.5:
                scores[0] += 0.2 * 2.5987643804996012
            else:
                scores[0] += 0.2 * 0.4217285227294689
    else:
        if  t_minus9 <= 3945.5:
            scores[0] += 0.2 * 27.535603602685132
        else:
            if  t_minus29 <= 3949.5:
                scores[0] += 0.2 * 0.22937098975787212
            else:
                scores[0] += 0.2 * -0.12503196241370865

    if  avedif <= 8.449999809265137:
        if  avedif <= 4.3500001430511475:
            if  avedif <= 4.2833335399627686:
                scores[0] += 0.2 * -0.010928847868337251
            else:
                scores[0] += 0.2 * -1.6202725139961882
        else:
            if  t_minus20 <= 3951.5:
                scores[0] += 0.2 * 0.5137406083607288
            else:
                scores[0] += 0.2 * -0.643021698866793
    else:
        if  t_minus11 <= 3954.5:
            if  t_minus29 <= 3949.5:
                scores[0] += 0.2 * -0.7938341928319614
            else:
                scores[0] += 0.2 * 0.54240750861328
        else:
            if  t_minus4 <= 3942.0:
                scores[0] += 0.2 * -2.4888373209441084
            else:
                scores[0] += 0.2 * -0.6365600956216926

    if  t_minus24 <= 3950.5:
        if  t_minus27 <= 3954.5:
            if  t_minus26 <= 3955.5:
                scores[0] += 0.2 * -0.09727546148514551
            else:
                scores[0] += 0.2 * -9.602468733358544
        else:
            if  avedif <= 0.8166666626930237:
                scores[0] += 0.2 * 9.670359714180094
            else:
                scores[0] += 0.2 * 0.181463610649343
    else:
        if  t_minus3 <= 3949.5:
            if  t_minus1 <= 3943.5:
                scores[0] += 0.2 * -0.4432389716777555
            else:
                scores[0] += 0.2 * 0.8561158104665837
        else:
            if  t_minus6 <= 3946.0:
                scores[0] += 0.2 * 3.665002892526133
            else:
                scores[0] += 0.2 * -0.031726008676413335

    if  t_minus17 <= 3953.5:
        if  t_minus21 <= 3955.5:
            if  t_minus18 <= 3957.5:
                scores[0] += 0.2 * -0.02057260470667442
            else:
                scores[0] += 0.2 * 3.8014246136125105
        else:
            if  t_minus24 <= 3949.5:
                scores[0] += 0.2 * -2.5416046435544626
            else:
                scores[0] += 0.2 * -0.6163740928231576
    else:
        if t_minus30 <= 3952.5:
            if  t_minus10 <= 3950.5:
                scores[0] += 0.2 * 1.8271861892213
            else:
                scores[0] += 0.2 * 0.3592328459091751
        else:
            if  t_minus9 <= 3942.5:
                scores[0] += 0.2 * -3.372807645076647
            else:
                scores[0] += 0.2 * -0.05033029233589677

    if  t_minus15 <= 3953.5:
        if  t_minus16 <= 3957.5:
            if  t_minus1 <= 3954.5:
                scores[0] += 0.2 * -0.006603819176117311
            else:
                scores[0] += 0.2 * -0.34838500689980106
        else:
            if  t_minus12 <= 3957.0:
                scores[0] += 0.2 * 1.1508437444606467
            else:
                scores[0] += 0.2 * 7.725559317100127
    else:
        if  t_minus13 <= 3949.5:
            if  t_minus9 <= 3953.5:
                scores[0] += 0.2 * 3.6864316802093215
            else:
                scores[0] += 0.2 * -2.211670749833646
        else:
            if  t_minus29 <= 3952.5:
                scores[0] += 0.2 * 0.5202051203996833
            else:
                scores[0] += 0.2 * -0.09762483714193324

    if  t_minus5 <= 3956.5:
        if  t_minus22 <= 3956.5:
            if  t_minus17 <= 3959.5:
                scores[0] += 0.2 * -0.03701432410094025
            else:
                scores[0] += 0.2 * -1.058148534891887
        else:
            if  t_minus12 <= 3955.5:
                scores[0] += 0.2 * -0.26040321875792155
            else:
                scores[0] += 0.2 * 0.6916841433090553
    else:
        if  t_minus24 <= 3946.5:
            if  t_minus17 <= 3937.0:
                scores[0] += 0.2 * 1.768523948565649
            else:
                scores[0] += 0.2 * -1.1991611974985685
        else:
            if  t_minus24 <= 3952.5:
                scores[0] += 0.2 * 1.451642803839266
            else:
                scores[0] += 0.2 * 0.16410962952828922

    if  t_minus4 <= 3959.5:
        if  t_minus9 <= 3956.5:
            if  t_minus26 <= 3956.5:
                scores[0] += 0.2 * -0.03856490006423055
            else:
                scores[0] += 0.2 * 0.37695100214761634
        else:
            if  t_minus13 <= 3952.5:
                scores[0] += 0.2 * 1.3268270859107134
            else:
                scores[0] += 0.2 * 0.10799636714134879
    else:
        if  t_minus28 <= 3942.5:
            if  t_minus11 <= 3953.5:
                scores[0] += 0.2 * -1.8108988178325898
            else:
                scores[0] += 0.2 * -1.1593186502817
        else:
            if  t_minus10 <= 3951.5:
                scores[0] += 0.2 * 1.1993311143192205
            else:
                scores[0] += 0.2 * -0.8978509838483091

    if  avedif <= 3.950000047683716:
        if  avedif <= 3.1166666746139526:
            if  t_minus21 <= 3953.5:
                scores[0] += 0.2 * -0.0747173360541182
            else:
                scores[0] += 0.2 * 0.14688579669544866
        else:
            if  t_minus28 <= 3952.5:
                scores[0] += 0.2 * -0.022636528618659543
            else:
                scores[0] += 0.2 * -0.7927477888400096
    else:
        if  t_minus3 <= 3953.5:
            if  t_minus1 <= 3950.5:
                scores[0] += 0.2 * 0.036479885724845604
            else:
                scores[0] += 0.2 * 1.3171020324181553
        else:
            if  t_minus4 <= 3955.5:
                scores[0] += 0.2 * -0.8926951101980269
            else:
                scores[0] += 0.2 * 0.030735472026452652

    if  avedif <= 0.6833333373069763:
        if  t_minus21 <= 3956.5:
            if  t_minus16 <= 3955.5:
                scores[0] += 0.2 * -0.19935294748256072
            else:
                scores[0] += 0.2 * 0.43161193118670527
        else:
            if  t_minus29 <= 3946.0:
                scores[0] += 0.2 * -3.5115680412823616
            else:
                scores[0] += 0.2 * -0.4338653208904621
    else:
        if  t_minus8 <= 3958.5:
            if  t_minus9 <= 3956.5:
                scores[0] += 0.2 * 0.023752251177083634
            else:
                scores[0] += 0.2 * 0.320141862005439
        else:
            if  t_minus25 <= 3944.0:
                scores[0] += 0.2 * -1.6177117244072223
            else:
                scores[0] += 0.2 * -0.5832651174821165

    if  t_minus24 <= 3959.5:
        if  t_minus18 <= 3959.5:
            if t_minus30 <= 3957.5:
                scores[0] += 0.2 * -0.0030542249704589553
            else:
                scores[0] += 0.2 * 0.2606190353996615
        else:
            if  t_minus12 <= 3954.5:
                scores[0] += 0.2 * -1.4350741358087262
            else:
                scores[0] += 0.2 * -0.5564317244373272
    else:
        if  avedif <= 14.116666316986084:
            if  avedif <= 2.350000023841858:
                scores[0] += 0.2 * -0.49979625446026876
            else:
                scores[0] += 0.2 * -1.0563909090041819
        else:
            scores[0] += 0.2 * -1.54006282811818

    if  t_minus27 <= 3958.5:
        if  t_minus27 <= 3957.5:
            if  t_minus15 <= 3959.5:
                scores[0] += 0.2 * -0.0005736440616167258
            else:
                scores[0] += 0.2 * -0.7874092232227021
        else:
            if  t_minus23 <= 3955.5:
                scores[0] += 0.2 * 1.4199311853415628
            else:
                scores[0] += 0.2 * -0.3581957216021685
    else:
        if  t_minus19 <= 3949.5:
            if  t_minus19 <= 3939.5:
                scores[0] += 0.2 * -1.259742962412666
            else:
                scores[0] += 0.2 * -1.5243748163524968
        else:
            if  t_minus17 <= 3954.5:
                scores[0] += 0.2 * 0.7255963003154803
            else:
                scores[0] += 0.2 * -0.7425816120830963

    if  t_minus8 <= 3950.5:
        if  t_minus7 <= 3955.5:
            if  t_minus10 <= 3953.5:
                scores[0] += 0.2 * 0.03182147155607726
            else:
                scores[0] += 0.2 * 1.2534291879075767
        else:
            if  t_minus8 <= 3949.0:
                scores[0] += 0.2 * 23.840902732852367
            else:
                scores[0] += 0.2 * 2.83210102615455
    else:
        if t_minus30 <= 3949.5:
            if  t_minus10 <= 3955.5:
                scores[0] += 0.2 * 0.3380042826839439
            else:
                scores[0] += 0.2 * -0.6974369649423302
        else:
            if  t_minus19 <= 3953.5:
                scores[0] += 0.2 * -0.32229528215747943
            else:
                scores[0] += 0.2 * 0.01895153206847961

    if t_minus30 <= 3948.5:
        if  t_minus12 <= 3951.5:
            if  t_minus14 <= 3952.5:
                scores[0] += 0.2 * -0.3031016094124512
            else:
                scores[0] += 0.2 * 0.8263917238584907
        else:
            if  t_minus9 <= 3954.5:
                scores[0] += 0.2 * 0.8338486305488314
            else:
                scores[0] += 0.2 * -0.497894430505265
    else:
        if  t_minus3 <= 3946.5:
            if  avedif <= 3.1333333253860474:
                scores[0] += 0.2 * 1.9068479712893722
            else:
                scores[0] += 0.2 * -0.16206426878646626
        else:
            if  t_minus6 <= 3945.5:
                scores[0] += 0.2 * 1.9706732681878172
            else:
                scores[0] += 0.2 * -0.04461915936820473

    if  avedif <= 17.983333587646484:
        if  avedif <= 16.449999809265137:
            if  t_minus8 <= 3956.5:
                scores[0] += 0.2 * -0.015618956185846213
            else:
                scores[0] += 0.2 * 0.13034826186311982
        else:
            if  t_minus15 <= 3951.0:
                scores[0] += 0.2 * 0.2543596002915727
            else:
                scores[0] += 0.2 * -1.4733013838408202
    else:
        if  t_minus13 <= 3956.5:
            if  t_minus7 <= 3948.0:
                scores[0] += 0.2 * 1.0784212392561565
            else:
                scores[0] += 0.2 * 1.2106257004727081
        else:
            scores[0] += 0.2 * -1.2997400359261584

    if t_minus30 <= 3958.5:
        if t_minus30 <= 3957.5:
            if  t_minus13 <= 3956.5:
                scores[0] += 0.2 * -0.030202258031483437
            else:
                scores[0] += 0.2 * 0.25889498767363156
        else:
            if  t_minus26 <= 3955.5:
                scores[0] += 0.2 * 1.2664219002785313
            else:
                scores[0] += 0.2 * -0.31374691268247595
    else:
        if  t_minus18 <= 3952.5:
            if  t_minus1 <= 3956.5:
                scores[0] += 0.2 * -1.0063535916281403
            else:
                scores[0] += 0.2 * 2.324012612652956
        else:
            if  t_minus5 <= 3956.5:
                scores[0] += 0.2 * -1.168221059271178
            else:
                scores[0] += 0.2 * -0.5258431016932824

    if  t_minus1 <= 3955.5:
        if  t_minus18 <= 3956.5:
            if  t_minus19 <= 3958.5:
                scores[0] += 0.2 * -0.0010922469204654416
            else:
                scores[0] += 0.2 * 1.981679760006501
        else:
            if  avedif <= 1.9166666269302368:
                scores[0] += 0.2 * 0.9323519097017616
            else:
                scores[0] += 0.2 * -0.159902310863693
    else:
        if  t_minus29 <= 3931.0:
            if  t_minus18 <= 3946.5:
                scores[0] += 0.2 * -1.2969775692877534
            else:
                scores[0] += 0.2 * 1.6891386355249909
        else:
            if  t_minus26 <= 3945.5:
                scores[0] += 0.2 * -0.8362267431432245
            else:
                scores[0] += 0.2 * -0.0640021106135332

    if  avedif <= 3.950000047683716:
        if  avedif <= 3.816666603088379:
            if  t_minus7 <= 3941.5:
                scores[0] += 0.2 * 0.6377006766706173
            else:
                scores[0] += 0.2 * -0.048855347995310265
        else:
            if  t_minus1 <= 3954.5:
                scores[0] += 0.2 * -0.5343233032726626
            else:
                scores[0] += 0.2 * -2.3521863101432054
    else:
        if  t_minus17 <= 3951.5:
            if  t_minus19 <= 3947.5:
                scores[0] += 0.2 * -0.12174271208295298
            else:
                scores[0] += 0.2 * 0.7851363665808603
        else:
            if  t_minus13 <= 3944.5:
                scores[0] += 0.2 * -4.634816089926171
            else:
                scores[0] += 0.2 * -0.2210247857883007

    if  t_minus3 <= 3957.5:
        if  t_minus3 <= 3956.5:
            if  t_minus20 <= 3957.5:
                scores[0] += 0.2 * -0.022778218014452522
            else:
                scores[0] += 0.2 * 0.4789655319192846
        else:
            if  t_minus28 <= 3952.5:
                scores[0] += 0.2 * 1.0362458595345594
            else:
                scores[0] += 0.2 * 0.1719127336349388
    else:
        if  t_minus2 <= 3953.5:
            if  t_minus12 <= 3957.5:
                scores[0] += 0.2 * 8.81426697551494
            else:
                scores[0] += 0.2 * -1.155372840813106
        else:
            if  t_minus14 <= 3954.5:
                scores[0] += 0.2 * -0.8018954890396592
            else:
                scores[0] += 0.2 * -0.13729270311414335

    if  avedif <= 0.6833333373069763:
        if  t_minus23 <= 3955.5:
            if t_minus30 <= 3957.5:
                scores[0] += 0.2 * -0.09578664363378403
            else:
                scores[0] += 0.2 * 1.886097926208279
        else:
            if  t_minus29 <= 3946.0:
                scores[0] += 0.2 * -2.176072689863434
            else:
                scores[0] += 0.2 * -0.3246776800876668
    else:
        if  t_minus14 <= 3958.5:
            if  t_minus11 <= 3956.5:
                scores[0] += 0.2 * 0.020056496541711207
            else:
                scores[0] += 0.2 * 0.29371255095751614
        else:
            if  t_minus10 <= 3955.5:
                scores[0] += 0.2 * -1.264329839059601
            else:
                scores[0] += 0.2 * -0.4954518285603956

    if t_minus30 <= 3935.5:
        if  t_minus15 <= 3955.5:
            if  t_minus15 <= 3950.5:
                scores[0] += 0.2 * -1.19576737230285
            else:
                scores[0] += 0.2 * 1.0480227071912445
        else:
            if  t_minus19 <= 3956.0:
                scores[0] += 0.2 * -2.0274396417678666
            else:
                scores[0] += 0.2 * -1.9229153357175954
    else:
        if  t_minus26 <= 3939.5:
            if  t_minus20 <= 3947.5:
                scores[0] += 0.2 * 1.409350209719015
            else:
                scores[0] += 0.2 * 2.1276454179738
        else:
            if  t_minus21 <= 3927.5:
                scores[0] += 0.2 * 2.8114157773671207
            else:
                scores[0] += 0.2 * -0.015721142151822104

    if  t_minus25 <= 3950.5:
        if  t_minus11 <= 3952.5:
            if  t_minus19 <= 3955.5:
                scores[0] += 0.2 * -0.17300064555505246
            else:
                scores[0] += 0.2 * 1.9138282170322682
        else:
            if  t_minus3 <= 3953.5:
                scores[0] += 0.2 * 0.9293856163212694
            else:
                scores[0] += 0.2 * -0.33684841958853534
    else:
        if  t_minus4 <= 3950.5:
            if  t_minus3 <= 3953.5:
                scores[0] += 0.2 * 0.40566338220993264
            else:
                scores[0] += 0.2 * 3.009135585028086
        else:
            if  t_minus13 <= 3945.5:
                scores[0] += 0.2 * 5.416946245059415
            else:
                scores[0] += 0.2 * -0.08446469163102058

    if  t_minus5 <= 3956.5:
        if  t_minus5 <= 3955.5:
            if  t_minus11 <= 3957.5:
                scores[0] += 0.2 * 0.020220700479119
            else:
                scores[0] += 0.2 * -0.8154507623140468
        else:
            if  t_minus7 <= 3950.5:
                scores[0] += 0.2 * 2.873975733251451
            else:
                scores[0] += 0.2 * -0.2461272276899931
    else:
        if  t_minus2 <= 3950.5:
            if  t_minus17 <= 3954.5:
                scores[0] += 0.2 * 2.001242462437179
            else:
                scores[0] += 0.2 * -1.1531168198982682
        else:
            if  t_minus24 <= 3946.5:
                scores[0] += 0.2 * -0.7956090473688178
            else:
                scores[0] += 0.2 * 0.16181492639203052

    if  t_minus7 <= 3956.5:
        if  t_minus5 <= 3955.5:
            if  t_minus22 <= 3957.5:
                scores[0] += 0.2 * 0.0025018931955708276
            else:
                scores[0] += 0.2 * 0.6276476915078513
        else:
            if  t_minus1 <= 3947.5:
                scores[0] += 0.2 * 1.8796630264844976
            else:
                scores[0] += 0.2 * -0.2315595539408332
    else:
        if  t_minus24 <= 3955.5:
            if  t_minus18 <= 3955.5:
                scores[0] += 0.2 * 0.8748413081333734
            else:
                scores[0] += 0.2 * -0.1385453762929794
        else:
            if  t_minus25 <= 3951.5:
                scores[0] += 0.2 * 1.7390611008399537
            else:
                scores[0] += 0.2 * -0.18946753324560062

    if  t_minus24 <= 3950.5:
        if  t_minus3 <= 3951.5:
            if  t_minus29 <= 3954.5:
                scores[0] += 0.2 * -0.24692572813924166
            else:
                scores[0] += 0.2 * 1.0424726328355753
        else:
            if  t_minus9 <= 3955.5:
                scores[0] += 0.2 * 0.5633869570052438
            else:
                scores[0] += 0.2 * -0.6117789942517743
    else:
        if  t_minus5 <= 3932.5:
            if  t_minus23 <= 3950.5:
                scores[0] += 0.2 * 1.4924492973905208
            else:
                scores[0] += 0.2 * 1.1809539055655665
        else:
            if  t_minus15 <= 3939.5:
                scores[0] += 0.2 * -2.506847961101551
            else:
                scores[0] += 0.2 * 0.04368178991413945

    if  t_minus6 <= 3956.5:
        if  t_minus29 <= 3956.5:
            if  t_minus14 <= 3957.5:
                scores[0] += 0.2 * -0.04163605152368131
            else:
                scores[0] += 0.2 * 0.6743177532920253
        else:
            if  t_minus27 <= 3949.5:
                scores[0] += 0.2 * 19.654507184376143
            else:
                scores[0] += 0.2 * 0.17467685962787616
    else:
        if  t_minus1 <= 3953.5:
            if  avedif <= 1.100000023841858:
                scores[0] += 0.2 * 3.180300568702022
            else:
                scores[0] += 0.2 * 0.46827068855126075
        else:
            if  t_minus19 <= 3949.5:
                scores[0] += 0.2 * -1.0198006143806442
            else:
                scores[0] += 0.2 * 0.09852461231186496

    if  t_minus28 <= 3955.5:
        if  t_minus17 <= 3955.5:
            if  t_minus22 <= 3957.5:
                scores[0] += 0.2 * -0.025496589328404883
            else:
                scores[0] += 0.2 * 1.3125872478582268
        else:
            if  t_minus12 <= 3942.0:
                scores[0] += 0.2 * -16.75851895509044
            else:
                scores[0] += 0.2 * 0.29306041482774625
    else:
        if  t_minus19 <= 3944.5:
            if  t_minus26 <= 3951.5:
                scores[0] += 0.2 * 1.2861101211775792
            else:
                scores[0] += 0.2 * -1.7590248046762889
        else:
            if  t_minus3 <= 3952.5:
                scores[0] += 0.2 * 0.5011885122908183
            else:
                scores[0] += 0.2 * -0.1965196314363844

    if  t_minus23 <= 3955.5:
        if  t_minus28 <= 3957.5:
            if  t_minus18 <= 3957.5:
                scores[0] += 0.2 * -0.0020428083689308083
            else:
                scores[0] += 0.2 * 0.9031777837546272
        else:
            if  t_minus19 <= 3952.5:
                scores[0] += 0.2 * -1.7245854617931093
            else:
                scores[0] += 0.2 * 1.0886198596203027
    else:
        if  t_minus15 <= 3944.5:
            if  t_minus27 <= 3956.0:
                scores[0] += 0.2 * -3.7759419322235797
            else:
                scores[0] += 0.2 * 0.3868209719158109
        else:
            if  t_minus11 <= 3951.5:
                scores[0] += 0.2 * 1.1875393204821947
            else:
                scores[0] += 0.2 * -0.177279560851347

    if  avedif <= 8.21666669845581:
        if  avedif <= 7.483333349227905:
            if  avedif <= 7.383333444595337:
                scores[0] += 0.2 * 0.006901186682438065
            else:
                scores[0] += 0.2 * -2.4803971193624608
        else:
            if  t_minus27 <= 3943.5:
                scores[0] += 0.2 * 2.0517519359276317
            else:
                scores[0] += 0.2 * -0.1940957963559912
    else:
        if  t_minus18 <= 3957.5:
            if  t_minus25 <= 3957.5:
                scores[0] += 0.2 * -0.12963091063579602
            else:
                scores[0] += 0.2 * -1.2445300508253123
        else:
            if  t_minus9 <= 3953.5:
                scores[0] += 0.2 * 1.1563339218452102
            else:
                scores[0] += 0.2 * -1.4412900973178633

    if  t_minus29 <= 3958.5:
        if  t_minus24 <= 3959.5:
            if  t_minus29 <= 3957.5:
                scores[0] += 0.2 * 0.0009668105981260348
            else:
                scores[0] += 0.2 * 0.34042566800014706
        else:
            if  avedif <= 14.116666316986084:
                scores[0] += 0.2 * -1.0080110822090915
            else:
                scores[0] += 0.2 * -1.5412663862540008
    else:
        if  t_minus3 <= 3938.5:
            if  t_minus6 <= 3934.0:
                scores[0] += 0.2 * -1.7750769129048714
            else:
                scores[0] += 0.2 * -1.1830755787565277
        else:
            if  t_minus26 <= 3955.5:
                scores[0] += 0.2 * 0.6557692441868681
            else:
                scores[0] += 0.2 * -0.90221401276119

    if  t_minus7 <= 3948.5:
        if  t_minus10 <= 3952.5:
            if  t_minus6 <= 3955.5:
                scores[0] += 0.2 * 0.08145512941336559
            else:
                scores[0] += 0.2 * 3.351094496452404
        else:
            if  t_minus28 <= 3950.5:
                scores[0] += 0.2 * 1.6243860829672194
            else:
                scores[0] += 0.2 * -0.0896805946157924
    else:
        if  t_minus1 <= 3947.5:
            if  t_minus4 <= 3952.5:
                scores[0] += 0.2 * -0.5684339275738409
            else:
                scores[0] += 0.2 * 1.4987158356695018
        else:
            if  t_minus6 <= 3945.5:
                scores[0] += 0.2 * 6.102819296300782
            else:
                scores[0] += 0.2 * -0.015498695454440955

    if  t_minus21 <= 3959.5:
        if  t_minus8 <= 3956.5:
            if  t_minus25 <= 3957.5:
                scores[0] += 0.2 * -0.01928378603782036
            else:
                scores[0] += 0.2 * 0.3741113472001116
        else:
            if  t_minus13 <= 3952.5:
                scores[0] += 0.2 * 1.036111989090395
            else:
                scores[0] += 0.2 * 0.04691344408918869
    else:
        if  t_minus1 <= 3938.5:
            if  t_minus24 <= 3958.0:
                scores[0] += 0.2 * -1.82642351993263
            else:
                scores[0] += 0.2 * -1.5538064787745256
        else:
            if  t_minus14 <= 3953.0:
                scores[0] += 0.2 * 1.2830479763786902
            else:
                scores[0] += 0.2 * -0.7346323787059492

    if  t_minus29 <= 3955.5:
        if  t_minus12 <= 3957.5:
            if  t_minus20 <= 3957.5:
                scores[0] += 0.2 * -0.005073339006094263
            else:
                scores[0] += 0.2 * 0.6988601755884529
        else:
            if  t_minus25 <= 3946.0:
                scores[0] += 0.2 * -1.4817643998735412
            else:
                scores[0] += 0.2 * 0.8904880107893364
    else:
        if  t_minus2 <= 3953.5:
            if  t_minus2 <= 3943.5:
                scores[0] += 0.2 * -0.44652506821923954
            else:
                scores[0] += 0.2 * 0.5970794680713893
        else:
            if  avedif <= 3.399999976158142:
                scores[0] += 0.2 * -0.19853675905651327
            else:
                scores[0] += 0.2 * -1.2319974653810366

    if  t_minus5 <= 3950.5:
        if  t_minus3 <= 3952.5:
            if  t_minus19 <= 3952.5:
                scores[0] += 0.2 * -0.06329757548233049
            else:
                scores[0] += 0.2 * 0.7365323989580652
        else:
            if  t_minus14 <= 3949.5:
                scores[0] += 0.2 * 3.602707274090483
            else:
                scores[0] += 0.2 * 0.7390067132798882
    else:
        if  t_minus10 <= 3946.5:
            if  avedif <= 7.549999952316284:
                scores[0] += 0.2 * 4.535345127142133
            else:
                scores[0] += 0.2 * -0.6320063100889273
        else:
            if  t_minus25 <= 3944.5:
                scores[0] += 0.2 * -0.4072087249435928
            else:
                scores[0] += 0.2 * -0.040880042648271

    if  avedif <= 5.950000047683716:
        if  avedif <= 4.916666746139526:
            if  avedif <= 4.549999952316284:
                scores[0] += 0.2 * -0.0026311056958039864
            else:
                scores[0] += 0.2 * -0.5688461847028131
        else:
            if  t_minus18 <= 3945.5:
                scores[0] += 0.2 * -0.6198876091062312
            else:
                scores[0] += 0.2 * 0.8141958319251641
    else:
        if  t_minus16 <= 3951.5:
            if  t_minus17 <= 3948.5:
                scores[0] += 0.2 * -0.22581063384528394
            else:
                scores[0] += 0.2 * 0.49379541550381595
        else:
            if  t_minus29 <= 3952.5:
                scores[0] += 0.2 * -1.5427017595775296
            else:
                scores[0] += 0.2 * -0.024971898668279105

    if  t_minus5 <= 3959.5:
        if  t_minus5 <= 3956.5:
            if  t_minus1 <= 3955.5:
                scores[0] += 0.2 * 0.012971856904267727
            else:
                scores[0] += 0.2 * -0.17215728357354082
        else:
            if  t_minus22 <= 3956.5:
                scores[0] += 0.2 * 0.2913630437118969
            else:
                scores[0] += 0.2 * -0.29762468401391734
    else:
        if  t_minus10 <= 3941.5:
            scores[0] += 0.2 * -1.432199735653975
        else:
            if  t_minus11 <= 3951.5:
                scores[0] += 0.2 * 1.3375242126680267
            else:
                scores[0] += 0.2 * -0.8668406302134998

    if  avedif <= 0.01666666753590107:
        if  t_minus12 <= 3955.5:
            if  t_minus15 <= 3950.5:
                scores[0] += 0.2 * -1.012059169562266
            else:
                scores[0] += 0.2 * -1.0328185403625483
        else:
            if t_minus30 <= 3952.5:
                scores[0] += 0.2 * -1.1783646117152795
            else:
                scores[0] += 0.2 * -1.0599265087697116
    else:
        if  t_minus23 <= 3959.5:
            if  t_minus6 <= 3956.5:
                scores[0] += 0.2 * -0.005912725050443952
            else:
                scores[0] += 0.2 * 0.13426330197057376
        else:
            if  t_minus8 <= 3952.5:
                scores[0] += 0.2 * -1.3539393161649318
            else:
                scores[0] += 0.2 * -0.5105661098079826

    if  t_minus9 <= 3948.5:
        if  t_minus13 <= 3952.5:
            if  t_minus7 <= 3954.0:
                scores[0] += 0.2 * 0.06039590019644433
            else:
                scores[0] += 0.2 * 3.483045021784851
        else:
            if  t_minus11 <= 3949.5:
                scores[0] += 0.2 * 2.4466152759343966
            else:
                scores[0] += 0.2 * 0.2621782639942405
    else:
        if  t_minus5 <= 3942.0:
            if  t_minus14 <= 3953.0:
                scores[0] += 0.2 * 1.1556029095324085
            else:
                scores[0] += 0.2 * -2.168068570099825
        else:
            if  t_minus4 <= 3941.5:
                scores[0] += 0.2 * -1.1390699338424448
            else:
                scores[0] += 0.2 * -0.027640686498771896

    if  t_minus18 <= 3959.5:
        if  t_minus4 <= 3956.5:
            if  t_minus21 <= 3956.5:
                scores[0] += 0.2 * -0.027826518858996674
            else:
                scores[0] += 0.2 * 0.2756600186508242
        else:
            if  t_minus21 <= 3956.5:
                scores[0] += 0.2 * 0.33363943578263455
            else:
                scores[0] += 0.2 * -0.40307024044619927
    else:
        if  t_minus12 <= 3954.5:
            if  t_minus10 <= 3955.5:
                scores[0] += 0.2 * -1.4343056774817915
            else:
                scores[0] += 0.2 * -1.1552247184159352
        else:
            if  t_minus1 <= 3942.0:
                scores[0] += 0.2 * -1.2991567342910482
            else:
                scores[0] += 0.2 * -0.3802189110346514

    return scores.index(max(scores))


def predict(X):
    result = []
    for sample in X.values.tolist():
        result.append(prediction(*sample))
    return result
