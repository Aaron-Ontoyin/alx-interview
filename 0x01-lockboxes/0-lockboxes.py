#!usr/bin//python3


def unlock(available_keys, locked_boxes):
	"""Unlock boxes"""
	print(locked_boxes, available_keys)
	if len(locked_boxes) == 0:
		return True

	for box in locked_boxes:
		box_id, box_content = box
		if box_id in available_keys:
			available_keys += box_content
			locked_boxes.remove(box)
			return unlock(available_keys, locked_boxes)

	return False


def canUnlockAll(boxes):
	"""Check if all boxes can be opened"""
	if len(boxes) == 0:
		return False

	available_keys = boxes[0]
	locked_boxes = list(enumerate(boxes))[1:]

	return unlock(available_keys, locked_boxes)
