"""
    This file contains the implementation of the NIST tests for randomness.
    All tests are documented in the NIST documentation (https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-22r1a.pdf).
"""

import copy
import math
import numpy as np
from scipy.special import gammaincc
import scipy.fftpack as sff
import scipy.special as spc
from scipy.stats import norm


class Tester:
    def __init__(self, inputData, debug=False) -> None:
        self.input = inputData
        if debug == False:
            self.isInputValid()
        
        
            

    def isInputValid(self):
        for i in self.input:
            if i != 0 and i != 1:
                raise ValueError("Input should be list of 0's and 1's")
        if len(self.input) < 20000:
            raise ValueError("Input should be list of at least 20000 elements")
        return True


    def frequencyMonobitTest(self):
        """
        This test is documented in section 2.1 of the NIST documentation.
        n should be at least 100.
        """
        n = len(self.input)
        S = 0
        for bit in self.input:
            if bit == 0:
                S -= 1
            else:
                S += 1
        s = abs(S)/math.sqrt(n)
        pval = math.erfc(s/math.sqrt(2))

        if pval < 0.01:
            return pval, False
        else:
            return pval, True
        

    def frequencyTestWithinBlock(self, M = 128):
        """
        This test is documented in section 2.2 of the NIST documentation.
        n should be at least 100.
        n must be greater than M*N where M is size of block and N is number of blocks created.
        N should be lower than 100.
        M >= 20
        M > 0.01*n
        N < 100

        For input size larger or equal to suggested size of 20000 bits, u can use M = (0.01*n) + 1 then all other conditions are met.
        """    
        blocks = []
        n = len(self.input)
        N = math.floor(n/M)

        for i in range(N):
            blocks.append(self.input[i*M:(i+1)*M])
        pis = []
        for i in range(N):
            denominator = 0
            for j in range(M):
                denominator += self.input[i*M+j]
            pis.append(denominator/M)

        chi_squared = 4*M*sum([(pi - 0.5)**2 for pi in pis])

        pval = gammaincc(N/2, chi_squared/2)

        return pval, pval >= 0.01
    

    def runsTest(self):
        """
        This test is documented in section 2.3 of the NIST documentation.
        n should be at least 100.
        """
        n = len(self.input)
        pi = sum(self.input)/n

        if abs(pi - 0.5) >= (2/math.sqrt(n)):
            pval = 0.0000
            return pval, pval >= 0.01
        V = 1
        for i in range(n-1):
            if self.input[i] != self.input[i+1]:
                V += 1
        pval = math.erfc(abs(V - 2*n*pi*(1-pi))/(2*math.sqrt(2*n)*pi*(1-pi)))
        return pval, pval >= 0.01
    
   
    def longestRunOfOnesInABlockTest(self):
        """
        This test is documented in section 2.4 of the NIST documentation.
        For M = 8, n should be at least 128.
        For M = 128, n should be at least 6272.
        For M = 10**4, n should be at least 750000.
        """
        n = len(self.input)
        if n < 128:
            raise ValueError("Input should be at least 128 bits")
        elif n < 6272 and n >= 128:
            M = 8
            K = 3
            N = math.floor(n / M)
            pis = [0.2148, 0.3672, 0.2305, 0.1875]
        elif n < 750000 and n >= 6272:
            M = 128
            K = 5
            N = math.floor(n / M)
            pis = [0.1174, 0.2430, 0.2493, 0.1752, 0.1027, 0.1124]
        else:
            M = 10**4
            N = math.floor(n / M)
            K = 6
            pis = [0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727]
        
        v = [0] * (K+1)

        blocks = []
        for i in range(math.floor(n / M)):
            blocks.append(self.input[i*M:(i+1)*M])
        
        if M == 8:
            for block in blocks:
                #get longest run of ones in block
                longest_run = 0
                current_run = 0
                for bit in block:
                    if bit == 1:
                        current_run += 1
                    else:
                        if current_run > longest_run:
                            longest_run = current_run
                        current_run = 0
                if current_run > longest_run:
                            longest_run = current_run
                if longest_run <= 1:
                    v[0] += 1
                elif longest_run == 2:
                    v[1] += 1
                elif longest_run == 3:
                    v[2] += 1
                elif longest_run >= 4:
                    v[3] += 1
            
        elif M == 128:
            for block in blocks:
                longest_run = 0
                current_run = 0
                for bit in block:
                    if bit == 1:
                        current_run += 1
                        if current_run > longest_run:
                            longest_run = current_run
                    else:
                        if current_run > longest_run:
                            longest_run = current_run
                        current_run = 0
                if current_run > longest_run:
                    longest_run = current_run
                if longest_run <= 4:
                    v[0] += 1
                elif longest_run == 5:
                    v[1] += 1
                elif longest_run == 6:
                    v[2] += 1
                elif longest_run == 7:
                    v[3] += 1
                elif longest_run == 8:
                    v[4] += 1
                elif longest_run >= 9:
                    v[5] += 1
        elif M == 10**4:
            for block in blocks:
                longest_run = 0
                current_run = 0
                for bit in block:
                    if bit == 1:
                        current_run += 1
                        if current_run > longest_run:
                            longest_run = current_run
                    else:
                        if current_run > longest_run:
                            longest_run = current_run
                        current_run = 0
                if current_run > longest_run:
                    longest_run = current_run
                if longest_run <= 10:
                    v[0] += 1
                elif longest_run == 11:
                    v[1] += 1
                elif longest_run == 12:
                    v[2] += 1
                elif longest_run == 13:
                    v[3] += 1
                elif longest_run == 14:
                    v[4] += 1
                elif longest_run == 15:
                    v[5] += 1
                elif longest_run >= 16:
                    v[6] += 1
        
        chi_squared = 0
        for i in range(len(v)):
            chi_squared += ((v[i] - (N*pis[i]))**2)/(N*pis[i])
        pval = gammaincc(K/2, chi_squared/2)
        return pval, pval >= 0.01


    def binaryMatrixRankTest(self):
        n = len(self.input)
        M = 32
        Q = 32
        N = math.floor(n/(M*Q))
        if N < 1:
            raise ValueError("Input should be at least 1024 bits")
        blocks = [[[0]*M] *Q for _ in range(N)]
        block_start = 0
        block_end = M
        for i in range(N):
            for j in range(Q):
                blocks[i][j] = self.input[block_start:block_end]
                block_start += M
                block_end += M

        ranks = [0, 0, 0]
        for block in blocks:
            matrix = BinaryMatrix(np.array(block))
            if matrix.compute_rank() == min(M, Q):
                ranks[0] += 1
            elif matrix.compute_rank() == min(M, Q) - 1:
                ranks[1] += 1
            else:
                ranks[2] += 1
        chi_squared = (ranks[0] - 0.2888*N)**2/(0.2888*N) + (ranks[1] - 0.5776*N)**2/(0.5776*N) + (ranks[2] - 0.1336*N)**2/(0.1336*N)
        pval = math.exp(-chi_squared/2)

        
        
        return pval, pval >= 0.01

    def discreteFourierTransformTest(self):
        n = len(self.input)

        X = [0] * n
        for i in range(n):
            if self.input[i] == 0:
                X[i] = -1
            else:
                X[i] = 1
        S = sff.fft(X)
        M = np.abs(S[0:math.floor(n/2)])
        T = math.sqrt(math.log(1 / 0.05) * n)
        N0 = 0.95*n/2
        N1 = len([m for m in M if m < T])
        
        d = (N1 - N0)/math.sqrt(n*0.95*0.05/4)
        pval = math.erfc(abs(d)/math.sqrt(2))

        return pval, pval >= 0.01
    
    
    def nonOverlappingTemplateMatchingTest(self, M = 8, template = "000000001"):
        n = len(self.input)
        pattern_len = len(template)
        N = math.floor(n/M)
        w = [0] * M
        for i in range(M):
            block_start = i*N
            block_end = (i+1)*N
            block = self.input[block_start:block_end]
            j = 0
            while j < N:
                if ''.join(map(str,block[j:j+pattern_len])) == template:
                    w[i] += 1
                    j += pattern_len
                else:
                    j += 1
        mu = (N - pattern_len + 1)/2**pattern_len
        sigma = N * ((1/(2**pattern_len) - (2*pattern_len-1)/(2**(2*pattern_len))))
        chi_squared = 0
        for i in range(M):
            chi_squared += (w[i] - mu)**2/sigma
        pval = gammaincc(M/2, chi_squared/2)
        return pval, pval >= 0.01

    
    def overlappingTemplateMatchingTest(self):
        n = len(self.input)
        template_len = 9
        template = '1' * template_len
        block_size = 1032
        v = [0] * 6
        N = math.floor(n/block_size)
        if N < 1:
            raise ValueError("Input should be at least 1032 bits")
        
        #count number of occurences of template in each block
        for i in range(N):
            block_start = i*block_size
            block_end = (i+1)*block_size
            block = self.input[block_start:block_end]
            j = 0
            noofoccurs = 0
            while j < block_size:
                if ''.join(map(str, block[j:j+template_len])) == template:
                    noofoccurs += 1
                j+=1
            if noofoccurs >= 5:
                v[5] += 1
            else:
                v[noofoccurs] += 1

        #calculate probabilities (3.8 in NIST documentation)
        piks = [0] * 6
        lambda_val = (block_size - template_len + 1)/2**template_len
        etha = lambda_val/2
        for i in range(5):
            if i != 0:
                piks[i] = 1.0 * etha * np.exp(2 * -etha) * (2 ** -i) * spc.hyp1f1(i + 1, 2, etha)
            else:
                piks[0] = 1.0 * np.exp(-etha)
        piks[5] = 1 - sum(piks)

        #calculate chi squared and pval
        chi_squared = 0.0
        for i in range(6):
            chi_squared += pow(v[i] - N *piks[i], 2.0)/ (N * piks[i])
        pval = gammaincc(5/2, chi_squared/2)
        return pval, pval >= 0.01

    def maurersUniversalStatisticalTest(self):
        n = len(self.input)

        if n < 387840:
            raise ValueError("Input should be at least 387840 bits")
        

        if n >= 387840:
            L = 6
        if n >= 904960:
            L = 7
        if n >= 2068480:
            L = 8
        if n >= 4654080:
            L = 9
        if n >= 10342400:
            L = 10
        if n >= 22753280:
            L = 11
        if n >= 49643520:
            L = 12
        if n >= 107560960:
            L = 13
        if n >= 231669760:
            L = 14
        if n >= 496435200:
            L = 15
        if n >= 1059061760:
            L = 16
        Q = 10 * 2**L
        K = math.floor(n/L) - Q
        max_bit_num = "1" * L
        max_bit_int = int(max_bit_num, 2)
        pos_vals = [0] * (max_bit_int + 1)
        L_expected = [5.2177052, 6.1962507, 7.1836656, 8.1764248, 9.1723243, 10.170032, 11.168765, 12.168070, 13.167693, 14.167488, 15.167379]
        L_variance = [2.954, 3.125, 3.238, 3.311, 3.356, 3.384, 3.401, 3.410, 3.416, 3.419, 3.421]
        block_start = 0
        block_end = L
        Q_iter = 0
        while Q_iter < Q:
            block = self.input[block_start:block_end]
            pos_vals[int(''.join(map(str, block)), 2)] = Q_iter+1
            block_start += L
            block_end += L
            Q_iter += 1

        block_start = Q*L
        block_end = block_start + L
        K_iter = 0
        suma = 0 
        while K_iter < K:
            block = self.input[block_start:block_end]
            bit_val = int(''.join(map(str, block)), 2)
            prev_indx = pos_vals[bit_val]
            curr_indx = K_iter + Q + 1
            suma += math.log(curr_indx-prev_indx, 2)
            pos_vals[bit_val] = curr_indx
            block_start += L
            block_end += L
            K_iter += 1
        test_stat = suma/K
        c = 0.7 - 0.8/L + (4 + 32/L)*pow(K, -3/L)/15
        sigma = c * math.sqrt(L_variance[L-6] / K)
        pval = math.erfc(abs((test_stat - L_expected[L-6])/(math.sqrt(2)*sigma)))

        return pval, pval >= 0.01

    def linearComplexityTest(self, M = 500):
        n = len(self.input)
        block_start = 0
        block_end = M
        blocks = []
        i = 0
        N = math.floor(n/M)
        while i<N:
            blocks.append(self.input[block_start:block_end])
            block_start += M
            block_end += M
            i+=1
        t0 = M/2
        t1 = (9+pow(-1, M+1))/(36)
        t2 = ((M/3) + (2/9))/(pow(2, M))
        theoretical_mean = t0 + t1 - t2
        v = [0] * 7

        for block in blocks:
            complexity = self.berlekamp_massey_algorithm(block)
            T = pow(-1, M) * (complexity - theoretical_mean) + (2/9)
            if T <= -2.5:
                v[0] += 1
            elif T > -2.5 and T <= -1.5:
                v[1] += 1
            elif T > -1.5 and T <= -0.5:
                v[2] +=1
            elif T > -0.5 and T <= 0.5:
                v[3] += 1
            elif T > 0.5 and T <= 1.5:
                v[4] += 1
            elif T > 1.5 and T <= 2.5:
                v[5] += 1
            else:
                v[6] += 1 
        
        chi = 0
        piks = [0.01047, 0.03125, 0.125, 0.5, 0.25, 0.0625, 0.020833]
        for i in range(7):
            chi += (pow(v[i] - N*piks[i], 2))/(N*piks[i]) 
        pval = spc.gammaincc(6 / 2.0, chi / 2.0)
        return pval, pval >= 0.01

    def berlekamp_massey_algorithm(self, block_data):
        """
        An implementation of the Berlekamp Massey Algorithm. Taken from Github [1]
        [1] - https://gist.github.com/StuartGordonReid/a514ed478d42eca49568
        The Berlekamp–Massey algorithm is an algorithm that will find the shortest linear feedback shift register (LFSR)
        for a given binary output sequence. The algorithm will also find the minimal polynomial of a linearly recurrent
        sequence in an arbitrary field. The field requirement means that the Berlekamp–Massey algorithm requires all
        non-zero elements to have a multiplicative inverse.
        :param block_data:
        :return:
        """
        n = len(block_data)
        c = np.zeros(n)
        b = np.zeros(n)
        c[0], b[0] = 1, 1
        l, m, i = 0, -1, 0
        while i < n:
            v = block_data[(i - l):i]
            v = v[::-1]
            cc = c[1:l + 1]
            d = (block_data[i] + np.dot(v, cc)) % 2
            if d == 1:
                temp = copy.copy(c)
                p = np.zeros(n)
                for j in range(0, l):
                    if b[j] == 1:
                        p[j + i - m] = 1
                c = (c + p) % 2
                if l <= 0.5 * i:
                    l = i + 1 - l
                    m = i
                    b = temp
            i += 1
        return l

    def serialTest(self, m = 16, mode = "single"):
        n = len(self.input)
        input_prim = self.input + self.input[0:m-1]
        input_prim = ''.join(map(str, input_prim))
        
        vm = [0] * pow(2, m)
        vm_1 = [0] * pow(2, m-1)
        vm_2 = [0] * pow(2, m-2)
        for i in range(n):
            vm[int(input_prim[i:i+m], 2)] += 1
            vm_1[int(input_prim[i:(i+m-1)], 2)] += 1
            vm_2[int(input_prim[i:(i+m-2)], 2)] += 1
        psim = 0
        psim_1 = 0
        psim_2 = 0
        for v in vm:
            psim += pow(v, 2)
        for v in vm_1:
            psim_1 += pow(v, 2)
        for v in vm_2:
            psim_2 += pow(v, 2)
        psim = (psim * (pow(2, m))/(n)) - n
        psim_1 = (psim_1 * (pow(2, m-1))/(n)) - n
        psim_2 = (psim_2 * (pow(2, m-2))/(n)) - n

        delta = psim - psim_1
        delta_squared = psim - 2*psim_1 + psim_2


        pval1 = spc.gammaincc(pow(2, m-2), delta/2)
        pval2 = spc.gammaincc(pow(2, m-3), delta_squared/2)
        if mode == "both":
            return (pval1, pval2), pval1 >= 0.01 and pval2 >= 0.01
        if mode == "single":
            return pval1, pval1 >= 0.01
        
    def approximateEntropyTest(self, m = 10):
        n = len(self.input)
        input_prim_m = self.input + self.input[:m-1]
        freqs_m = [0] * pow(2, m)
        for j in range(n):
            sequence = "".join(map(str, input_prim_m[j: (j+m)]))
            sequence_int = int(sequence, 2)
            freqs_m[sequence_int] += 1
        C_m = [0] * len(freqs_m)
        for i in range(len(freqs_m)):
            C_m[i] = freqs_m[i]/n
        phi_m = 0
        for i in range(len(C_m)):
            if C_m[i] != 0:
                phi_m += C_m[i] * math.log(C_m[i])

        input_prim_m_1 = self.input + self.input[:m]
        freqs_m_1 = [0] * pow(2, m+1)
        for j in range(n):
            sequence_1 = "".join(map(str, input_prim_m_1[j: (j+m+1)]))
            sequence_1_int = int(sequence_1, 2)
            freqs_m_1[sequence_1_int] += 1
        
        C_m_1 = [0] * len(freqs_m_1)
        for i in range(len(C_m_1)): 
            C_m_1[i] = freqs_m_1[i]/n
        phi_m_1 = 0
        for i in range(len(C_m_1)):
            if C_m_1[i] != 0:
                phi_m_1 += C_m_1[i] * math.log(C_m_1[i])
        ape = phi_m - phi_m_1
        chi = 2 * n * (math.log(2) - ape)
        pval = spc.gammaincc(pow(2, m-1), chi/2)
        return pval, pval>= 0.01
    
    def cumulativeSumsForwardTest(self):
        n = len(self.input)
        input_prim = [1] * n
        for i in range(n):
            if self.input[i] == 0:
                input_prim[i] = -1
        S = input_prim[0]
        z = S
        for i in range(1, n):
            S += input_prim[i]
            z = max(z, abs(S))

        t0 = 0
        start = math.floor((math.floor(-n/z)+1)/4)
        end = math.floor((math.floor(n/z)-1)/4)
        for k in range(start, end+1):
            t0 += norm.cdf(((4*k+1)*z)/(math.sqrt(n)))
            t0 -= norm.cdf(((4*k-1)*z)/(math.sqrt(n)))

        t1 = 0
        start = math.floor((math.floor(-n/z)-3)/4)
        end = math.floor((math.floor(n/z)-1)/4)
        for k in range(start, end+1):
            t1 += norm.cdf(((4*k+3)*z)/(math.sqrt(n)))
            t1 -= norm.cdf(((4*k+1)*z)/(math.sqrt(n)))
        
        pval = 1 - t0 + t1

        return pval, pval>=0.01

    def cumulativeSumsBackwardTest(self):
        n = len(self.input)
        input_prim = [1] * n
        for i in range(n):
            if self.input[i] == 0:
                input_prim[i] = -1
        S = input_prim[-1]
        z = S
        for i in range(n-2, -1, -1):
            S += input_prim[i]
            z = max(z, abs(S))

        t0 = 0
        start = math.floor((math.floor(-n/z)+1)/4)
        end = math.floor((math.floor(n/z)-1)/4)
        for k in range(start, end+1):
            t0 += norm.cdf(((4*k+1)*z)/(math.sqrt(n)))
            t0 -= norm.cdf(((4*k-1)*z)/(math.sqrt(n)))

        t1 = 0
        start = math.floor((math.floor(-n/z)-3)/4)
        end = math.floor((math.floor(n/z)-1)/4)
        for k in range(start, end+1):
            t1 += norm.cdf(((4*k+3)*z)/(math.sqrt(n)))
            t1 -= norm.cdf(((4*k+1)*z)/(math.sqrt(n)))
        
        pval = 1 - t0 + t1

        return pval, pval>=0.01
 
    def randomExcursionsTest(self):
        n = len(self.input)
        input_prim = [1] * n
        states = {
            -4: [0] * 6,
            -3: [0] * 6,
            -2: [0] * 6,
            -1: [0] * 6,
            1: [0] * 6,
            2: [0] * 6,
            3: [0] * 6,
            4: [0] * 6,
        }
        for i in range(n):
            if self.input[i] == 0:
                input_prim[i] = -1
        S = [0] * (n+2)
        S[1] = input_prim[0]
        c_start = 0
        cycles = []
        for i in range(2, n+1):
            S[i] = S[i-1] + input_prim[i-1]
            if S[i] == 0:
                cycles.append(S[c_start:i+1])
                c_start = i
        cycles.append(S[c_start:len(S)])
        J = len(cycles)
        for key in states.keys():
            for cycle in cycles:
                s = 0
                for item in cycle:
                    if item == key:
                        s+=1
                if s >=5:
                    states[key][5] += 1
                else:
                    states[key][s] += 1
        chis = {
            -4: 0,
            -3: 0,
            -2: 0,
            -1: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
        }
        
        for key in states.keys():
            for k in range(6):
                prob = self.get_probs_for_random_excursion(k, key)
                vk = states[key][k] 
                chis[key] += ((vk - (J*prob))**2)/(J*prob)
        pvals = {
            -4: 0,
            -3: 0,
            -2: 0,
            -1: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
        }
        for key in pvals.keys():
            pvals[key] = spc.gammaincc(5/2, chis[key]/2)
        
        return pvals

    def get_probs_for_random_excursion(self, k, x):
        if k == 0:
            return 1 - (1/(2*abs(x)))
        elif k == 5:
            return (1/(2*abs(x)))*(1-(1/(2*abs(x))))**4
        else:
            return (1/(4*(x**2)))*(1-(1/(2*abs(x))))**(k-1)
        
    def randomExcursionsVariantTest(self):
        n = len(self.input)
        input_prim = [1] * n
        for i in range(n):
            if self.input[i] == 0:
                input_prim[i] = -1
        S = [0] * (n+2)
        S[1] = input_prim[0]
        c_start = 0
        cycles = []
        for i in range(2, n+1):
            S[i] = S[i-1] + input_prim[i-1]
            if S[i] == 0:
                cycles.append(S[c_start:i+1])
                c_start = i
        cycles.append(S[c_start:len(S)])
        J = len(cycles)
        states = {
            -9: 0,
            -8: 0,
            -7: 0,
            -6: 0,
            -5: 0,
            -4: 0,
            -3: 0,
            -2: 0,
            -1: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
        }
        for cycle in cycles:
            for item in cycle:
                if item != 0:
                    if item <= -9:
                        states[-9] += 1
                    elif item >= 9:
                        states[9] += 1
                    else:
                        states[item] += 1
        pvals = {
            -9: 0,
            -8: 0,
            -7: 0,
            -6: 0,
            -5: 0,
            -4: 0,
            -3: 0,
            -2: 0,
            -1: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
        }         
        
        for key in states.keys():
            state_val = states[key]
            pvals[key] = spc.erfc((abs(state_val-J))/(math.sqrt(2*J*(4*abs(key)-2))))

        return pvals

class BinaryMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def compute_rank(self):
        """
        Compute the rank of a binary matrix using Gaussian elimination.
        """
        n_rows, n_cols = self.matrix.shape
        rank = min(n_rows, n_cols)
        m = min(n_cols, n_rows)
        i = 0
        while i < m-1:
            if self.matrix[i, i] == 0:
                for j in range(i+1, n_rows):
                    if self.matrix[j, i] == 1:
                        self.matrix[[i, j]] = self.matrix[[j, i]]
                        break
                else:
                    i += 1
                    continue
            if self.matrix[i, i] == 1:
                for j in range(i+1, n_rows):
                    if self.matrix[j, i] == 1:
                        self.matrix[j] = self.matrix[j] ^ self.matrix[i]
            i += 1
        
        i = m - 1
        while i > 0:
            if self.matrix[i, i] == 0:
                for j in range(i-1, -1, -1):
                    if self.matrix[j, i] == 1:
                        self.matrix[[i, j]] = self.matrix[[j, i]]
                        break
                else:
                    i -= 1
                    continue
            if self.matrix[i, i] == 1:
                for j in range(i-1, -1, -1):
                    if self.matrix[j, i] == 1:
                        self.matrix[j] = self.matrix[j] ^ self.matrix[i]
            i -= 1


        
        for i in range(n_rows):
            if np.all(self.matrix[i] == 0):
                rank -= 1
                
        return rank
    

