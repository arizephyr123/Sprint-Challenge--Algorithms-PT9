class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    
    def __str__(self):
        return f'****\n{self._list}\nitem- {self._item}\nposition- {self._position}\nlight- {self._light}\n****'
    
    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        # print('in swap, dropping', self._item, 'grabbing ', self._list[self._position])
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def left_most_start(self):
        # print('back to start')
        while self.can_move_left():
            self.move_left()

    def right_most_end(self):
        # print('go to end')
        while self.can_move_right():
            self.move_right()
    
    def holding_none(self):
        """
        Returns True if the robot is holding None and False otherwise.
        """
        # print('in holding_none', self._item, self.compare_item())
        if self.compare_item() is not None:
            return False
        else:
            if self.can_move_right():
                self.move_right()
                if self.compare_item() is None:
                    # return to original position
                    self.move_left()
                    # print(f'{self._item} vs {self._list[self._position]}')
                    return True
                else: 
                    return False
            elif self.can_move_left():
                self.move_left()
                if self.compare_item() is None:
                    # print(f'{self._item}vs {self._list[self._position]}')
                    # return to original position
                    self.move_right()
                    return True
                else: 
                    return False

    def collect_none(self):
        if self.holding_none():
            # print('holding None? =>', self._item)
            return 
        else:
            if self.can_move_right():
                while self.can_move_right():
                    if self.compare_item() is not None:
                        # print('compare_item-> ', self.compare_item())
                        self.move_right()
                    else:
                        # print('holding before =>', self._item)
                        self.swap_item()
                        # print('now holding None? =>', self._item)
                        return
            elif self.can_move_left():
                while self.can_move_left():
                    if self.compare_item() is not None:
                        # print('compare_item-> ', self.compare_item())
                        self.move_left()
                    else:
                        # print('holding before =>', self._item)
                        self.swap_item()
                        # print('now holding None? =>', self._item)
                        return

    
    # PLAN
    # 2-way bubble sort
    # move to right, swap if carrying None or smaller item (bubble up large items and None)
    # then move left, swap if carrying larger item (bubble down small items)
    # after 'return' pass back 
        # if robot holding None, exit function
        # else run sort function again 
    
    def sort(self):
        while self.can_move_right() == True:
            if self.compare_item() is None or self.compare_item() == -1: # either holding None or robot holding smaller item
                self.swap_item()
                self.move_right()
            else:
                # keep moving right w/o swapping
                self.move_right()
        while self.can_move_left() is True:
            if self.compare_item() == 1: # robot holding larger item
                self.swap_item()
                self.move_left()
            else:
                self.move_left()
        # if robot hoding None then sorted
        # if robot NOT holding None, then repeat sort function
        if self._item is not None:
            self.sort()
        # tried using my own custom function 
        #  but the following extra function maxes out recursion stack
        # if self.holding_none() is False:
        #     self.sort()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [4, 3, 2, 1]

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    # print('None', robot._item)
    # robot.move_right()
    # print(robot._position)
    # robot.move_right()
    # print(robot._position)
    # robot.swap_item()
    # print('now holding', robot._item)
    # robot.collect_none()
    # print('None', robot._item)

    robot.sort()
    # print('holding', robot._item)
    # print('holding none?',  robot.holding_none())
    # robot.swap_item()
    # print('holding none?',  robot.holding_none())
    # robot.return_to_start()
    # print(robot._position)
    

    print(robot._list)