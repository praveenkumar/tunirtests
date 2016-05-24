#/usr/bin/sh

rm -rf tunirtests
mkdir -p tunirtests
cp -f *.py tunirtests/
cp LICENSE tunirtests
tar -czvf /tmp/tunirtests.tar.gz tunirtests
rsync -avz --progress /tmp/tunirtests.tar.gz kumarpraveen@fedorapeople.org:~/public_html/
