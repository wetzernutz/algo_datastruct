def naive_pattern_match(text, pattern):
    count_arr = [0] * len(text)
    for i in range(len(text)):
        count = 0
        j = 0
        while j < len(pattern) and i+j < len(text):
            if pattern[j] == text[i+j]:
                count += 1
                j += 1
            else:
                break
        count_arr[i] = count
    return count_arr

def _z_explicit_match(text, r_finger_start, l_finger_start=0):
    l_finger = l_finger_start
    r_finger = r_finger_start
    while r_finger < len(text) and text[l_finger] == text[r_finger]:
        l_finger += 1
        r_finger += 1
    return r_finger

def z_algorithm(text):
    # q-k is the match count starting from k
    z_arr = [0] * len(text)
    l, r = float('-inf'), float('-inf')

    # # Base Case
    # k = 1
    # q = Z_explicit_match(text, start=k)
    # if q-k>0:     # q!=k ^ q>=k = q>k
    #     l, r = k, q-k
    #     z_arr[1] = q-k

    # set to start=2 if explicit base case
    for k in range(1, len(text)):
        # Case 1: r<k
        if r<k: # actually includes base case
            q = _z_explicit_match(text, r_finger_start=k)
            # if count=0, z_value is 1
            if q>k:
                z_arr[k] = q-k
                l, r = k, q - 1

        else:
            # Case 2a
            if z_arr[k-l] < r-k+1:
                z_arr[k] = z_arr[k-l]
            # Case 2b
            else:
                q = _z_explicit_match(text, r_finger_start=r+1, l_finger_start=r-k+1)
                # equal because if count=0, we still need to assign z value, as z_value is not 0 but length of alpha
                z_arr[k] = q-k
                l, r = k, q - 1
    return z_arr


def z_algorithm_pattern_match(text, pattern):
    string = pattern + '$' + text
    z_arr = z_algorithm(string)

    match_array = [False] * len(text)
    for i in range(len(pattern)+1, len(string)):
        if z_arr[i] == len(pattern):
            match_array[i-len(pattern)-1] = True
    return match_array

###################################
# Z-algorithm ian
# - r is now exclusive (r==q), zbox = str[i..r)
# - k is the i mirror in left box
# - remaining is the length(str[i..r))
###################################

""" Potential Bugs

1) set i=0
    sets zbox_right to len(str) since the entire str becomes the zbox
"""

def in_zbox(i, zbox_right):
    # i is always gt zbox_left (no zbox exists after i)
    return i < zbox_right

def z_algorithm_ian(string):
    z_array = [None] * len(string)
    zbox_left, zbox_right = -1, -1

    i = 1
    while i < len(string):
        if in_zbox(i, zbox_right):
            k = i - zbox_left
            remaining = zbox_right - i

            if z_array[k] < remaining:
                z_array[i] = z_array[k]
            elif z_array[k] > remaining:
                z_array[i] = remaining
            else:
                zbox_left = i
                zbox_right = _z_explicit_match(string, r_finger_start=zbox_right, l_finger_start=remaining)
                z_array[i] = zbox_right - zbox_left
        else:
            zbox_left = i
            zbox_right = _z_explicit_match(string, r_finger_start=i)
            z_array[i] = zbox_right - zbox_left
        i+=1
    return z_array




###########################################################
# THEORY DEMONSTRATION ONLY
###########################################################
def naive_z_array(string):
    """ Naive implementation(2 finger approach) of getting Z array

    Z[i] = longest prefix of string that matches substring starting at i for any i > 1
         = str[0..(a-1)] = str[i..i+(a-1)], where str[a] != str[i+a]
         = a

    Time Complexity: O(n^2)
    Total Comparisons = n + n-1 + n-2.. + 1 = n(n+1)/2
    Args:
        string: string

    Returns:
        Z array
    """
    Z = [0] * len(string)
    # Z[0] = len(string) # trivial (not used)

    for i in range(1, len(string)):
        l = 0
        r = i #  Note: l always < r
        while r < len(string) and string[l] == string[r]:
            l += 1
            r += 1
        Z[i] = l # think of l as keeping track of length of prefix
    return Z

class ZBox:
    """ Z-box for demonstration purposes
    for str[0..n-1]:
    if Z[i] = a
    Z-box = str[i..i+(a-1)]
    left_inner_bound = i
    right_inner_bound = i+(a-1)
    """
    def __init__(self, left_bound, length):
        self.left_bound = left_bound
        self.right_bound = left_bound + (length-1)

    def __len__(self):
        return self.right_bound - (self.left_bound-1)

    def __repr__(self):
        return f"({self.left_bound}, {self.right_bound})"

def convert_Z_arr_2_Z_box_arr(Z_arr):
    Z_box_arr = [None] * len(Z_arr)
    for i in range(1, len(Z_arr)):
        Z_i = Z_arr[i]
        if Z_i > 0:
            Z_box_arr[i] = ZBox(i, Z_i)
    return Z_box_arr

def demonstrate_l_i_r_i(string):
    """ Naive approach of demonstrating what is l and r in Z algorithm.
    """
    Z_arr = naive_z_array(string)
    Z_box_arr = convert_Z_arr_2_Z_box_arr(Z_arr)

    r_array = [None] * len(Z_arr)
    l_array = [None] * len(Z_arr)
    for i in range(1, len(Z_box_arr)):
        r = float('-inf')
        l = float('-inf')
        for j in range(1, i+1): # exclude 0, including i
            if (Z_box_arr[j] is not None) and (r < Z_box_arr[j].right_bound):
                r = Z_box_arr[j].right_bound
                l = Z_box_arr[j].left_bound # l is defined based on r
        r_array[i] = r
        l_array[i] = l
    return l_array, r_array




