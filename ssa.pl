%fatos

pai(mary,jane).
pai(jane,karen).								
pai(john,jim).
pai(mary,john).
pai(jane,bill).

%regras

irmao(A,B) :- pai(X,A), pai(X,B), A\=B.

primo(A,B):- irmao(X,Y), pai(X,A), pai(Y,B).