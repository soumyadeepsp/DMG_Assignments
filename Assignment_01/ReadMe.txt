METHODOLY ------------------------------------------
1,2) We fetched the json data from the file or from the online link using http call in python. then we just iterated over the json object and extracted the data required and stored them in arrays in required format for us to do the required computations. In question 2 after getting the outputs we converted them from simple arrays to pandas dataframe objects so that we can plot the area trend graphs.
3) We assumed a hypothesis which is a linear function - y_pred = m*x+c. Then we plotted the graph of mean square error considering y_pred with our hypothesis equation and y_actual. This graph of mean squared error came to be a parabola w.r.t theta(column matrix of [m,c]) which is a convex function. Thus we then used the gradient descent algorithm to find the global minima of the function which will give us the value of m and c which produces theleast mean squared error. The gradient descent algorithm ran with a learning rate of 0.00000001 and 10000 iterations.

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
Intercept = -8.901833941157925
Slope     = 13.96502518623434
Recovered : 
Intercept = -1.0765434133366463
Slope     = 12.00205210306684
Deceased : 
Intercept = 0.05690559171730575
Slope     = 0.24168987285330937
