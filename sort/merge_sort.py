#!/usr/bim/python
#-*-coding:utf8-*-
import unittest
import time
import random
def selection_sort(orignal_list:list)->list:
    if len(orignal_list) == 0: return None
    sorted_list = []

    while orignal_list:
        j = float("inf")
        for i in orignal_list:
            if i<j:
                j = i
        sorted_list.append(j)
        orignal_list.remove(j)
    return sorted_list

def insertion_sort(orignal_list:list)->list:
    if len(orignal_list) == 0: return None
    sorted_list = []
    sorted_list.append(orignal_list[0])
    for i in orignal_list[1:]:
        if i >= sorted_list[-1]:
            sorted_list.append(i)
            continue
        for j,v in enumerate(sorted_list):
            if i <= v:
                sorted_list.insert(j, i)


                break

    return sorted_list

def bublle_sort(orignal_list:list)->list:

    if len(orignal_list) == 0: return None
    left_list_len = len(orignal_list)-1
    for j in range(len(orignal_list)-1):
        for i in range(left_list_len):
            if orignal_list[i]>orignal_list[i+1]:
                swap = orignal_list[i]
                orignal_list[i] = orignal_list[i + 1]
                orignal_list[i + 1] = swap
        left_list_len -= 1
    return orignal_list

def maerge_sort(orignal_list:list)->list:
    if len(orignal_list) == 0: return None
    sorted_list = []
    list_len = len(orignal_list)
    if  list_len <= 1:
        return orignal_list
    else:
        left_sorted_list = maerge_sort(orignal_list[:list_len//2])
        right_sorted_list = maerge_sort(orignal_list[list_len // 2:])



        for i in range(list_len):
            left_sorted_list.append(float("inf"))
            right_sorted_list.append(float("inf"))
            if left_sorted_list[0] < right_sorted_list[0]:
                #print("5**", left_sorted_list[0])
                sorted_list.append(left_sorted_list[0])
                left_sorted_list.pop(0)
                #print("6***", sorted_list)
            else:
                sorted_list.append(right_sorted_list[0])
                right_sorted_list.pop(0)
    return sorted_list


def quick_sort(orignal_list):
    if len(orignal_list) == 0: return None
    sorted_list = []
    if len(orignal_list) == 1: return orignal_list
    if len(orignal_list) == 2:
        return orignal_list if orignal_list[0] < orignal_list[1] else orignal_list[::-1]
    left_orignal_list = []
    right_orignal_list = []
    flag = orignal_list[0]
    for i in orignal_list[1:]:
        if i < flag:
            left_orignal_list.append(i)
             #print("333", left_orignal_list)
        else:
            right_orignal_list.append(i)

    if len(left_orignal_list) == 0:
        left_orignal_list.append(flag)
    else:
        right_orignal_list.append(flag)

    left_sorted_list = quick_sort(left_orignal_list)
    right_sorted_list = quick_sort(right_orignal_list)

    return left_sorted_list + right_sorted_list



    return sorted_list




class TestSort(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_all_sorts(self):
        original_list = [\
            [6,5,4,3,2,1],\
            [1,2,3,4,5,6],\
            [1,3,6,2,4,5],\
            ]

        for i in original_list:
            self.assertEqual(selection_sort(i[:]),[1,2,3,4,5,6],msg = "selection_sort")
            self.assertEqual(insertion_sort(i[:]),[1,2,3,4,5,6], msg = "insertion_sort")
            self.assertEqual(bublle_sort(i[:]), [1, 2, 3, 4, 5, 6], msg = "bublle_sort")
            self.assertEqual(maerge_sort(i[:]), [1, 2, 3, 4, 5, 6], msg = "maerge_sort")
            self.assertEqual(quick_sort(i[:]), [1, 2, 3, 4, 5, 6], msg="quick_sort")

    def _test_speed(self, fun, original_list):

        time_start = time.process_time()
        #print("11111", time_start)
        fun(original_list)
        time_end = time.process_time()
        #print("22222", time_end)
        return time_end - time_start

    def get_original_list(self):
        original_list = []
        for i in range(30000):
            #original_list.append(i)
            original_list.append(random.randint(0,100000000))
        with open("num.txt","w") as f:
            for i in original_list:
                f.write(", "+ str(i))
        return original_list
    def test_compare_speed(self):

        print("test_compare_speed")
        original_list = self.get_original_list()
        print("selection_sort", self._test_speed(selection_sort,original_list[:]))
        print("insertion_sort", self._test_speed(insertion_sort, original_list[:]))
        print("bublle_sort", self._test_speed(bublle_sort, original_list[:]))
        print("maerge_sort", self._test_speed(maerge_sort, original_list[:]))
        print("quick_sort", self._test_speed(quick_sort, original_list[:]))

        s1 = selection_sort(original_list[:])
        s2 = insertion_sort( original_list[:])
        s3 = bublle_sort( original_list[:])
        s4 = maerge_sort( original_list[:])
        s5 = quick_sort(original_list[:])
        self.assertEqual(s1, s2)
        self.assertEqual(s2, s3)
        self.assertEqual(s3, s4)
        self.assertEqual(s4, s5)


if __name__ == "__main__":


    unittest.main()