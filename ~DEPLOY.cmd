set myssh=ssh -i "%userprofile%\.ssh\fastbooktrip-master-key.pem" ec2-user@ec2-65-0-173-111.ap-south-1.compute.amazonaws.com 
set s3path=s3://cloud-workspace/WEB_LIPI_FBT/
echo VARIABLES HAVE BEEN SET!


::==COMMIT-NIGGA
git add -A
git commit -m "PIT=[%DATE%-%TIME%]"
git push

::==BUILD STUFF
call ./www.crayonpapers.in/!BUILD-WEBSITE.cmd
cd %~dp0
echo %~dp0

::==CLOUD SYNC
aws s3 sync . %s3path% --exclude "*.git\*" --exclude "*.git/*" --exclude "*\node_modules\*" 

%myssh% sudo mkdir -p /srv/lipi/
%myssh% aws s3 sync %s3path% /srv/lipi/ --exclude "*/node_modules/*"


%myssh% "bash -s " < RELOAD-NGINX.sh
timeout 10
