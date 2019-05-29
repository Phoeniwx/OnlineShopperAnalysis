# OnlineShopperAnalysis
The dataset consists of 10 numerical and 8 categorical attributes. 
The 'Revenue' attribute can be used as the class label. 

"Administrative", "Administrative Duration", "Informational", "Informational Duration", "Product Related" and "Product Related Duration" represent the number of different types of pages visited by the visitor in that session and total time spent in each of these page categories.   

The "Bounce Rate", "Exit Rate" and "Page Value" features represent the metrics measured by "Google Analytics" for each page in the e-commerce site. The value of "Bounce Rate" feature for a web page refers to the percentage of visitors who enter the site from that page and then leave ("bounce") without triggering any other requests to the analytics server during that session. The value of "Exit Rate" feature for a specific web page is calculated as for all pageviews to the page, the percentage that were the last in the session. The "Page Value" feature represents the average value for a web page that a user visited before completing an e-commerce transaction.   

The "Special Day" feature indicates the closeness of the site visiting time to a specific special day (e.g. Mother’s Day, Valentine's Day) in which the sessions are more likely to be finalized with transaction. The value of this attribute is determined by considering the dynamics of e-commerce such as the duration between the order date and delivery date. For example, for Valentina’s day, this value takes a nonzero value between February 2 and February 12, zero before and after this date unless it is close to another special day, and its maximum value of 1 on February 8.  

The dataset also includes operating system, browser, region, traffic type, visitor type as returning or new visitor, a Boolean value indicating whether the date of the visit is weekend, and month of the year.

## Test Result
+ linear SVM
```
Train time: 1926.8377079963684
accuracy: 0.870235198702352, 
precision: 0.8096111111111111, 
recall: 0.6744453770601274
[[1987   57]
 [ 263  159]]
```
+ Bayes
```
Train time: 0.01177668571472168
accuracy: 0.8410381184103812, 
precision: 0.7193829985592, 
recall: 0.7160664434572115
[[1852  192]
 [ 200  222]]

```
+ Logic Regression
```
Train time: 0.41097402572631836
accuracy: 0.8333333333333334, 
precision: 0.8498980008159935, 
recall: 0.5149136068112891
[[2042    2]
 [ 409   13]]
```
+ KNN
```
Train time: 0.04596209526062012
accuracy: 0.851581508515815, 
precision: 0.7605920786743905, 
recall: 0.6255843017593975
[[1981   63]
 [ 303  119]]
```
+ Decision Tree
```
Train time: 0.06131792068481445
accuracy: 0.8596918085969181, 
precision: 0.7532520365537838, 
recall: 0.7367210469203587
[[1888  156]
 [ 190  232]]
```
+ Random Forest
```
Train time: 0.1614680290222168
accuracy: 0.884022708840227, 
precision: 0.8192174822515212, 
recall: 0.7335340518080893
[[1967   77]
 [ 209  213]]
```