
if __name__ == '__main__':

    import sys
    numero = sys.argv[1]
    vlan = sys.argv[2]

    red_piso = int(numero) << 3
    red_vlan = int(vlan) + 100

    red = "10.{}.{}.0".format(red_vlan, red_piso)
    red_con_mascara = "{}/21".format(red)
    router_ip = "10.{}.{}.1".format(red_vlan, red_piso)
    interface = "vlan_{}_{}".format(numero,vlan)
    pool_name = "dhcp_pool_{}".format(interface)
    dhcp_name = "dhcp_{}".format(interface)

    import ipaddress

    ired_con_mascara = ipaddress.ip_network(red_con_mascara)
    _ihosts = list(ired_con_mascara.hosts())[-200:]
    ip1 = "{}".format(_ihosts[0])
    ip2 = "{}".format(_ihosts[-1])

    configure_vlan = f"interface vlan add interface=bond2 name={interface} vlan-id={vlan}"
    configure_ip = f"ip address add address={router_ip}/21 interface={interface} network={red}"

    generate_pool = f"ip pool add name={pool_name} ranges={ip1}-{ip2}"
    configure_dhcp_network = f"ip dhcp-server network add address={red} dns-server=169.254.254.253 gateway={router_ip}"
    generate_server = f"ip dhcp-server add address-pool={pool_name} disabled=no interface={interface} name={dhcp_name}"

    print(configure_vlan)
    print(configure_ip)
    print(generate_pool)
    print(configure_dhcp_network)
    print(generate_server)
