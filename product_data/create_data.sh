# /bin/bash

for file in `\find . -maxdepth 2 -name '*.py'`; do
    name=`echo $file | rev | cut -d'/' -f1 | cut -c 4- | rev`;
    python $file > json/$name.json;
done
