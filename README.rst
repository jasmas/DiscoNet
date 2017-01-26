DiscoNet module
###############

This module scans specified subnets and IPs for SSH servers that can be accessed with the
provided credentials and populates an xlsx workbook with the output.

.. image:: DiscoNet.png
   :alt: DiscoNet GUI

Installation
------------

A binary distribution is available for OS X `here <https://github.com/jasmas/DiscoNet/releases/latest>`_.

To install DiscoNet, install python on your system and run the following from the DiscoNet
source tree::

    $ python setup.py install

DiscoNet makes use of Kivy for GUI components which is distributed with binary wheels for
python versions 2.7 and 3.4. Stick to those versions to avoid having to build Kivy.

Usage
-----

The GUI and command line application take several input parameters:
    * workbook: Path to output xlsx file
    * subnets: Comma delimited list of networks and IP addresses to scan
    * username: SSH username
    * password: SSH password
    * commands: String listing commands to run, one per line

Examples:
    To open the GUI application::
    
        $ python -m DiscoNet
    
    To scan and create a discovery workbook from the command line::
    
        $ python -m DiscoNet.discoveryscan workbook subnets username password commands
    
    A convenience script is included so that the GUI and command line utility can each be
    run using the following commands accordingly::
    
        $ DiscoNet
        $ discoveryscan workbook subnets username password commands
    
    To use as a module in your own application::
    
        from DiscoNet.discoveryscan import DiscoveryScan
        
        d = DiscoveryScan(workbook, subnets, username, password, commands)
        d.start()
        
    The start method will block until the scan is complete. Optionally, the start method
    can be non-blocking when supplied with an optional callback function::
    
        from DiscoNet.discoveryscan import DiscoveryScan
        
        def cb()
            #callback function
            return
        
        d = DiscoveryScan(workbook, subnets, username, password, commands)
        d.start(cb)
