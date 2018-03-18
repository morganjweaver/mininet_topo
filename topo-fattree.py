"""Custom topology fattree

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

iAdding the 'topos' dict with a key/value pair to generate our newly defined
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
    "fattree topology"

    CoreSwitches = []
    AggregateSwitches = []
    AccessSwitches = []
    Hosts = []
    

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

	    self.bw_c2ag = 5.0
        self.bw_ag2ac = 0.5
        self.bw_ac2h = 0.05
	
        # Add core switches
	logger.debug("Add Core")
	for i in range(1,3):
	    self.CoreSwitches.append(self.addSwitch( 'c{}'.format(i) ))
	
	# Add aggregate and access switches
	logger.debug("Add Aggregate and Access")
	for i in range(1,11):
	    self.AggregateSwitches.append(self.addSwitch( 'ag{}'.format(i) ))
	    self.AccessSwitches.append(self.addSwitch( 'ac{}'.format(i) ))

	# Add hosts
	logger.debug("Add Host")
	for i in range(1,101):
	    self.Hosts.append(self.addHost( 'h{}'.format(i) ))
	
	logger.debug("Finished topology creation!")
	

        # Add links core <-> aggregate
	logger.debug("Add link: Core <--> Aggregate")
	linkopts = dict(bw=self.bw_c2ag)
	for k in range(0,5):
	    self.addLink( self.CoreSwitches[0], self.AggregateSwitches[k*2], **linkopts )
	    self.addLink( self.CoreSwitches[1], self.AggregateSwitches[k*2+1], **linkopts )
	
	# Add links aggregate <-> access
	logger.debug("Add link: Aggregate <--> Access")
	linkopts = dict(bw=self.bw_ag2ac)
	for k in range(0,10):
	    if(k % 2 == 0):
	        self.addLink( self.AggregateSwitches[k], self.AccessSwitches[k], **linkopts )
	        self.addLink( self.AggregateSwitches[k], self.AccessSwitches[k+1], **linkopts )
	    else:
		    self.addLink( self.AggregateSwitches[k], self.AccessSwitches[k], **linkopts )
	        self.addLink( self.AggregateSwitches[k], self.AccessSwitches[k-1], **linkopts )
	
	# Add links access <-> hosts
	#import pdb; pdb.set_trace()
	logger.debug("Add link: Access <--> Host")
	linkopts = dict(bw=self.bw_ac2h)	
	for k in range(0,100):
	    tensPlace = int(floor(k/10))
	    onesPlace = k%10
	    self.addLink( self.AccessSwitches[tensPlace], self.Hosts[onesPlace], **linkopts )

	logger.debug("Finished adding links!")


topos = { 'mytopo': ( lambda: MyTopo() ) }
setLogLevel('info')
fattree = MyTopo()
