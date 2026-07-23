1. <span style="font-size:11.142857551574707pt;">Install the EB CLI</span> 
	1. <span style="font-size:11.142857551574707pt;">Here’s a detailed docs for installing EB CLI</span> <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html" rel="noopener" class="external-link" target="_blank" style="font-size:11.142857551574707pt;color:#e4afaff;"><u>https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html</u></a> 
1. <span style="font-size:11.142857551574707pt;">Within the project folder, create another folder “.elasticbeanstalk” (yes, with dot)</span> 
	1. <span style="font-size:11.142857551574707pt;">Grab the config.yml file (included in the zip) and place it there.</span> 
1. <span style="font-size:11.142857551574707pt;">Go to “~/.aws”</span>  
	1. <span style="font-size:11.142857551574707pt;">Create that subdirectory if you still don’t have it</span> 
	2. <span style="font-size:11.142857551574707pt;">Create a file called “credentials” (no file extension) if you don’t have it yet</span> 
		1. <span style="font-size:11.142857551574707pt;">check the “credentials” file in the zip. You can use that.</span>  
		2. <span style="font-size:11.142857551574707pt;">this is actually my aws credentials I created within the IAM profiles. If you can navigate through creating your own, better. if not, i think this will work.</span> 
1. <span style="font-size:11.142857551574707pt;">Before you try to deploy, make sure that you’ve made a commit first. That commit will be the reference point of each deploy.</span> 
2. <span style="font-size:11.142857551574707pt;">When you’re ready to deploy issue a command “./deploy.sh”. (if this fails, make sure you have that file executable — 755)</span> 
	1. <span style="font-size:11.142857551574707pt;">When asked, type “prod"</span> 
	2. <span style="font-size:11.142857551574707pt;">It will first create a local build</span> 
	3. <span style="font-size:11.142857551574707pt;">After the build, it will try to deploy to EB.  I’m not sure what you’ll see, but theoretically, you should be able to deploy. If not, get a screenshot and send it over to me so I can check.</span> 


[[eb cli.zip]]