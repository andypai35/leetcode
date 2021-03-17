def merge(nums1, m, nums2, n) :

        
    while m > 0 and n > 0 :
        if nums1[m-1] < nums2[n-1]:
            nums1[m+n-1] = nums2[n-1]
            n-=1
        else:
            nums1[m+n-1],nums1[m-1] =  nums1[m-1] , nums1[m+n-1]
            m-=1

        print(m,n, nums1)
    if n > 0:
        print(nums2[:n])
        nums1[:n] =  nums2[:n]

merge([2,5,8,0,0,0], 3,[1,2,3], 3)
