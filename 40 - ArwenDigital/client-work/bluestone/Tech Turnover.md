Tech stacks

1. Typescript
2. AWS Lambda
3. NodeJS
4. ReactJS
5. Mambu
6. Jest
7. Github Actions
8. Docker

——

1. Origination
2. Payments
3. Internet Banking
4. Commission
5. Offset

Mambu Rate Change Functionality


—
Origination

		Check [appcentre-failed-validation-](https://s3.console.aws.amazon.com/s3/buckets/appcentre-failed-validation-staging?region=ap-southeast-2)prod bucket by date
		- Download XML and find identifier
		- Check identifier in application-id-mappings table
		- Check Mambu to see if it is already settled
		- If not already settled, check slack alert or logs to see where error is
		- Consult originations BA to get missing / incorrect data
		- Resubmit via API Gateway
		- Check Mambu for settlement

<p style="text-align:right;margin:0"><a href="https://bluestonemortgages.slack.com/archives/C054Y2TCDQT/p1682481214267169" rel="noopener" class="external-link" target="_blank">11:53</a>
</p>
The originations team is:
BA : Jen Carag
PM: Hayley T.
QA: Ria Hererra

So you want to message 
[@Jen Carag](https://bluestonemortgages.slack.com/team/U0270M1RGR0)
 if you need help fixing the data

—
Discharge
https://docs.google.com/document/d/1snW3lr9wiSpYkwzaPxKxFGzsC8gYzPKp-a9IlMnJ-WM/edit#heading=h.8tbl2ldl290x

—

With Alex
1. Structure of the team
2. Belarus team, what’s the focus?
3. How process runs top level
4. What’s the deployment process like? Staging? Prod?
5. AWS Lambda Sandbox


—
Commissions
Loan servicing (rate changes, discharging) - Belarus 
- Custom fields
- Zab Maria Pacleb 
- Daniel and Nabeem
	- Oksana, Walter
	- Joanna QA
	- Ric 
Internet banking 
Payments
Origination 


——
Mac On-boarding
https://bluestoneapac.atlassian.net/wiki/spaces/CPR/pages/1092845577/Mac+onboarding