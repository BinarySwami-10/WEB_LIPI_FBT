@echo off
set myssh=ssh -i "%userprofile%\.ssh\fastbooktrip-master-key.pem" ec2-user@ec2-65-0-173-111.ap-south-1.compute.amazonaws.com 
%myssh% cd /home/ec2-user/github/WEB_LIPI_FBT ; git pull -f ; echo success 
pause