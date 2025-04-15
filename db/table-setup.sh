#!/usr/bin/bash

DB_NAME="log-messages"
DB_USER="root"
DB_PASS="Wnml6OeywzKvE3Ac"
DB_HOST="127.0.0.1"
DB_PORT="3306"
DB_CHARSET="utf8mb4"

mysql -h $DB_HOST -P $DB_PORT -u $DB_USER -p$DB_PASS $DB_NAME < table.sql


