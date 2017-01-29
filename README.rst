DiscoNet module
###############

DiscoNet scans specified subnets and IPs for SSH servers that can be accessed with the
provided credentials and executes an arbitrary list of commands.

.. image:: screenshot.png
   :alt: DiscoNet GUI

The process of scanning networks and collecting command output is built on a multiprocess
architecture, so DiscoNet can rapidly scan through management and loopback subnets,
populating an xlsx workbook with the output.

To use the module in your own projects, please reference the `API Documentation <https://disconet.readthedocs.io>`_.

Installation
------------

Binary distributions for OS X and Windows are available `here <https://github.com/jasmas/DiscoNet/releases>`_.

To install DiscoNet, install python on your system and run the following from the DiscoNet
source tree::

    $ python setup.py install

DiscoNet makes use of Kivy for GUI components which is distributed with binary wheels for
python versions 2.7 and 3.4. Stick to those versions to avoid having to build Kivy. If you
wish to use a different version of python, you will first need to install Kivy, by
following the instructions for your platform `here <https://kivy.org/docs/installation/installation.html>`_, before installing DiscoNet.

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

    To use as a module in your own application::
    
        from DiscoNet.discoveryscan import DiscoveryScan
        
        d = DiscoveryScan(workbook, subnets, username, password, commands)
        d.start()
        
    The commands parameter should be an array of command strings to run. The start method
    will block until the scan is complete. Optionally, the start method can be
    non-blocking when supplied with a callback function::
    
        from DiscoNet.discoveryscan import DiscoveryScan
        
        def cb()
            #callback function
            return
        
        d = DiscoveryScan(workbook, subnets, username, password, commands)
        d.start(cb)
