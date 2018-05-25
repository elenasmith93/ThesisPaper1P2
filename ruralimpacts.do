**Elena Smith

import delimited "/Users/work-pc/Desktop/Thesis/Paper 1/rurality.csv", delimiter(comma) encoding(utf8) 
xtset id2 year, yearly //For FE/RE Later
replace rurality = rurality*-1

xtreg learn rurality l.learn hachman entropy pgrowth growth unemployment patents, fe
est store fe


quietly xtreg learn rurality l.learn hachman entropy growth unemployment
est store re

hausman fe re, sigmamore

gen pgrowth = 1 if growth >0
replace pgrowth = 0 if pgrowth == .

gen learn = log(mearn)

logit pgrowth rurality l.learn hachman entropy unemployment patents
margins, dydx(*)
