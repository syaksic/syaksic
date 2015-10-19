# Bitcoins

Tras leer la noticia de [21 Inc lanza portal educativo para desarrolladores de Bitcoin][criptonoticias], con [Francisco][Alberto.el.cerdo] hemos decidido resumir el [tutorial][tuto21btc] presentado por 21 Inc para que alumnos de la USM se motiven en utilizar este enredado sistema monetario.

## Resumen 21 Bitcoin

Este resumen se basa en el [tutorial][tuto21btc] y [faq][faq21btc] de 21 bitcoin.

### Tutorial 0

[Creating a basic Bitcoin development environment][tuto0]

En esta seccion nos indican los comandos para dejar instalado y corriendo el [demonio][demonio] de bitcoin.

#### Creando un entorno basico de Bitcoin en Ubuntu

Ingresando los siguientes comandos, tendremos instalado el Demonio Bitcoin.

'''
# Install dependencies
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y git-core
sudo apt-get install -y build-essential libtool autotools-dev autoconf pkg-config libssl-dev
sudo apt-get install -y libboost-all-dev

# Install the special Berkeley DB dependency (and optionally MiniUPNPC)
sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt-get update
sudo apt-get install -y libdb4.8-dev libdb4.8++-dev
sudo apt-get install -y libminiupnpc-dev

# Build bitcoind from source
export CORES=$( nproc ) # Linux or Mac
cd $HOME
git clone https://github.com/bitcoin/bitcoin.git
cd bitcoin
git checkout v0.11.0
./autogen.sh
./configure --enable-hardening
make -j $CORES

# Add bitcoind, bitcoin-cli, bitcoin-tx to your path
mkdir -p $HOME/bin
cd $HOME/bin
ln -s ../bitcoin/src/bitcoind .
ln -s ../bitcoin/src/bitcoin-cli .
ln -s ../bitcoin/src/bitcoin-tx .
export PATH=$PATH:$HOME/bin

# Set up bitcoin.conf
mkdir -p $HOME/.bitcoin
echo -e "rpcuser=bitcoinrpc\\nrpcpassword=MAKE_UP_A_PASSWORD\\n" > $HOME/.bitcoin/bitcoin.conf

# Launch bitcoind
bitcoind -daemon -txindex -reindex -server
'''




### Tutorial 1

[Introduction to Bitcoin][tuto1]

### Tutorial 2

[Bitcoin Mining][tuto2]

### Tutorial 3

[The Blockchain][tuto3]

[demonio]:https://es.wikipedia.org/wiki/Demonio_(inform%C3%A1tica)
[tuto3]:https://21.co/learn/the-blockchain/
[tuto2]:https://21.co/learn/bitcoin-mining/
[tuto1]:https://21.co/learn/introduction-to-bitcoin/#introduction-to-bitcoin
[tuto0]:https://21.co/learn/setup-a-bitcoin-development-environment/#creating-a-basic-bitcoin-development-environment
[faq21btc]:https://21.co/learn/faq/#what-is-the-21-bitcoin-chip  
[tuto21btc]:https://21.co/learn/introduction-to-bitcoin/#introduction-to-bitcoin
[Alberto.el.cerdo]:https://www.facebook.com/Alberto.el.cerdo/
[criptonoticias]:http://criptonoticias.com/21-inc-lanza-portal-educativo-para-desarrolladores-de-bitcoin/

