"""Search for different IoTs. Find interesting hosts that have: OS information, specific vulnerabilities, etc."""
"""
list_devices = ['webcam', 'router', 'Amazon Echo', 'printer', 'light']
list_exploits_type = ['dos', 'local', 'remote', 'shellcode', ' webapps']
industrial_control = ['xzeres wind', 'modbus port:502', 'dnp port:2000', 'siemens port:102']
databases = ['product:MongoDB', 'port:5432 PostgreSQL', 'product:MySQL', 'elastic port:9200 json', 'product:Redis']
videogames = ['Minecraft Server port:25565', 'product:"Counter-Strike Global Offensive"', 'product:"Starbound"', 'product:"ARK Survival Evolved"']
"""

# Search
# Save IPs if: they have OS, they have more than 3 exposures, they have more than 1 open port 