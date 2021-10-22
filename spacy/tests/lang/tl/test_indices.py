def test_tl_simple_punct(tl_tokenizer):
    text = "Sige, punta ka dito"
    tokens = tl_tokenizer(text)
    assert tokens[0] == 0
    assert tokens[1] == 4
    assert tokens[2] == 6
    assert tokens[3] == 12
    assert tokens[4] == 15
