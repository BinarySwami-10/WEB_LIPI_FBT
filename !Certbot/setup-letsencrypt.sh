mkdir /certbotdir
cd /certbotdir
sudo wget -r --no-parent -A 'epel-release-*.rpm' https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/
sudo rpm -Uvh dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-*.rpm
sudo yum-config-manager --enable epel*
sudo yum repolist all
sudo yum install -y certbot python-certbot-nginx
sudo yum install -y ./epel.rpm

#MAIN
sudo certbot -i nginx -a manual --preferred-challenges dns -d *.crayonpapers.in -d crayonpapers.in

#UPLOAD NEW CERT
sudo aws s3 sync "/etc/letsencrypt/" "s3://cloud-workspace/WEB_LIPI_FBT/\!Certbot/certificates/"
sudo aws s3 cp "/etc/nginx/nginx.conf" "s3://cloud-workspace/WEB_LIPI_FBT/nginx.conf"