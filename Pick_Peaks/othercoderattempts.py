""" Variation 1 """

def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}

""" Variation 2 """

# def pick_peaks(arr):
#     peak, pos = [], []
#     res = { "peaks":[], "pos":[] }

#     for i in range(1, len(arr)) :
#         if arr[i]>arr[i-1] :
#             peak, pos = [arr[i]], [i]

#         elif arr[i]<arr[i-1] :
#             res["peaks"] += peak
#             res["pos"] += pos
#             peak, pos = [], []

#     return res

# print(pick_peaks([1,2,3,6,4,1,2,3,2,1])) # {"pos":[3,7], "peaks":[6,3]})
# print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3])) # {"pos":[3,7], "peaks":[6,3]})
# print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])) # {"pos":[3,7,10], "peaks":[6,3,2]})
# print(pick_peaks([2,1,3,1,2,2,2,2,1])) # {"pos":[2,4], "peaks":[3,2]})
print(pick_peaks([2,1,3,1,2,2,2,2])) # {"pos":[2], "peaks":[3]})
# print(pick_peaks([2,1,3,2,2,2,2,5,6])) # {"pos":[2], "peaks":[3]})
# print(pick_peaks([2,1,3,2,2,2,2,1])) # {"pos":[2], "peaks":[3]})
# print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])) # {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
# print(pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7])) # {'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]})
# print(pick_peaks([])) # {"pos":[],"peaks":[]})
# print(pick_peaks([1,1,1,1])) # {"pos":[],"peaks":[]})