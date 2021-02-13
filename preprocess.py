# preprocess

whitelist = "\n「」。、あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゐゆゑよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽぁぃぅぇぉゃゅょっゎ"
whitelist = set(whitelist)
with open("input.txt", "r") as f:
    for l in f:
        for c in l:
            if c in whitelist:
                print(c, end="")