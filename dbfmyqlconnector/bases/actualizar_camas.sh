#!/bin/bash
USER="root"
PASSWORD="rod161082"
DATABASE="sanlucastest1"
TABLEFILE="camas.sql"
HOSTNAME="localhost"
TABLENAME="CAMAS"
DBFFILE="CAMAS.DBF"


#########################
echo "Eliminando Tabla anterior"
mysql -u$USER -p$PASSWORD $DATABASE -e "drop table $TABLENAME"

echo "Creando Tabla $TABLEFILE"
mysql -u$USER -p$PASSWORD $DATABASE < $TABLEFILE

echo "IMPORTANDO DATOS DESDE $DBFFILE A $TABLENAME"
dbf2mysql -h $HOSTNAME -d $DATABASE -U $USER -P $PASSWORD -t $TABLENAME $DBFFILE  -vvvvv

echo "Incorporando campo ID - Primary Key"
mysql -u$USER -p$PASSWORD $DATABASE -e "ALTER TABLE $TABLENAME ADD id INT PRIMARY KEY AUTO_INCREMENT;"
