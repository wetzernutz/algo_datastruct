def _z_explicit_match_reverse(text, l_finger_start ,r_finger_start=-1):
    r_finger = r_finger_start
    l_finger = l_finger_start
    while l_finger >=0 and text[l_finger] == text[r_finger]:
        l_finger -= 1
        r_finger -= 1
    return l_finger

def z_algorithm_reverse_ian(string):
    n = len(string)
    z_array = [None] * n
    zbox_left, zbox_right = n, n

    i = n - 2
    while i >=0:
        if i > zbox_left:
            remaining = i - zbox_left
            k = i + (n-1-zbox_right)
            if z_array[k] < remaining:
                z_array[i] = z_array[k]
            elif z_array[k] > remaining:
                z_array[i] = remaining
            else:
                zbox_right = i
                zbox_left = _z_explicit_match_reverse(string, l_finger_start=zbox_left, r_finger_start=(n-1)-remaining)
                z_array[i] = zbox_right - zbox_left
        else:
            zbox_left = _z_explicit_match_reverse(string, l_finger_start=i)
            zbox_right = i
            z_array[i] = zbox_right - zbox_left
        i-=1
    return z_array