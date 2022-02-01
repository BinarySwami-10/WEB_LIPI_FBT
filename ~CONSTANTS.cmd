@echo off
set myssh=ssh -i %userprofile%\.ssh\universal-swamix-key.pem ec2-user@ec2-13-126-1-99.ap-south-1.compute.amazonaws.com
set s3path=s3://cloud-workspace/WEB_LIPI_FBT/
echo VARIABLES HAVE BEEN SET!
@echo on



:: TEST
:: %myssh%
