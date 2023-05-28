# Introduction: Hub-Finder
The purpose of this Ansible playbook and associated files is to help find un-managed switches (often inaccurately referred to as a 'hub') on a network running Cisco IOS based devices at the access layer.

# Getting Started
This playbook **'hub-finder.yml'** was created to help with identifying switchports at the access layer that have more than one mac address attached, or if they have a Cisco IP phone connected, only contain two unique mac addresses.  Ports that should be exempt from this compliance check(such as uplinks to a distribution switch) can be updated in a per-device yaml file located in the hostvars directory.

This playbook uses a number of filter plugins written in python.  They are primarily used to try and normalize the data returned from the cisco switches and create a uniform data model where all the necessary information gathered from the show commands is consolidated into a dictionary per interface, per switch.

The information gathered from each switch is parsed wth [TextFSM templates from NTC](https://github.com/networktocode/ntc-templates). One of the templates 'cisco_ios_show_power_inline-all' is not a part of that repo and something I originally had to recreate to help determine if a connected device was a non-cisco access point that trunked/bridged traffic from the AP to the switch.  I ended up not needing this function in the end, but the template and parsing still remains for the time being.

## Running the playbook
1.	The target group used select hosts for the play to run on must match in both the playbook:
```yaml
- name: Collect, Parse and Store Switch Data With Show Commands
  hosts: asw
```
 and in the j2 template named 'hub-yaml':
```jinja2
{% if 'asw' in facts.group_names %}
```
2.	Not every task in the first play needs to be executed. Specifically, writing the interface data to files for each host. The playbook can be sped up by commenting these out, but they are useful for de-bugging and validating that the data is being processed correctly.

3.	It should go without saying, but a working ansible inventory and ssh credential will need to be configured for this playbook to run in your environment. 

4. A simple Docker file has been included for managing the python environment and dependencies. 

5. The hostvars file 'interface_exemption.yaml' is required for the playbook to run.  There  two playbooks (located under the 'helper_playbooks' directory) that can be helpful for setting up these var files quickly as well as testing to make sure the host pattern match you intend to use matches the correct group of hosts.

