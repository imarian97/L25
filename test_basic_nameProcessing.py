from nameProcessing import numeScurte

def test_simplu():
    L=["Marian","Ion","Gigel","Ab"]
    Ln=numeScurte(L)

    assert "Ion" in Ln
    assert "Ab" in Ln
    # if "Ion" not in Ln: raise SystemError("Nu e bine")
    assert len(Ln)==2
    # if len(Ln)!=1: raise SystemError("Lungimea nu e buna")


def test_avansat():
    listaDeNume=["Marian","Gigel"]
    listaFiltrata=numeScurte(listaDeNume)

    assert len(listaFiltrata)==0
    # if len(listaFiltrata)!=0: raise SystemError("Nu e bine")
    assert listaDeNume==["Marian","Gigel"]
    # if listaDeNume!=["Marian","Gigel"]: raise SystemError("Nu e bine")


# teste=[test_simplu,test_avansat]
# for t in teste: t()
# totulOk=False not in [t() for t in teste]
# print(totulOk)