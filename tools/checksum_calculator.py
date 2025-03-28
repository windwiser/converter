def b_and_g_checksum(data: bytes) -> int:
    """Calculate checksum using the B&G style (0x100 - sum(data) % 256)."""
    return (256 - sum(data[:-1]) % 256) % 256

def verify_checksum(data: bytes) -> bool:
    """Check if the last byte is a valid checksum."""
    return (sum(data) % 256) == 0

# Sample packets
jobb_110_b = b'\xFF\x70\x0C\x01\x84\x4E\x88\x03\x45\x51\x01\x00\x6E\x52\x08\x4E\x34\xF0'
jobb_120_b = b'\xFF\x70\x0C\x01\x84\x4E\x88\x01\x74\x51\x01\x00\x78\x52\x08\x55\x50\x96'
jobb_90_b  = b'\xFF\x70\x0C\x01\x84\x4E\x88\x00\x00\x51\x01\x00\x5A\x52\x08\x00\x00\xCE'
jobb_91_b  = b'\xFF\x70\x0C\x01\x84\x4E\x88\x00\x00\x51\x01\x00\x5B\x52\x08\x00\x00\xCD'
bal_90_b   = b'\xFF\x70\x0C\x01\x84\x4E\x88\x00\x00\x51\x01\xFF\xA6\x52\x08\x00\x00\x83'
bal_21_b   = b'\xFF\x70\x0C\x01\x84\x4E\x88\x00\x00\x51\x01\xFF\xEB\x52\x08\x00\x00\x3E'

# List of packets for easy checking
packets = {
    "jobb_110_b": jobb_110_b,
    "jobb_120_b": jobb_120_b,
    "jobb_90_b": jobb_90_b,
    "jobb_91_b": jobb_91_b,
    "bal_90_b": bal_90_b,
    "bal_21_b": bal_21_b,
}

# Check each packet
for name, packet in packets.items():
    is_valid = verify_checksum(packet)
    calculated = b_and_g_checksum(packet)
    actual = packet[-1]
    print(f"{name}: {is_valid}, checksum = 0x{actual:02X}, calculated = 0x{calculated:02X}")
