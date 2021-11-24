from enaCRAM import enaCRAM

ena = enaCRAM()


print("Testing validate_sid")

print()
sid = "3050107579885e1608e6fe50fae3f8d0"
print("sid = {}".format(sid))
try:
    ena.validate_sid(sid)
    print("Test good MD5 hash string: Pass")
except Exception as e:
    print("Test good MD5 hash string: Fail")

print()
sid = "an invalid string"
print("sid = {}".format(sid))
try:
    ena.validate_sid(sid)
    print("Test bad MD5 string to ValueError: Fail")
except Exception as e:
    print("Test bad MD5 string to ValueError: Pass")

print()
sid = 1234567890
print("sid = {}".format(sid))
try:
    ena.validate_sid(sid)
    print("Test integer to TypeError: Fail")
except Exception as e:
    print("Test integer to TypeError: Pass")