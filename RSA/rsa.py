## RSA Implementation
##
##


## Import Modules
##
import random, math
from fractions import gcd


## FUNCTIONS
##
# Function to test for composite. Return True for composite.
def _func_composite_test(a,d,n,s):
    if pow( a, d, n ) == 1:
        return False
    for i in range(s):
        if pow( a, 2**i * d, n ) == n-1:
            return False
    return True
# Function to test for primality using Miller Rabin.
def _func_millerRabin_probable_prime( n ):
    assert n >= 2
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Write n-1 as 2**s * d
    # Repeatedly try to divide n-1 by 2
    s, d = 0, n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert ( 2**s * d == n-1 )
    # test the base a to see whether it is a witness for the compositeness of n
    for i in range(0,10): # range is arbitrary...
        a = random.randint( 2, n-1 )
        if _func_composite_test(a,d,n,s):
            return False
    # Return True because n is not found to be a composite.
    return True
# Function to calculate inverse of a modulo m.
def _mod_inv( a, m ):
    # Check if they are relatively prime.
    if gcd(a,m) != 1:
        return 0
    else:
        linearcombination = extendedEuclid(a, m)
        return linearcombination[1] % m



## RSA Class
##
class RSA(object):
    
    # Initialize by setting two primes
    # Then calculate N and phi from p and q
    # Pick encryption exponent e and decryption exp. d
    def __init__( self ):
        self.set_primes( 10 ** 10, 10 ** 11 )
        self.N = self.p * self.q
        self.N_phi = (self.p-1) * (self.q-1)
        self.set_exponents()
    
    def set_primes( self, lower_lim, upper_lim ):
        try:
            self.p = self.find_prime( lower_lim, upper_lim )
            while True:
                self.q = self.find_prime( lower_lim, upper_lim )
                if self.q != self.p:
                    break
        except:
            raise ValueError

    def find_prime( self, a, b ):
        # Return a pseudo prime number roughly between a and b (can be larger than b).
        # Raise ValueError if cannot find a pseudo prime after 10 * ln(x) + 3 tries.
        x = random.randint(a, b)
        for i in range( 0, int(10 * math.log(x) + 3) ):
            if _func_millerRabin_probable_prime(x):
                return x
            else:
                x += 1
        raise ValueError

    def set_exponents( self ):
        # Obtain e.
        if self.N_phi > 65537:
            self.e = 65537
        else:
            while True:
                self.e = random.randint( 1, self.N_phi )
                # Check if they are relatively prime.
                if gcd( self.e, self.N_phi ) == 1:
                    break
        # Get d as the inverse of e modulo N_phi
        self.d = self.get_exp_d( self.e, self.N_phi )

    def get_exp_d( self, e, phi ):
        # Obtains d based on e and phi.
        x = lasty = 0
        lastx = y = 1
        while phi != 0:
            q = e // phi
            e, phi = phi, e % phi
            x, lastx = lastx - q*x, x
            y, lasty = lasty - q*y, y
        if lastx < 0:
            lastx += self.N_phi
        return lastx




## MAIN
##
if __name__=="__main__":
    rsa = RSA()
    print "p/q:", rsa.p, " / ", rsa.q
    print "gcd: ", gcd( rsa.p, rsa.q )
    print "N: ", rsa.N
    print "e (enc): ", rsa.e
    print "d (dec): ", rsa.d
    print "e*d%phi: ", rsa.e * rsa.d % rsa.N_phi