# Programming Exercise

## Problem Statement
We need to be able to capture revenue from our external partners. Our partners share with
us their merchant base and then will share the revenue each merchant makes.

A revenue model represents a SALE or RETURN. It is important that we are able to
distinguish between these two types of transactions.

Our external partners vary in how near real time they can share their revenue across their
merchant base. Some partners share revenue on a daily basis, where revenue represents a
day. Other partners share revenue with us on a monthly basis, where revenue represents a
month.


We would like you to create a Proof of Concept of an API which receives a model that describes a
revenue claim on a given period of time (i.e. day, month) from our external partners. It should
capture:
• A unique reference of the partner. Required
• A unique reference of the merchant the revenue relates to. Required
• Total amount of revenue. Required
• Count of transactions the revenue is associated with Required
• Currency. Required
• If the transaction is a SALE or RETURN. Required
• An optional description field

It is expected that unit tests are included as part of this challenge.
