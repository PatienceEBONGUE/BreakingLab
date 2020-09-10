#!/bin/bash
## dependance : docker netstat grep at date

##Ce script permet de faire la lisaison entre le site écrit avec django et le gestionnaire de containeurs
# Version 1.3

PATH=/usr/local/bin:/usr/bin:/bin:/usr/games

TIMEOUT=120 ## La durée par default est de 2H
MAXTIME=300 ## la durée maximum authorisé est 5H

case $1 in
start)
	## test le nombre d'argumetns
	if [[ $# -ne 3 && $# -ne 4 ]]
	then
		printf "{\"status\":\"1\", \"error\":\"too few arguments\"}\n"
		exit 1
	fi

	## definit le timer
	if [ $# -eq 4 ]
	then
		if [[ $4 -gt 0 && $4 -lt  $MAXTIME ]]
		then
			TIME=$4 ##si plus petit, on met l'arguent
		else
			TIME=$MAXTIME ##si plus grand que la limite, on met la limite 
		fi
	elif [ $# -eq 3 ]
	then
		TIME=$TIMEOUT ##timeout par default si non précisé
	fi


	USER=$3
	## verifie si l'user a deja un tp en cous
	if docker ps -a | grep " $USER$" > /dev/null
	then
		IDrunning=$(docker ps -a | tr -s ' ' | grep " $3$"| cut -d ' ' -f 1)
		docker rm -f $IDrunning > /dev/null
	fi

	## verifie si un TP donnee existe 
	if docker images | tr -s ' ' | grep "$2 " > /dev/null
	then
		TP=$2
	else
		printf "{\"status\":\"1\", \"error\":\"Image not found\"}\n"
		exit 1
	fi

	## initialise le port alaetoire du container
	PORT=$(($RANDOM+5000))
	## verifie que le port aleatoire n'est pas deja utilisÃ, sinon en regenere un
	while netstat -plount 2> /dev/null | grep ":$PORT " > /dev/null
	do
		PORT=$(($RANDOM+5000))
	done

	## lance le docker, et sort un json en retour, 0 tout est ok, 1 il y a eu un probleme
	if docker run --name $USER -p $PORT:80 $TP /start.sh > /dev/null 2> /dev/null &
	then
		printf "{\"status\":\"0\", \"error\":\"Container started\", \"port\":\"$PORT\"}\n"
		END=$(date -d "now +$TIME min" +%H:%M)
		echo "docker rm -f $USER" | at $END 2> /dev/null
		exit 0
	else
		printf "{\"status\":\"1\", \"error\":\"Container not started\"}\n"
		exit 1
	fi
	;;


stop)
	## check si argument est un port
	if [ $2 -gt 1 -a $2 -lt 65535 2> /dev/null ]
	then
		ID=$(docker ps | grep "0.0.0.0:$2-" | cut -d ' ' -f 1)
		if [ "$ID" ==  "" ]; then
			printf "{\"status\":\"1\", \"error\":\"Container not found\"}\n"
			exit 1
		fi
	else
		ID=$(docker ps | tr -s ' ' | grep " $2$"| cut -d ' ' -f 1)
		if [ "$ID" ==  "" ]; then
			printf "{\"status\":\"1\", \"error\":\"Container not found\"}\n"
			exit 1
		fi
		
	fi
	
	if docker ps | grep "$ID" > /dev/null 2> /dev/null	## verifie que l'ID donne existe bien (pas super utile mais pas genant) 
	then
		echo "\"$ID\""
		if docker rm -f $ID > /dev/null
		then
			printf "{\"status\":\"0\", \"error\":\"Done\"}\n"
			exit 0
		else
			printf "{\"status\":\"1\", \"error\":\"Container not closed\"}\n"
			exit 1
		fi
	fi
	;;
help)
	printf "usage : proj-script.sh start image username (timeout)\n time out is not requiered. It is 2H by default, and can be set betwenn 1min and 5H\nusage : proj-script.sh stop container-port OR username\n"
	;;

*)
	echo "error-unexpected, try help"
	printf "{\"status\":\"2\", \"error\":\"unexpected error\"}\n"
	exit 2
	;;
esac
