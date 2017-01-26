# -*- coding: utf-8 -*-
"""
DiscoNet module

This module scans specified subnets and IPs for SSH servers that can be accessed with the
provided credentials and populates an xlsx workbook with the output.

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
    can be non-blocking when supplied with a callback function::
    
        from DiscoNet.discoveryscan import DiscoveryScan
        
        def cb()
            #callback function
            return
        
        d = DiscoveryScan(workbook, subnets, username, password, commands)
        d.start(cb)
"""
__name__ = 'DiscoNet'
__description__ = 'A tool for automating network discovery.'
__url__ = 'https://github.com/jasmas/DiscoNet'
__author__ = 'Jason Masker'
__copyright__ = 'Copyright © 2017 Jason Masker <masker@post.harvard.edu>'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jason Masker'
__email__ = 'masker@post.harvard.edu'
