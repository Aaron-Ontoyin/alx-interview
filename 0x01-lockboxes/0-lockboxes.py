#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each
box may contain keys to the other boxes.
This module contains functions that determines if all the boxes can be opened
"""


def unlock(available_keys, locked_boxes):
    """Unlock boxes"""
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
