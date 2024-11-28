import hashlib

s = "DM Fall 2024 HW3"

#SHA-256 хэш строки s
h = hashlib.sha256(s.encode('utf-8')).hexdigest()

#хэш в 256-битную двоичную строку с ведущими нулями
b = bin(int(h, 16))[2:].zfill(256)

#разделение строки b на восемь 32-х битные части
slices = [b[i:i + 32] for i in range(0, 256, 32)]

#применим XOR ко всем частям из "slices"
xor_result = 0
for binary_slice in slices:
    xor_result ^= int(binary_slice, 2)

#Рассчитать w = d ⊕ 0x7613a0ca
d = xor_result
w = d ^ 0x7613a0ca

print("hash (256-bit):", b)
print("32-bit Slices:", slices)
print("d:", bin(d)[2:].zfill(32))
print("w:", bin(w)[2:].zfill(32))
