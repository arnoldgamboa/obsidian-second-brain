<span style="font-family:ArialMT;font-size:11.142857551574707pt;color:#263238ff;">ALTER TABLE `articles`</span>
<span style="font-family:ArialMT;font-size:11.142857551574707pt;color:#263238ff;">ADD `featured` varchar(1) COLLATE 'utf8_general_ci' NULL AFTER `set_to_front`;</span>

<span style="font-family:ArialMT;font-size:11.142857551574707pt;color:#263238ff;">change /appliation/config/sites.php</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">managersofwealth = 1</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">ambankers = 2</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">apbankers = 3</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">eubankers = 4</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">mebankers = 5</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">africabankers = 6</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">offshorebankers = 7</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">globalbankers = 8</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">islamicbankes = 9</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">fintechnews = 10</span>
<span style="font-size:11.142857551574707pt;color:#2d3033ff;">pensionmanagers = 11</span>

<a href="https://serverpilot.io/community/articles/how-to-disable-strict-mode-in-mysql-5-7.html" rel="noopener" class="external-link" target="_blank" style="font-size:11.142857551574707pt;color:#2d3033ff;"><u>https://serverpilot.io/community/articles/how-to-disable-strict-mode-in-mysql-5-7.html</u></a>
<span style="font-size:11.142857551574707pt;">sudo nano /etc/mysql/conf.d/disable_strict_mode.cnf</span>

<span style="font-size:11.142857551574707pt;">[mysqld]</span>
<span style="font-size:11.142857551574707pt;">sql_mode=IGNORE_SPACE,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION</span>

<span style="font-size:11.142857551574707pt;">sudo service mysql restart</span>

<span style="font-size:11.142857551574707pt;">sudo mysql -i -BN -e 'SELECT @@sql_mode' | grep -E 'ONLY_FULL_GROUP_BY|STRICT_TRANS_TABLES'</span>