#Sample String : 'google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


sample = 'google.com'
dict = {}
for i in sample:
    dkeys = dict.keys()
    if i in dkeys:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

###############################################3333333333

#Sample String : 'restart'
#Expected Result : 'resta$t'

t_string = 'restartr'
ch = t_string[0]
t_string = t_string.replace(ch,'$')

t_string = ch + t_string[1:]

print(t_string)
###############################################3333333333

#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'

originals = 'abc'
original1 =(list(originals))
original1[0], original1[1] = original1[1],original1[0]
op = list('xyz')

op[0],op[1] = op[1],op[0]
print(op)
print(original1)
print("".join(original1) + ',' + "".join(op))
###############################################3333333333



def char_t(a,b):
    n_a = b[:2] + a[2:]
    n_b = a[:2] + b[2:]
    res = n_a + ',' + n_b
    return res
fi = char_t('abc','xpu')
print(fi)
###############################################3333333333
s_st =  'abchhing'
#op = 'abcing'

def con(a):
    if a[-3:] == 'ing':
        result = a + 'ly'
    else:
        result = a + 'ing'
    return result
final = con('abcje')
print(final)


ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
     "Thomas": 10,
     "Bob": 10,
     "Joseph": 11,
     "Maria": 12,
     "Gabriel": 10,
  }
v = list(ages.values())
k = list(ages.keys())
max_k = k[v.index(max(v))]
print(max_k)













