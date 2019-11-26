all: test

install: etc/* lib/* bin/* score doc
	test -d /opt/linuxer || mkdir /opt/linuxer 2>/dev/null
	test -d /opt/linuxer/score || mkdir /opt/linuxer/score 2>/dev/null
	cp -rf etc/ lib/ bin/ doc/ /opt/linuxer 2>/dev/null

help:
	echo "TODO"

uninstall: /opt/linuxer
	rm -rf /opt/linuxer

test: /opt/linuxer
	/opt/linuxer/bin/linuxer.bash
