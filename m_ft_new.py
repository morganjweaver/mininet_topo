"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from math import floor
import logging

logging.basicConfig(filename='./fattree.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

class MyTopo( Topo ):
    #"Simple topology example."

    Hosts = []
    EdgeSwitches = []

    def __init__( self ):
     #   "Create custom topo."

        Topo.__init__( self )
        self.bw_core = 5.0
        self.bw_agg = 0.5
        self.bw_edge = 0.05

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )

        Core1 = self.addSwitch( 'c1' )
        Core2 = self.addSwitch( 'c2' )

        Agg1 = self.addSwitch( 'a1' )
        Agg2 = self.addSwitch( 'a2' )
        Agg3 = self.addSwitch( 'a3' )
        Agg4 = self.addSwitch( 'a4' )
 
        logger.debug("Add Edges")
        for h in range (0,10):
            self.EdgeSwitches.append(self.addSwitch( 'e{}'.format(h) ))
 
        logger.debug("Add Host BANANAS")
        print("Adding hosts")
        for i in range(0,100):
            self.Hosts.append(self.addHost( 'h{}'.format(i) ))
        # Add links
        print("added hosts")
        #Connect cores to each other, then all 4 aggregators to each:
        #ALL 10 GB CONNECTIONS:
        linkopts = dict(bw=self.bw_core)
        self.addLink( Core1, Core2, **linkopts )
        self.addLink(Core1, Agg1, **linkopts)
        self.addLink(Core2, Agg1, **linkopts)
        self.addLink(Core1, Agg2, **linkopts)
        self.addLink(Core2, Agg2, **linkopts)
        self.addLink(Core1, Agg3, **linkopts)
        self.addLink(Core2, Agg3, **linkopts)
        self.addLink(Core1, Agg4, **linkopts) 
        self.addLink(Core2, Agg4, **linkopts) 
        #connect each aggregator to one peer, 1 GB connections: 
        linkopts = dict(bw=self.bw_agg) 
        self.addLink(Agg1, Agg2, **linkopts) 
        self.addLink(Agg2, Agg3, **linkopts) 
        self.addLink(Agg3, Agg4, **linkopts) 
        #Connect each aggregator to an edge, all 1 GB connections: 
        logger.debug("adding ag to edge links")
        for j in range(0,5):
            self.addLink(Agg1, self.EdgeSwitches[j], **linkopts)
            self.addLink(Agg2, self.EdgeSwitches[j], **linkopts)
        print("added forst 5hosts")
        for k in range(5,10):
            self.addLink(Agg3, self.EdgeSwitches[k], **linkopts)
            self.addLink(Agg4, self.EdgeSwitches[k], **linkopts)
        print("Added second 5 hosts")   
        #connect each edge switch to one peer
        print("adding 10 edge switch links")
        for m in range(0,9):
            self.addLink(self.EdgeSwitches[m], self.EdgeSwitches[m+1], **linkopts)
        #Connect each edge switch to 10 hosts
        logger.debug("adding edge to host links")
        linkopts = dict(bw=self.bw_edge)
        counter = 0
        for l in range(0,10):
            for m in range(0,10):
                self.addLink(self.EdgeSwitches[l], self.Hosts[counter], **linkopts)
                counter = counter + 1
      


topos = { 'mytopo': ( lambda: MyTopo() ) }
setLogLevel('info')
fattree = MyTopo()









