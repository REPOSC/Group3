cd ~
sudo python -m venv venv
cd venv
source bin/activate
pip install --upgrade pip
pip install Django mysqlclient
sudo yum -y install nodejs
sudo npm set registry https://registry.npm.taobao.org/
sudo npm install -g eslint
sudo npm install -y -g vue-cli@2.9
cd /vagrant/eng_project/frontend
npm install --no-bin-links