price = input("Prix revendeur: ")

def vinted():
  result = (((int(price) * 5) / 100) + 0.7 + int(price))
  return result

print("Prix avec charges vinted (HFDP): " + str(vinted()))