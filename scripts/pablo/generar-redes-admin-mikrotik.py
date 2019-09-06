
if __name__ == '__main__':

    import sys
    piso = sys.argv[1]
    interface_base = sys.argv[2]

    import ipaddress

    red_base = f"172.25.{piso}.0/24"
    ired_base = ipaddress.ip_network(red_base)

    parametros = [
        {'nombre':'switchs', 'vlan':0},
        {'nombre':'infraestructura', 'vlan':64},
        {'nombre':'camaras', 'vlan':128},
        {'nombre':'aps', 'vlan':192}
    ]

    for (indice,redes) in enumerate(ired_base.subnets(new_prefix=26)):
        red = str(redes.network_address)
        red_con_mascara = str(redes)
        router_ip = str(list(redes.hosts())[0])

        vlan = parametros[indice]['vlan']
        if vlan == 0:
            interface = interface_base
        else:
            interface = "vlan_{}_{}".format(parametros[indice]['nombre'], piso)

        pool_name = "dhcp_pool_{}".format(interface)
        dhcp_name = "dhcp_{}".format(interface)
        ip1 = list(redes.hosts())[10]
        ip2 = list(redes.hosts())[-1]

        if vlan > 0:
            configure_vlan = f"interface vlan add interface={interface_base} name={interface} vlan-id={vlan}"

        configure_ip = f"ip address add address={router_ip}/21 interface={interface} network={red}"

        generate_pool = f"ip pool add name={pool_name} ranges={ip1}-{ip2}"
        configure_dhcp_network = f"ip dhcp-server network add address={red} dns-server=169.254.254.253 gateway={router_ip}"
        generate_server = f"ip dhcp-server add address-pool={pool_name} disabled=no interface={interface} name={dhcp_name}"

        print('------------\n\n')
        if vlan > 0:
            print(configure_vlan)
        print(configure_ip)
        print(generate_pool)
        print(configure_dhcp_network)
        print(generate_server)