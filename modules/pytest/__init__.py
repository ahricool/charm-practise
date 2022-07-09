
i=10
k=i
print(id(i),i)
print(id(k),k)
i=20
print(id(i),i)
print(id(k),k)

bits=b"""# Etkin kullan\xc4\xb1c\xc4\xb1 say\xc4\xb1s\xc4\xb1 #', '# En \xc3\xb6nemli d\xc3\xb6n\xc3\xbc\xc5\x9f\xc3\xbcm etkinlikleri #', '# G\xc3\xbcnl\xc3\xbck kullan\xc4\xb1c\xc4\xb1 etkile\xc5\x9fimi #', '# Toplam gelir #', '# Kilitlenme sorunu ya\xc5\x9famayan kullan\xc4\xb1c\xc4\xb1lar #', '# Uygulama s\xc3\xbcr\xc3\xbcm\xc3\xbc kullan\xc4\xb1m\xc4\xb1 #', '# Edinme #', '# Elde tutma kohortlar\xc4\xb1 #', '# Kitle #', '# Kitle #"""
str=str(bits,encoding="utf-8")
print(str)