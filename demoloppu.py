def demoloppu(kivet):
    ö = 0
    loppu = 0
    while ö < kivet:
        loppu = loppu + random.randint(1, 6)
        ö = ö + 1
    return loppu

demoloppu(kerätyt_kivet)
