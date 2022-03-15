call ~CONSTANTS.cmd
echo %myssh%

::==COMMIT-NIGGA
call ~COMMIT.cmd

::==BUILD STUFF
call ./www.crayonpapers.in/!BUILD-WEBSITE.cmd
cd %~dp0
echo %~dp0

::==CLOUD SYNC
aws s3 sync . %s3path% --exclude "*.git\*" --exclude "*.git/*" --exclude "*\node_modules\*" --delete
%myssh% aws s3 sync %s3path% /srv/lipi/ --exclude "*/node_modules/*" --delete


%myssh% "bash -s " < RELOAD-NGINX.sh
timeout 10
