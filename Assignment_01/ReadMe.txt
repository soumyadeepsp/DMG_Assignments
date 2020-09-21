METHODOLOGY ------------------------------------------
1,2) We fetched the json data from the file or from the online link using http call in python. then we just iterated over the json object and extracted the data required and stored them in arrays in required format for us to do the required computations. In question 2 after getting the outputs we converted them from simple arrays to pandas dataframe objects so that we can plot the area trend graphs.
3) For this question, we found the intercept and slopes without using any libraries except numpy. We used Normal equation for in order to find the coefficients of the line. The values of theta can be calculated by using following equation where x is matrix of x and y is matrix of y.
		coeff = ((X.Transpose * X)^-1) * ((X.Transpose) * Y)

ASSUMPTIONS TAKEN ----------------------------------
1) For question 1 and part 6, we assumed that word "spike" means count of cases on a particular day.
2) We have also included the Unidentified states('un') in our results.
3) We have excluded 'tt' values from the data.


RESULTS OF QUESTION 1 AND QUESTION 3 ---------------

ANSWER TO Q1_1
Confirmed_count:  4110214
Recovered_count:  3177666
Deceased_count:  70095

ANSWER TO Q1_2
confirmed_count:  188193 
Recovered_count:  163785 
Deceased_count:  4538

ANSWER TO Q1_3
Confirmed_count:  1072055 
Recovered_count:  800359 
Deceased_count:  30813

ANSWER TO Q1_4
Confirmed - 
Highest affected State is:  mh
Highest affected State count is:  883862
Recovered - 
Highest affected State is:  mh
Highest affected State count is:  636574
Deceased - 
Highest affected State is:  mh
Highest affected State count is:  26275

ANSWER TO Q1_5
Confirmed - 
Lowest affected State is:  dd
Lowest affected State count is:  0
Recovered - 
Lowest affected State is:  dd
Lowest affected State count is:  0
Deceased -
Lowest affected State is:  dd
Lowest affected State count is:  0

ANSWER TO Q1_6
Confirmed - 
Day:  23-Jun-20
Count:  3947
Recovered - 
Day:  20-Jun-20
Count:  7725
Deceased - 
Day:  16-Jun-20
Count:  437

ANSWER TO Q1_7
Number of Active cases in  an  are :  343
Number of Active cases in  ap  are :  100880
Number of Active cases in  ar  are :  1525
Number of Active cases in  as  are :  28404
Number of Active cases in  br  are :  16735
Number of Active cases in  ch  are :  2143
Number of Active cases in  ct  are :  22320
Number of Active cases in  dd  are :  0
Number of Active cases in  dn  are :  301
Number of Active cases in  dl  are :  19870
Number of Active cases in  ga  are :  4945
Number of Active cases in  gj  are :  16266
Number of Active cases in  hp  are :  2023
Number of Active cases in  hr  are :  14912
Number of Active cases in  jh  are :  14980
Number of Active cases in  jk  are :  9547
Number of Active cases in  ka  are :  100224
Number of Active cases in  kl  are :  21867
Number of Active cases in  la  are :  834
Number of Active cases in  ld  are :  0
Number of Active cases in  mh  are :  221013
Number of Active cases in  ml  are :  1374
Number of Active cases in  mn  are :  1872
Number of Active cases in  mp  are :  15687
Number of Active cases in  mz  are :  349
Number of Active cases in  nl  are :  701
Number of Active cases in  or  are :  25856
Number of Active cases in  pb  are :  15870
Number of Active cases in  py  are :  5163
Number of Active cases in  rj  are :  14996
Number of Active cases in  sk  are :  561
Number of Active cases in  tg  are :  32405
Number of Active cases in  tn  are :  51580
Number of Active cases in  tr  are :  5905
Number of Active cases in  tt  are :  0
Number of Active cases in  un  are :  0
Number of Active cases in  up  are :  59963
Number of Active cases in  ut  are :  7649
Number of Active cases in  wb  are :  23390

ANSWER TO Q3
Confirmed : 
Intercept = -191.68619109947608
Slope     = 15.40430214935243
Recovered : 
Intercept = -243.82149869109912
Slope     = 13.913469619729947
Deceased : 
Intercept = 11.458278795811529
Slope     = 0.15191340589694113
