<span style="font-size:11.142857551574707pt;">1. install gd</span>
<span style="font-family:AndaleMono;font-size:10.285714149475098pt;color:#111111ff;"># apt-get install php5-gd</span>

<span style="font-family:AndaleMono;font-size:8.571428298950195pt;color:#111111ff;">2. activate mod_rewrite</span>
<span style="font-family:LucidaGrande;font-size:11.142857551574707pt;color:#101010ff;">sudo a2enmod rewrite</span>


<span style="font-size:11.142857551574707pt;">First look in the</span>  <span style="font-size:11.142857551574707pt;">section and change the line:</span><span style="font-size:11.142857551574707pt;"><i>AllowOverride None</i></span>

<span style="font-size:11.142857551574707pt;">to</span>
<span style="font-size:11.142857551574707pt;"><i>AllowOverride All</i></span>
<span style="font-family:LucidaGrande;font-size:11.142857551574707pt;color:#101010ff;">Do the same for the  section.</span>
<span style="font-size:11.142857551574707pt;"><i>sudo /etc/init.d/apache2 restart</i></span>

<span style="font-size:11.142857551574707pt;"><i>2.1 change home settings</i></span>
<span style="font-size:11.142857551574707pt;"><i>/etc/apache2/sites-available/default</i></span>    

<span style="font-size:11.142857551574707pt;"><i>3. install postfix</i></span>
<span style="font-family:CourierNewPSMT;font-size:12pt;color:#222222ff;">sudo apt-get install dovecot-postfix</span>

<span style="font-family:CourierNewPSMT;font-size:12pt;color:#222222ff;">5. install php5-cli</span>
<span style="font-family:CourierNewPSMT;font-size:12pt;color:#222222ff;">apt-get install php5-cli</span>

<span style="font-family:CourierNewPSMT;font-size:12pt;color:#222222ff;">6. Install curl</span>

<span style="font-family:ArialMT;font-size:12pt;">sudo apt-get install curl libcurl3 libcurl3-dev php5-curl php5-mcrypt</span>