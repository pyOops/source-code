BULKER_AND_GENERAL_CARGO = 0.56
TANKERS = 0.59
PASSENGER_SHIPS_AND_FERRIES = 0.65

def M_RE(P, type):
    return type*P**0.7

def E(L, B, T, D):
    return L*(B+T)+0.85*L*(D-T)

def Cb(CB, D, T):
    return CB + (1-CB)*(0.8*D-T)/(3*T)

def LS(Ws, Wo, Wm):
    return 1.02*(Ws+Wo+Wm)