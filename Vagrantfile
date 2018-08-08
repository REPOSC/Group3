# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "fedora/27-cloud-base"
  config.vm.box_url = "https://mirrors.tuna.tsinghua.edu.cn/fedora/releases/27/CloudImages/x86_64/images/Fedora-Cloud-Base-Vagrant-27-1.6.x86_64.vagrant-virtualbox.box"
  config.vm.box_download_checksum = "7a37a20f87900c7a9360969658c58e5a3edcac2f5120897ce783cf21b2debbf9"
  config.vm.box_download_checksum_type = :sha256

  config.vm.network "private_network", ip: "192.168.55.33"
  config.vm.synced_folder ".", "/vagrant", create: true, nfs: true
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL

    type -fp python3.7 &>/dev/null || (
      dnf install -y python37
      python3.7 -mensurepip
    )

    type -fp mysql &>/dev/null || (
      dnf install -y mariadb-server mariadb-devel
      systemctl enable mariadb
      systemctl start mariadb
      mysqladmin -u root password vagrant
    )

    [[ -f /etc/pip.conf ]] || cat > /etc/pip.conf <<'EOF'
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
EOF

  SHELL

  config.vm.provision "shell", inline: <<-SCRIPT
    sudo sed -i '1a #!/usr/bin/python3.6' /usr/bin/dnf
    sudo sed -i '1d' /usr/bin/dnf
    sudo rm /usr/bin/python3
    sudo ln -s /usr/bin/python3.7 /usr/bin/python3
    sudo rm /usr/bin/python
    sudo ln -s /usr/bin/python3.7 /usr/bin/python
  SCRIPT

  config.vm.provision "shell", inline: <<-SCRIPT
    sudo dnf install -y git
    sudo dnf install -y gcc
  SCRIPT

  config.vm.provision "shell", privileged: false, inline: <<-SCRIPT
    pip3 install ipython bpython --user
    pip3 install --upgrade pip --user
  SCRIPT

end
