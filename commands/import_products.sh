#!/usr/bin/env bash

for sql in /suez/fixtures/products/*.sql
do
mysql -u canallocal --password=hogehoge canal < $sql
done
