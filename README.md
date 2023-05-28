# Introduction: Hub-Finder
The purpose of this Ansible playbook and associated files is to help find un-managed switches (often inaccurately referred to as a 'hub') on a network running Cisco IOS based devices at the access layer.

# Getting Started
This playbook was created to help with identifying switchports at the access layer that have more than one mac address attached, or if they have a Cisco IP phone connected, only contain two unique mac addresses.  Ports that should be exempt from this compliance check(such as uplinks to a distribution switch) can be updated in a per-device yaml file located in the hostvars directory.

This playbook uses a number of filter plugins written in python.  They are primarily used to try and normalize the data returned from the cisco switches and create a uniform data model where all the necessary information gathered from the show commands is consolidated into a dictionary per interface, per switch.

The information gathered from each switch is parsed wth [TextFSM templates from NTC](https://github.com/networktocode/ntc-templates). One of the templates 'cisco_ios_show_power_inline-all' was a 

## Running the playbook
1.	
2.	Software dependencies
3.	Latest releases
4.	API references


