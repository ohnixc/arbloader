#!/bin/bash

restart=0

#check if /usr/local/bin exists

if [ ! -d "/usr/local/bin/" ]
then
	#if not create it
	sudo -S mkdir /usr/local/
	sudo -S mkdir /usr/local/bin/
	#add it to path
	export PATH=$PATH:/usr/local/bin
	#and set the restart flag
	restart=1
fi

sudo rm -rf arbloader

echo 'Downloading latest CLI settings.'


YT_DIR=~/Desktop/arbloader-cli
YT_ENV=arbenv


git clone https://github.com/ohnixc/arbloader.git
cd arbloader
CURR=$(pwd)

cd cli
CURR_CLI=$(pwd)


#give all executables executable permissions
chmod a+wx run.sh arbloader-cli arbloader-cli.py requirements.txt

if [ ! -d $YT_DIR ]
then 
echo 'First time here I see.. Welcome.'
mkdir ${YT_DIR}
echo 'mkdir '${YT_DIR} 
echo 'Creaty Desktop App'
cp ${CURR_CLI}/arbloader-cli.py ${YT_DIR}
cd ${YT_DIR}
fi
echo 'Checking Virtual Environment Settings'
echo 'Checking VENV settings'
if [ ! -d ${YT_DIR}/${YT_ENV} ]
then
echo 'Uh oh! notty notty venv'
python3 -m venv ${YT_ENV}
echo 'python3 -m venv ' ${YT_ENV}
echo 'Created Virtual Envirnonment'
chmod a+wx ${YT_DIR}/${YT_ENV}
echo 'chmod a+wx ' ${YT_DIR}'/'${YT_ENV}
echo 'Amended app and venv permissions'
cp ${CURR_CLI}/requirements.txt ${YT_DIR}
chmod a+wx ${YT_DIR} arbloader-cli.py requirements.txt ${YT_DIR}'/'${YT_ENV}

ls ${YT_DIR}
echo 'Loaded app plugins'
else
echo 'source '  ${YT_ENV}'/bin/activate'
echo 'Activated Virtual Environment'
pip install -r requirements.txt
chmod a+wx ${YT_DIR}
chmod a+wx ${YT_DIR}/${YT_ENV}
echo 'pip install -r requirements.txt'
echo 'Checked and updated plugins'
echo 'All checks successful.'
echo 'Exit Virtual Environment'
fi
echo 'Lezdooet!!'

python3 arbloader-cli.py
restart=1

if [ $restart == 0 ]
then
	echo 'Keep going man. Download away.'
	deactivate
else
	echo 'Don't listen to the others. You're a cool dood.'
	rm -rf ${CURR}

  fi

exit




