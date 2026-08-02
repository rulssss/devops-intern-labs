#!/bin/bash

respaldo="./archivos_backup"

destino="./backups"


if [ -d $destino ];
then

        fecha=$(date +%Y-%m-%d)
        tar -czvf "$destino/backup_$fecha.tar.gz" "$respaldo"
        echo "respaldo realizado"
        ls "$destino"

else

        mkdir ./$destino
        echo "directorio no encontrado pero creado, porfavor corra el\n sh de nuevo."
        ls
fi