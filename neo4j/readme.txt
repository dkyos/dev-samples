

https://neo4j.com/docs/operations-manual/current/installation/linux/debian/


wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.org/repo stable/' | sudo tee -a /etc/apt/sources.list.d/neo4j.list
sudo apt-get update


To install Neo4j Community Edition:
sudo apt-get install neo4j=1:3.4.0


sudo apt-get install oracle-java8-set-default


sudo service neo4j restart
sudo service neo4j stop
sudo service neo4j start


http://localhost:7474/browser/


sudo gedit /etc/neo4j/neo4j.conf


