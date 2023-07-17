from ...symbols import NORM, ORTH
from ...util import update_exc
from ..tokenizer_exceptions import BASE_EXCEPTIONS

_exc = {
    "isa'y": [{ORTH: "isa"}, {ORTH: "'y", NORM: "ay"}],
    "baya'y": [{ORTH: "baya"}, {ORTH: "'y", NORM: "ay"}],
    "sa'yo": [{ORTH: "sa"}, {ORTH: "'yo", NORM: "iyo"}],
    "ano'ng": [{ORTH: "ano"}, {ORTH: "'ng", NORM: "ang"}],
    "nawa'y": [{ORTH: "nawa"}, {ORTH: "'y", NORM: "ay"}],
    "papa'no": [{ORTH: "papa'no", NORM: "papaano"}],
    "'di": [{ORTH: "'di", NORM: "hindi"}],
}

# Pronouns
for pron in ["ako", "tayo", "kami", "kayo", "siya", "sila", "kanya", "kanila"]:
    for orth in [pron, pron.title()]:
        _exc[orth + "'y"] = [
            {ORTH: orth, NORM: pron},
            {ORTH: "'y", NORM: "ay"},
        ]




TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, _exc)
