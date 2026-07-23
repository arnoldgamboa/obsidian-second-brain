## DynamoDB Related Api Test
    **Cache Api Test**
      1) should save offset detail to cache after invoking getOffsetAccountById
      2) should invalidate cache of client and offset account after pay from offset account

user 526058721
offset 527175300
offset account access denied.
Seems to be an issue with offsetAllowed = false ;
https://bluestone.sandbox.mambu.com/api/creditarrangements/2010281/accounts

# Index.spec

1. should return daily limit exceeded error - BPS (ok)
2. should return updated loan account info if request is handled successfully (ok)
3. should return error when pay an amount more than redraw balance (ok)
4. should create transaction and update payment intent when process scheduled redraw payment intent

 **Account Overview Api Test**
      **1) "before each" hook for "should get account overview of regular user_2 successfully, without loan accounts in connective**

Error caused by the “offset account access denied.” Issue related to the other tests.
—

## **Locked Pay Now Api Test**
      **1) should return error when pay or transfer for home loan - isRedrawLocked = true**

Error caused by the “offset account access denied.” Issue related to the other tests.
—

      <span style="color:#ff23dff;"><b>2) should return error when pay or transfer for home loan account - isInterestOrFeesLocked = true</b></span>

<span style="color:#ff23dff;">MAMBU ISSUE, NO `lockedOperations` property in endpoint</span>


  Create Offset
**1) create offset account successfully**

https://bluestone.sandbox.mambu.com/#viewloanproduct.id=8a89861c762a688601762aae7d470066
There was a change done on 5-15-23 (Changed ID from 'BPS' to 'BPS_curr’). Since then, this account wouldn’t allow to create offset. Not exactly sure why.

  happy pass
    <span style="color:#ff260ff;"><b>1) view account overview page</b></span>

<span style="color:#ff260ff;">Nabin and I did some extensive analysis on this issue. Unfortunately, without context on why/how this test is done, we couldn’t find a reason why it’s failing. Will need Daniel’s comment/assistance</span>

    **2) view variable loan account in arrears from account overview**
There was a change done on 5-15-23 (Changed ID from ‘BPS' to 'BPS_curr’) that’s causing the error
(done)

    **3) view loan account detail navigating from account overview**
There was a change done on 5-15-23 (Changed ID from ‘BPS' to 'BPS_curr’) that’s causing the error
**(done)**

    **4) view offset account transaction history**
**(done)**

Related to Offset Account

    **5) view LOC account detail**

Passed

    **6) view locked redraw account detail**

Passed

    <span style="color:#ff260ff;"><b>7) view locked interest and fees home loan account detail</b></span>
<span style="color:#ff260ff;">(Potential issue)</span>
<span style="color:#ff260ff;">MAMBU ISSUE, NO `lockedOperations` property in endpoint</span>


    **8) view offset account detail**
**(done)**
Related to offset account issue

    **9) view deposit account detail page navigating from menu** 
**(done)**
Related to offset account issue


    **10) view statements page when click statements button in menu**

Passed - however, I noticed that the pdf file downloaded went to my machines “Downloads” directory. I’m not sure if this is a local machine settings behavior. But the test wouldn’t proceed until I copied the file on to “/internet-banking/ib-e2e/e2e-tests/cypress/downloads/“. It then proceeded and passed. Is this going to affect the pipeline processing? 


 payTo
    **1) "before each" hook for "view BPS PayTo page navigating from account overview"**

Related to offset account issue


## payToValidation
    **1) should check validations of the form fields**

Related to offset account issue

  pending DD
  LOC account will display correct redraw balance in account-overview and account-details page

<span style="color:#ff260ff;">(Potential issue)</span>
<span style="color:#ff260ff;">SERVER (MAMBU) IS TIMING OUT WHEN SENDING REPAYMENT TRANSACTIONS, TOO MANY TRANSACTIONS TO PROCESS. WILL NEED TO ASK MAMBU AND/OR DANIEL ON WHAT NEEDS TO BE DONE.</span>

  Scheduled payments
    **1) "before each" hook for "view scheduled payments page when click scheduled payments button in menu"**

related to offset account issue


—
https://github.com/Bluestone-APAC/internet-banking/actions/runs/5458668445/jobs/9933980240


Parameter store