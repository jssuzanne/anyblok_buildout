./bin/buildout -c buildout.cfg
./bin/nosetests anyblok/anyblok/tests anyblok/anyblok/bloks/anyblok_core/tests -s -v --with-coverage --cover-package anyblok
./bin/buildout -c anyblok_web_server.cfg
./bin/nosetests anyblok_web_server/anyblok_web_server/bloks/web/tests -s -v
