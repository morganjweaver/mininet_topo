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

	self.bw_c2ag = 100
        self.bw_ag2ac = 10
        self.bw_ac2h = 1


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
	    #self.Hosts.append(self.addHost( 'h{}'.format(i), ip="10.0.{}.100/24".format(i), defaultRoute = "via 10.0.1.1" ))
	    self.Hosts.append(self.addHost( 'h{}'.format(i)))

	logger.debug("Finished topology creation!")


        # Add links core <-> aggregate
	logger.debug("Add link: Core <--> Aggregate")
	#linkopts = dict(bw=self.bw_c2ag)
	linkopts1 = {'bw':50, 'delay':'5ms'}
	#for k in range(0,5):
    	self.addLink( self.CoreSwitches[0], self.CoreSwitches[1], **linkopts1 )
    	self.addLink( self.CoreSwitches[0], self.AggregateSwitches[0], **linkopts1 )
    	self.addLink( self.CoreSwitches[1], self.AggregateSwitches[1], **linkopts1 )
	self.addLink( self.CoreSwitches[0], self.AggregateSwitches[2], **linkopts1 )
    	self.addLink( self.CoreSwitches[1], self.AggregateSwitches[3], **linkopts1 )
	self.addLink( self.CoreSwitches[0], self.AggregateSwitches[4], **linkopts1 )
    	self.addLink( self.CoreSwitches[1], self.AggregateSwitches[5], **linkopts1 )
	self.addLink( self.CoreSwitches[0], self.AggregateSwitches[6], **linkopts1 )
    	self.addLink( self.CoreSwitches[1], self.AggregateSwitches[7], **linkopts1 )
	self.addLink( self.CoreSwitches[0], self.AggregateSwitches[8], **linkopts1 )
    	self.addLink( self.CoreSwitches[1], self.AggregateSwitches[9], **linkopts1 )

	    #self.addLink( self.CoreSwitches[1], self.AggregateSwitches[k*2+1], **linkopts )

	# Add links aggregate <-> access
	logger.debug("Add link: Aggregate <--> Access")
	#linkopts = dict(bw=self.bw_ag2ac)
	linkopts2 = {'bw':30, 'delay':'10ms'}
	#for k in range(0,10):
	    #if(k % 2 == 0):
    	self.addLink( self.AggregateSwitches[0], self.AccessSwitches[0], **linkopts2 )
    	#self.addLink( self.AggregateSwitches[0], self.AccessSwitches[1], **linkopts2 )
    	self.addLink( self.AggregateSwitches[1], self.AccessSwitches[1], **linkopts2 )
    	self.addLink( self.AggregateSwitches[2], self.AccessSwitches[2], **linkopts2 )
    	self.addLink( self.AggregateSwitches[3], self.AccessSwitches[3], **linkopts2 )
    	self.addLink( self.AggregateSwitches[4], self.AccessSwitches[4], **linkopts2 )
    	self.addLink( self.AggregateSwitches[5], self.AccessSwitches[5], **linkopts2 )
    	self.addLink( self.AggregateSwitches[6], self.AccessSwitches[6], **linkopts2 )
    	self.addLink( self.AggregateSwitches[7], self.AccessSwitches[7], **linkopts2 )
    	self.addLink( self.AggregateSwitches[8], self.AccessSwitches[8], **linkopts2 )
    	self.addLink( self.AggregateSwitches[9], self.AccessSwitches[9], **linkopts2 )
	    #else:
    	#self.addLink( self.AggregateSwitches[1], self.AccessSwitches[0], **linkopts2 )
    	#self.addLink( self.AggregateSwitches[1], self.AccessSwitches[1], **linkopts2 )

	# Add links access <-> hosts
	#import pdb; pdb.set_trace()
	logger.debug("Add link: Access <--> Host")
	#linkopts = dict(bw=self.bw_ac2h)
	linkopts = {'bw':10, 'delay':'15ms'}
	# for k in range(0,100):
	#     tensPlace = int(floor(k/10))
	#     onesPlace = k%10
	self.addLink( self.AccessSwitches[0], self.Hosts[0], **linkopts )
        self.addLink( self.AccessSwitches[0], self.Hosts[1], **linkopts )
        self.addLink( self.AccessSwitches[0], self.Hosts[2], **linkopts )
        self.addLink( self.AccessSwitches[0], self.Hosts[3], **linkopts )
        self.addLink( self.AccessSwitches[0], self.Hosts[4], **linkopts )
        self.addLink( self.AccessSwitches[0], self.Hosts[5], **linkopts )
        self.addLink( self.AccessSwitches[0], self.Hosts[6], **linkopts )
        self.addLink( self.AccessSwitches[0], self.Hosts[7], **linkopts )
        self.addLink( self.AccessSwitches[0], self.Hosts[8], **linkopts )
        self.addLink( self.AccessSwitches[0], self.Hosts[9], **linkopts )

        self.addLink( self.AccessSwitches[1], self.Hosts[10], **linkopts )
        self.addLink( self.AccessSwitches[1], self.Hosts[11], **linkopts )
        self.addLink( self.AccessSwitches[1], self.Hosts[12], **linkopts )
        self.addLink( self.AccessSwitches[1], self.Hosts[13], **linkopts )
        self.addLink( self.AccessSwitches[1], self.Hosts[14], **linkopts )
        self.addLink( self.AccessSwitches[1], self.Hosts[15], **linkopts )
        self.addLink( self.AccessSwitches[1], self.Hosts[16], **linkopts )
        self.addLink( self.AccessSwitches[1], self.Hosts[17], **linkopts )
        self.addLink( self.AccessSwitches[1], self.Hosts[18], **linkopts )
        self.addLink( self.AccessSwitches[1], self.Hosts[19], **linkopts )
	
	self.addLink( self.AccessSwitches[2], self.Hosts[20], **linkopts )
        self.addLink( self.AccessSwitches[2], self.Hosts[21], **linkopts )
        self.addLink( self.AccessSwitches[2], self.Hosts[22], **linkopts )
        self.addLink( self.AccessSwitches[2], self.Hosts[23], **linkopts )
        self.addLink( self.AccessSwitches[2], self.Hosts[24], **linkopts )
        self.addLink( self.AccessSwitches[2], self.Hosts[25], **linkopts )
        self.addLink( self.AccessSwitches[2], self.Hosts[26], **linkopts )
        self.addLink( self.AccessSwitches[2], self.Hosts[27], **linkopts )
        self.addLink( self.AccessSwitches[2], self.Hosts[28], **linkopts )
        self.addLink( self.AccessSwitches[2], self.Hosts[29], **linkopts )

        self.addLink( self.AccessSwitches[3], self.Hosts[30], **linkopts )
        self.addLink( self.AccessSwitches[3], self.Hosts[31], **linkopts )
        self.addLink( self.AccessSwitches[3], self.Hosts[32], **linkopts )
        self.addLink( self.AccessSwitches[3], self.Hosts[33], **linkopts )
        self.addLink( self.AccessSwitches[3], self.Hosts[34], **linkopts )
        self.addLink( self.AccessSwitches[3], self.Hosts[35], **linkopts )
        self.addLink( self.AccessSwitches[3], self.Hosts[36], **linkopts )
        self.addLink( self.AccessSwitches[3], self.Hosts[37], **linkopts )
        self.addLink( self.AccessSwitches[3], self.Hosts[38], **linkopts )
        self.addLink( self.AccessSwitches[3], self.Hosts[39], **linkopts )

	self.addLink( self.AccessSwitches[4], self.Hosts[40], **linkopts )
        self.addLink( self.AccessSwitches[4], self.Hosts[41], **linkopts )
        self.addLink( self.AccessSwitches[4], self.Hosts[42], **linkopts )
        self.addLink( self.AccessSwitches[4], self.Hosts[43], **linkopts )
        self.addLink( self.AccessSwitches[4], self.Hosts[44], **linkopts )
        self.addLink( self.AccessSwitches[4], self.Hosts[45], **linkopts )
        self.addLink( self.AccessSwitches[4], self.Hosts[46], **linkopts )
        self.addLink( self.AccessSwitches[4], self.Hosts[47], **linkopts )
        self.addLink( self.AccessSwitches[4], self.Hosts[48], **linkopts )
        self.addLink( self.AccessSwitches[4], self.Hosts[49], **linkopts )
	
	self.addLink( self.AccessSwitches[5], self.Hosts[50], **linkopts )
        self.addLink( self.AccessSwitches[5], self.Hosts[51], **linkopts )
        self.addLink( self.AccessSwitches[5], self.Hosts[52], **linkopts )
        self.addLink( self.AccessSwitches[5], self.Hosts[53], **linkopts )
        self.addLink( self.AccessSwitches[5], self.Hosts[54], **linkopts )
        self.addLink( self.AccessSwitches[5], self.Hosts[55], **linkopts )
        self.addLink( self.AccessSwitches[5], self.Hosts[56], **linkopts )
        self.addLink( self.AccessSwitches[5], self.Hosts[57], **linkopts )
        self.addLink( self.AccessSwitches[5], self.Hosts[58], **linkopts )
        self.addLink( self.AccessSwitches[5], self.Hosts[59], **linkopts )

        self.addLink( self.AccessSwitches[6], self.Hosts[60], **linkopts )
        self.addLink( self.AccessSwitches[6], self.Hosts[61], **linkopts )
        self.addLink( self.AccessSwitches[6], self.Hosts[62], **linkopts )
        self.addLink( self.AccessSwitches[6], self.Hosts[63], **linkopts )
        self.addLink( self.AccessSwitches[6], self.Hosts[64], **linkopts )
        self.addLink( self.AccessSwitches[6], self.Hosts[65], **linkopts )
        self.addLink( self.AccessSwitches[6], self.Hosts[66], **linkopts )
        self.addLink( self.AccessSwitches[6], self.Hosts[67], **linkopts )
        self.addLink( self.AccessSwitches[6], self.Hosts[68], **linkopts )
        self.addLink( self.AccessSwitches[6], self.Hosts[69], **linkopts )

	self.addLink( self.AccessSwitches[7], self.Hosts[70], **linkopts )
        self.addLink( self.AccessSwitches[7], self.Hosts[71], **linkopts )
        self.addLink( self.AccessSwitches[7], self.Hosts[72], **linkopts )
        self.addLink( self.AccessSwitches[7], self.Hosts[73], **linkopts )
        self.addLink( self.AccessSwitches[7], self.Hosts[74], **linkopts )
        self.addLink( self.AccessSwitches[7], self.Hosts[75], **linkopts )
        self.addLink( self.AccessSwitches[7], self.Hosts[76], **linkopts )
        self.addLink( self.AccessSwitches[7], self.Hosts[77], **linkopts )
        self.addLink( self.AccessSwitches[7], self.Hosts[78], **linkopts )
        self.addLink( self.AccessSwitches[7], self.Hosts[79], **linkopts )

	self.addLink( self.AccessSwitches[8], self.Hosts[80], **linkopts )
        self.addLink( self.AccessSwitches[8], self.Hosts[81], **linkopts )
        self.addLink( self.AccessSwitches[8], self.Hosts[82], **linkopts )
        self.addLink( self.AccessSwitches[8], self.Hosts[83], **linkopts )
        self.addLink( self.AccessSwitches[8], self.Hosts[84], **linkopts )
        self.addLink( self.AccessSwitches[8], self.Hosts[85], **linkopts )
        self.addLink( self.AccessSwitches[8], self.Hosts[86], **linkopts )
        self.addLink( self.AccessSwitches[8], self.Hosts[87], **linkopts )
        self.addLink( self.AccessSwitches[8], self.Hosts[88], **linkopts )
        self.addLink( self.AccessSwitches[8], self.Hosts[89], **linkopts )
	
	self.addLink( self.AccessSwitches[9], self.Hosts[90], **linkopts )
        self.addLink( self.AccessSwitches[9], self.Hosts[91], **linkopts )
        self.addLink( self.AccessSwitches[9], self.Hosts[92], **linkopts )
        self.addLink( self.AccessSwitches[9], self.Hosts[93], **linkopts )
        self.addLink( self.AccessSwitches[9], self.Hosts[94], **linkopts )
        self.addLink( self.AccessSwitches[9], self.Hosts[95], **linkopts )
        self.addLink( self.AccessSwitches[9], self.Hosts[96], **linkopts )
        self.addLink( self.AccessSwitches[9], self.Hosts[97], **linkopts )
        self.addLink( self.AccessSwitches[9], self.Hosts[98], **linkopts )
        self.addLink( self.AccessSwitches[9], self.Hosts[99], **linkopts )

	logger.debug("Finished adding links!")


topos = { 'mytopo': ( lambda: MyTopo() ) }
setLogLevel('info')
fattree = MyTopo()
