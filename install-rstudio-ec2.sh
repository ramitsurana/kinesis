#!/bin/bash

echo "Installing R ..."
sudo yum install -y R

echo "Installing RStudio ..."
wget https://download2.rstudio.org/rstudio-server-rhel-1.0.153-x86_64.rpm
sudo yum install -y --nogpgcheck rstudio-server-rhel-1.0.153-x86_64.rpm

echo "Adding libcurl-devel package ..."
sudo yum install libcurl-devel.x86_64 -y

echo "Adding User - RStudio ..."
sudo useradd rstudio
