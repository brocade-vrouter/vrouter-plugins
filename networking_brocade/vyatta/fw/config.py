from networking_brocade.vyatta.common import config 

#5600 command dictionary
FW_5600_commands = {
'FW_NAME' : 'security/firewall/name/{0}',
'FW_DESCRIPTION' : 'security/firewall/name/{0}/description/{1}',
'FW_RULE_DESCRIPTION' : 'security/firewall/name/{0}/rule/{1}/description/{2}',
'FW_RULE_PROTOCOL' : 'security/firewall/name/{0}/rule/{1}/protocol/{2}',
'FW_RULE_SRC_PORT' : 'security/firewall/name/{0}/rule/{1}/source/port/{2}',
'FW_RULE_DEST_PORT' : 'security/firewall/name/{0}/rule/{1}/destination/port/{2}',
'FW_RULE_SRC_ADDR' : 'security/firewall/name/{0}/rule/{1}/source/address/{2}',
'FW_RULE_DEST_ADDR' : 'security/firewall/name/{0}/rule/{1}/destination/address/{2}',
'FW_RULE_ACTION' : 'security/firewall/name/{0}/rule/{1}/action/{2}',
'FIREWALL'       : 'security/firewall',
};

zone_commands_5600 = {
'ZONE_INTERFACE_CMD' : 'security/zone-policy/zone/{0}/interface/{1}',
'ZONE_FIREWALL_CMD'  : 'security/zone-policy/zone/{0}/to/{1}/firewall/{2}',
'ZONE_POLICY'        : 'security/zone-policy',
};

#5400 command
FW_5400_commands = {
'FW_NAME' : 'firewall/name/{0}',
'FW_DESCRIPTION' : 'firewall/name/{0}/description/{1}',
'FW_ESTABLISHED_ACCEPT' : 'firewall/state-policy/established/action/accept',
'FW_RELATED_ACCEPT' : 'firewall/state-policy/related/action/accept',
'FW_RULE_DESCRIPTION' : 'firewall/name/{0}/rule/{1}/description/{2}',
'FW_RULE_PROTOCOL' : 'firewall/name/{0}/rule/{1}/protocol/{2}',
'FW_RULE_SRC_PORT' : 'firewall/name/{0}/rule/{1}/source/port/{2}',
'FW_RULE_DEST_PORT' : 'firewall/name/{0}/rule/{1}/destination/port/{2}',
'FW_RULE_SRC_ADDR' : 'firewall/name/{0}/rule/{1}/source/address/{2}',
'FW_RULE_DEST_ADDR' : 'firewall/name/{0}/rule/{1}/destination/address/{2}',
'FW_RULE_ACTION' : 'firewall/name/{0}/rule/{1}/action/{2}',
'FIREWALL'       : 'firewall',
'FIREWALL_STATE_POLICY' : 'firewall/state-policy',
};

zone_commands_5400 = {
'ZONE_INTERFACE_CMD' : 'zone-policy/zone/{0}/interface/{1}',
'ZONE_FIREWALL_CMD'  : 'zone-policy/zone/{0}/from/{1}/firewall/name/{2}',
'ZONE_POLICY'        : 'zone-policy',
};

fw_commands = { 
                 config.VROUTER_VSE_MODEL : FW_5400_commands, 
                 config.VROUTER_VR_MODEL : FW_5600_commands,
              }

zone_commands = {
                  config.VROUTER_VSE_MODEL : zone_commands_5400,
                  config.VROUTER_VR_MODEL  : zone_commands_5600,
                }
