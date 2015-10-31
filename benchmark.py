def benchmark(source, codeMap):
    print('source entropy: ', source.entropy())
    print('code mean symbol length: ', codeMap.meanLength())
    print('code efficiency: ', 100*source.entropy()/codeMap.meanLength(), '%')
    print('Kraft number: ', codeMap.kraft())
