
def calculate_open_port(ip_address):
    parts = ip_address.split('.')
    total = sum(int(part) for part in parts)
    open_port = total * int(parts[0])
    return open_port

ip_address = input("Tanpri, tape adrès IP a: ")
open_port = calculate_open_port(ip_address)
print("Pòt ki ouvri a se:", open_port)