@echo off
set myssh=ssh -i %userprofile%\.ssh\fastbooktrip-master-key.pem ec2-user@ec2-65-0-4-25.ap-south-1.compute.amazonaws.com 
set s3path=s3://cloud-workspace/WEB_LIPI_FBT/
echo VARIABLES HAVE BEEN SET!
@echo on



:: TEST
:: %myssh%
