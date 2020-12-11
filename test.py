from refex.extractor import RefExtractor

extractor = RefExtractor()

def extract(text):
    content, markers = extractor.extract(text, ignore_case=True)
    return [m.text for m in markers]

print(extract('<p>Ein Satz mit § 3b AsylG, § 3b asylg und weiteren Sachen.</p>'))

print(extract('Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 167 VwGO i.V.m. §§ 708 Nr. 11, 711 ZPO.'))

print(extract('Bar und bar §§ 1, 2 Abs. 2, 3, 10 Abs. 1 Nr. 1 BGB foo.'))


print(extract('sonderzahlung § 5 abs. 1 bgb kündigung'))

print(extract('§ 92 betrvg personalplanung'))