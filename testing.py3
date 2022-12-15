def mergeTwoLists(list1, list2):
	merged_list = []
	while list1.next is not None and list2.next is not None:
		if list1.val < list2.val:
			merged_list.append(list1.val)
			list1 = list1.next
		if list2.val < list1.val:
			merged_list.append(list2.val)
			list2 = list2.next

	return merged_list

mergeTwoLists([1],[2])