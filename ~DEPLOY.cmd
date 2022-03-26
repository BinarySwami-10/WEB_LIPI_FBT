call ~CONSTANTS.cmd
echo %myssh%

::==COMMIT-NIGGA
git add -A
git commit -m "PIT=[%DATE%-%TIME%]"
git push

::==BUILD STUFF
call ./www.crayonpapers.in/!BUILD-WEBSITE.cmd
cd %~dp0
echo %~dp0

::==CLOUD SYNC
aws s3 sync . %s3path% --exclude "*.git\*" --exclude "*.git/*" --exclude "*\node_modules\*" --delete

%myssh% mkdir -p /srv/lipi/
%myssh% aws s3 sync %s3path% /srv/lipi/ --exclude "*/node_modules/*" --delete


%myssh% "bash -s " < RELOAD-NGINX.sh
timeout 10
