#!/usr/bin/python

import random, gmpy2


## FUNCTIONS
##
def print_line():
    print 20 * "--"



## MAIN
##
if __name__=="__main__":

    ## Setup variables.
    p = 17
    q = 29
    N = p * q
    N_phi = (p-1) * (q-1)
    ## Obtain e (encryption exponent). Has to be co-prime to N_phi
    while True:
        e = random.randint( 2, N_phi )
        if gmpy2.gcd( e, N_phi )==1:
            break
    ## Find d (decryption exponent). Has to be inverse of e mod N_phi.
    d = gmpy2.invert( e, N_phi )
    assert d>0
    ## Print results.
    print_line()
    print_line()
    print "Prime P:   ", p
    print "Prime Q:   ", q
    print "N:         ", N
    print_line()
    print "N (Phi):   ", N_phi
    print "e (enc):   ", e
    print "d (dec):   ", d
    print_line()
    print_line()

    msg = "6"
    print "MSG:       ", msg
    print "MSG (Hex): ", msg.encode('hex')
    print "MSG (int): ", int( msg.encode('hex'), 16 )
    print_line()
    msg_enc = pow( int( msg.encode('hex'), 16 ), e, N )
    print "MSG (enc): ", msg_enc
    print "MSG (dec): ", pow( msg_enc, d, N )

