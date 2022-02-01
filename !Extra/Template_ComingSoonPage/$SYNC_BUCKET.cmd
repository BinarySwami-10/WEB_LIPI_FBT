aws s3 sync . s3://www.bellaberries.com/ --acl public-read


rem cd /usr/share/nginx/html/bellaberries.com/; aws s3 sync s3://www.bellaberries.com/ .  --acl public-read
timeout 5
