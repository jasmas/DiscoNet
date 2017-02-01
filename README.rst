DiscoNet Package
################

DiscoNet scans specified subnets and IPs for SSH servers that can be accessed with the
provided credentials and executes an arbitrary list of commands.

.. image:: screenshot.png
   :alt: DiscoNet Screenshot

The process of scanning networks and collecting command output is built on a multiprocess
architecture, so DiscoNet can rapidly scan through management and loopback subnets,
populating an xlsx workbook with the output.

Installation
------------

Install DiscoNet using the latest version of setuptools and pip::

    $ pip install --upgrade setuptools pip
    $ pip install DiscoNet

You can also opt to install the DiscoNet GUI which uses to Kivy library. To install it,
you will first need to follow the `Kivy Installation Instructions <https://kivy.readthedocs.io/en/latest/installation/installation.html>`_ for your platform.
Then install DiscoNet with the GUI marker::

    $ pip install DiscoNet[kivy]

Binary distributions for OS X and Windows are available `here <https://github.com/jasmas/DiscoNet/releases>`_.

Usage
-----

The GUI and command line application take several input parameters:
    * workbook: Path to output xlsx file
    * subnets: Comma delimited list of networks and IP addresses to scan
    * username: SSH username
    * password: SSH password
    * commands: One per line in the GUI or passed as parameters from the command line

Examples:
    To open the GUI application::
    
        $ python -m DiscoNet
    
    To scan and create a discovery workbook from the command line::
    
        $ python -m DiscoNet.discoveryscan workbook subnets username password commands
    
    A convenience script is included so that the GUI and command line utility can each be
    run using the following commands accordingly::
    
        $ DiscoNet
        $ discoveryscan workbook subnets username password commands ...
    
    Use double quotes for each command and include as many as required, e.g.::
    
        $ discoveryscan out.xlsx 172.16.0.0/24 admin password "show ver" "show run"

API
---

To use the module in your own projects, please reference the `API Documentation <https://disconet.readthedocs.io>`_.

Examples:
    Initiate a discovery scan from python::
    
        from DiscoNet.discoveryscan import DiscoveryScan
        
        d = DiscoveryScan(workbook, subnets, username, password, [commands, ...])
        d.start()
        
    The commands parameter should be a list of command strings. The start method will
    block until the scan is complete. Optionally, the start method can be non-blocking
    when supplied with a callback function::
    
        from DiscoNet.discoveryscan import DiscoveryScan
        
        def cb()
            #callback function
            return
        
        d = DiscoveryScan(workbook, subnets, username, password, [commands, ...])
        d.start(cb)
