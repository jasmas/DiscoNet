DiscoNet module
###############

This module scans specified subnets and IPs for SSH servers that can be accessed with the
provided credentials and populates an xlsx workbook with the output.

.. image:: https://raw.githubusercontent.com/jasmas/DiscoNet/master/doc/_static/DiscoNet.png
   :alt: DiscoNet GUI

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
    
        from DiscoNet import DiscoveryScan
        
        d = DiscoveryScan(workbook, subnets, username, password, commands)
        d.start()
        
    The start method will block until the scan is complete. Optionally, the start method
    can be non-blocking when supplied with an optional callback function::
    
        from DiscoNet import DiscoveryScan
        
        def cb()
            #callback function
            return
        
        d = DiscoveryScan(workbook, subnets, username, password, commands)
        d.start(cb)
