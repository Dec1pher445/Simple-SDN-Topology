#!/usr/bin/env python3

from mininet.topo import Topo

class MyTopo( Topo ):

   def __init__( self ):
      
      #"Create custom topo."

      # Initialize topology
      Topo.__init__( self )

      # Add hosts and switches
      rightHost = self.addHost( 'h1' )
      rightHost1 = self.addHost( 'h2' )
      leftHost = self.addHost( 'h3' )
      leftHost1 = self.addHost( 'h4' )
      leftHost2 = self.addHost ( 'h5' )
      leftSwitch = self.addSwitch( 's2' )
      rightSwitch = self.addSwitch( 's1' )

      # Add links between hosts and switches
      self.addLink( rightHost, rightSwitch )
      self.addLink( rightHost1, rightSwitch )
      self.addLink( leftHost, leftSwitch )
      self.addLink(leftHost2, leftSwitch )
      self.addLink( leftHost1, leftSwitch )
         
      # creating the bridge between switch1 and switch2 
      self.addLink( leftSwitch, rightSwitch )

topos = { 'mytopo': ( lambda: MyTopo() ) }