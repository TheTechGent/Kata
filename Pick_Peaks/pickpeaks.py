# Attempt 1 at optimising. 10 tests = 0.25ms, 100 tests = 6.49ms

def pick_peaks(arr):
    """function finds peaks in array of numbers."""

    # dexs[0,1,2,3,4,5,6,7]
    # nums[2,1,3,1,2,2,2,2]

    peaks_pos = {"pos": [], "peaks": []}
    dex = 1
    end = len(arr) - 1

    while dex < end:
        # Finds peaks
        if arr[dex] > arr[dex - 1] and arr[dex] > arr[dex + 1]:
            peaks_pos["pos"].append(dex)
            peaks_pos["peaks"].append(arr[dex])
            dex += 1

        # Finds plateau's
        elif arr[dex] == arr[dex + 1]:

            plateau_result = avoid_plateau(arr, dex)

            if plateau_result == 1:

                peaks_pos["pos"].append(dex)
                peaks_pos["peaks"].append(arr[dex])
                dex += 1

            else:
                dex = plateau_result
        else:
            dex += 1

    return peaks_pos

def avoid_plateau(arr, start_position) -> int:

    end_position = len(arr)
    num_before_plateau = arr[start_position - 1]
    num_after_plateau = 0
    plateau_num = arr[start_position]
    end_dex = 0

    for pos in range(start_position + 1, end_position):

        if pos == end_position - 1:
            end_dex = pos
            return end_dex

        elif arr[pos] == arr[pos + 1]:
            continue

        else:
            num_after_plateau = arr[pos + 1]
            end_dex = pos
            break

    if plateau_num > num_before_plateau and plateau_num > num_after_plateau:

        return 1

    else:

        return end_dex


print(pick_peaks([1,2,3,6,4,1,2,3,2,1])) # {"pos":[3,7], "peaks":[6,3]})
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3])) # {"pos":[3,7], "peaks":[6,3]})
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])) # {"pos":[3,7,10], "peaks":[6,3,2]})
print(pick_peaks([2,1,3,1,2,2,2,2,1])) # {"pos":[2,4], "peaks":[3,2]})
print(pick_peaks([2,1,3,1,2,2,2,2])) # {"pos":[2], "peaks":[3]})
print(pick_peaks([2,1,3,2,2,2,2,5,6])) # {"pos":[2], "peaks":[3]})
print(pick_peaks([2,1,3,2,2,2,2,1])) # {"pos":[2], "peaks":[3]})
print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])) # {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
print(pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7])) # {'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]})
print(pick_peaks([])) # {"pos":[],"peaks":[]})
print(pick_peaks([1,1,1,1])) # {"pos":[],"peaks":[]})


# Correct code - NOT OPTIMISED

# 10 tests = 0.28ms and 100 tests = 6.92ms

# def pick_peaks(arr):
#     """function finds peaks in array of numbers."""

#     peaks_pos = {"pos": [], "peaks": []}

#     for dex in range(1, len(arr) - 1):
#         # Finds peaks
#         if arr[dex] > arr[dex - 1] and arr[dex] > arr[dex + 1]:
#             peaks_pos["pos"].append(dex)
#             peaks_pos["peaks"].append(arr[dex])

#         # Finds plateau's
#         elif arr[dex] == arr[dex + 1]:

#             if avoid_plateau(arr, dex):
#                 peaks_pos["pos"].append(dex)
#                 peaks_pos["peaks"].append(arr[dex])

#     return peaks_pos

# def avoid_plateau(arr, start_position) -> bool:

#     end_position = len(arr)
#     num_before_plateau = arr[start_position - 1]
#     num_after_plateau = 0
#     plateau_num = arr[start_position]

#     for pos in range(start_position + 1, end_position):

#         if pos == end_position - 1:
#             num_after_plateau = arr[pos]
#             break

#         elif arr[pos] == arr[pos + 1]:
#             continue

#         else:
#             num_after_plateau = arr[pos + 1]
#             break

#     if plateau_num > num_before_plateau and plateau_num > num_after_plateau:

#         return True 

#     else:

#         return False