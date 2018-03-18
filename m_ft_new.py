"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
        
        self.bw_core = 5.0
        self.bw_agg = 0.5
        self.bw_edge = 0.05

        EdgeSwitches = []
        Hosts = []
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
        for i in range (1,11):
        self.EdgeSwitches.append(self.addSwitch( 'e{}'.format(i) )
        
        logger.debug("Add Host")
        for i in range(1,101):
            self.Hosts.append(self.addHost( 'h{}'.format(i) ))
        # Add links
        #Connect cores to each other, then all 4 aggregators to each:
        #ALL 10 GB CONNECTIONS:
        linkopts = dict(bw=self.bw_c2ag)
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
        linkopts = dict(bw=self.bw_c2ag)
        self.addLink(Agg1, Agg2, **linkopts)
        self.addLink(Agg2, Agg3, **linkopts)
        self.addLink(Agg3, Agg4, **linkopts)
        #Connect each aggregator to an edge, all 1 GB connections:
        for j in range(1,6):
            self.addLink(Agg1, EdgeSwitches[j], **linkopts)
            self.addLink(Agg2, EdgeSwitches[j], **linkopts)
        for k in range(6,11):
            self.addLink(Agg3, EdgeSwitches[k], **linkopts)
            self.addLink(Agg4, EdgeSwitches[k], **linkopts)
        #connect each edge switch to one peer
        for m in range(1,10):
            self.addLink(EdgeSwitches[m], EdgeSwitches[m+1], **linkopts)
        #Connect each edge switch to 10 hosts
        linkopts = dict(bw=self.bw_edge)
        counter = 1
        for l in range(1,11):
            for m in range(1,11)
                self.addLink(EdgeSwitches[l], Hosts[counter], **linkopts)
                counter = counter + 1
        


topos = { 'mytopo': ( lambda: MyTopo() ) }
setLogLevel('info')
fattree = MyTopo()









