def generate_matching_df(template, color_lookup, top=20, sample=15):
    """generate_matching_df (worst function name ever)
    this will generate a dataframe with x,y, corr, and png file path for images that most highly match each sampled pixel. The df gets parsed to json that plugs into d3 grid 
    """
    # Now read in our actual image
    base = Image.open(template)
    width, height = base.size
    pixels = base.load()
    data = []

    count = 0
    new_image = pandas.DataFrame(columns=["x", "y", "corr", "png"])

    for x in range(width):
        for y in range(height):
            # And take only every [sample]th pixel
            if np.remainder(x, sample) == 0 and np.remainder(y, sample) == 0:
                cpixel = pixels[x, y]
                tmp = color_lookup.copy()
                tmp = (tmp - cpixel).abs().sum(axis=1)
                tmp.sort()
                png = choice(tmp.loc[tmp.index[0:top]].index.tolist(), 1)[0]
                new_image.loc[count] = [x, y, 0, png]
                count += 1

    new_image["x"] = [int(x) for x in (new_image["x"] / sample) * 10]
    new_image["y"] = [int(x) for x in (new_image["y"] / sample) * 10]

    return new_image
