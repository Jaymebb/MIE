# MIE
Medical Entity and Relation Extraction Service

##Installation

###Install Quick-UMLS

Download MetamorphoSys, the UMLS installation program at here (umls-2016AB-full.zip) with your UMLS Terminology Services Username and Password.

Unzip umls-2016AB-full.zip and mmsys.zip (inside 2016AB).

Install MetamorphoSys with ./run_linux.sh, after installed, find path of META folder.

Make sure python-dev is installed.

cd MIE, into this project folder

pip install -r requirements.txt

python -m spacy.en.download

cd MIE/mie/utils, download and compile simstring using bash setup_simstring.sh 2 where 2 indicates the current Python version is 2.X.

cd MIE/mie/initialize/, installize the system by running python install.py <ummls_installation_path> <destination_path> where umls_installation_path is the path of META folder, specify the destination_path yourself.

###Install MetaMap

Download MetaMap16 here

Unzip and fetch MetaMap.

Follow this link to install MetaMap.

Install cTakes

A formal installation guide can be found here.

Java 1.7 or higher is needed, test with java -version
Download cTakes here.
Unzip cTakes with sudo tar -xvf apache-ctakes-3.2.2-bin.tar.gz -C /usr/local.
Download cTakes resource file here (ctakes-resources-3.2.1.1-bin.zip, unzip and copy the content of resources with: cp -R <path-to-resource>/resources/* /usr/local/apache-ctakes-3.2.2/resources
cd /usr/local/apache-ctakes-<version_number>/desc/ctakes-clinical-pipeline/desc/collection_processing_engine
sudo cp test_plaintext.xml test_plaintext_test.xml
sudo vim test_plaintext_test.xml
Replace the value of node NameValuePair (where name is InputDirectory) to note_input.
Replace the value of node NameValuePair (where name is OutputDirectory) to result_out. Save and quit test_plaintext_test.xml
cd /usr/local/apache-ctakes-<version_number>/bin
sudo cp runctakesCPE.sh runctakesCPE_CLI.sh
sudo vim runctakesCPE_CLI.sh, add #!/bin/sh to first line,replace the last line (java…) to java -Dctakes.umlsuser=USER -Dctakes.umlspw=PW -cp $CTAKES_HOME/lib/*:$CTAKES_HOME/desc/:$CTAKES_HOME/resources/ -Dlog4j.configuration=file:$CTAKES_HOME/config/log4j.xml -Xms2g -Xmx3g org.apache.uima.examples.cpe.SimpleRunCPE $CTAKES_HOME/desc/ctakes-clinical-pipeline/desc/collection_processing_engine/test_plaintext_test.xml. Where you need to change USER parameter with your UMLS terminology username, PW to your UMLS password, save and quit.
In root folder of cTakes, create two folder with sudo mkdir note_input and sudo mkdir result_output.
##Configuration

Configure environment variable at .env file (within project root folder). Here I use MongoDB to store the abstract of medical papers, the variables include

MONGO_DB=YOUR-MONGO-DB-DATABASE-NAME
MONGO_PORT=YOUR-MONGO-DB-PORT
MONGO_URL=YOUR-MONGO-DB-SERVICE-URL
MONGO_COL=YOUR-MONGO-DB-COLLECTION
DEST_PATH=YOUR-SPECIFIED-DESTINATION-PATH
INSTANCE_PATH=YOUR-METAMAP-INSTALLATION-PATH
##Running

python app.py
http://127.0.0.1:5000/medir/api/v0.1/quickumls/doc_id
http://127.0.0.1:5000/medir/api/v0.1/metamap/doc_id
http://127.0.0.1:5000/medir.api/v0.1/ctakes/doc_id
##Testing

nosetests
